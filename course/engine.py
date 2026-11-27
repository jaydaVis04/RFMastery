"""Course orchestration. Learner programs execute as local processes, never via a shell."""
import argparse
from datetime import datetime, timezone, timedelta
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import random
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from . import terminal as ui
from .terminal import print, ask as input

ROOT = Path(__file__).resolve().parent.parent
CATALOG = json.loads((ROOT / 'course/catalog.json').read_text())
STATE = Path(os.environ.get('SIGNAL_STATION_STATE', ROOT / '.progress/state.json'))
INTERVALS = (1, 3, 7, 14, 30)


class CourseError(Exception):
    pass


def now():
    return datetime.now(timezone.utc)


def stamp():
    return now().isoformat()


def load_state():
    if not STATE.exists():
        return {'version': 1, 'missions': {}, 'cards': {}}
    try:
        state = json.loads(STATE.read_text())
        if state.get('version') != 1 or not isinstance(state.get('missions'), dict) or not isinstance(state.get('cards'), dict):
            raise ValueError('unsupported state schema')
        return state
    except (ValueError, OSError) as exc:
        raise CourseError(f'Cannot read progress at {STATE}: {exc}. Back it up before repairing; it has not been overwritten.') from exc


def save_state(state):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    # Atomic replacement prevents a partially written JSON file after interruption.
    with tempfile.NamedTemporaryFile(mode='w', dir=STATE.parent, prefix='.state-', delete=False) as f:
        json.dump(state, f, indent=2)
        f.write('\n')
        tmp = Path(f.name)
    try:
        tmp.replace(STATE)
    finally:
        tmp.unlink(missing_ok=True)


def mission(number):
    if not 1 <= number <= len(CATALOG):
        raise CourseError(f'Mission must be 1–{len(CATALOG)}.')
    return CATALOG[number - 1]


def record(state, m):
    return state['missions'].setdefault(str(m['id']), {})


def digest(m, source_dir=None):
    folder = Path(source_dir) if source_dir else ROOT / m['path']
    h = hashlib.sha256()
    names = sorted(m['files'] + (['lab.h'] if m['kind'] == 'c' else []))
    for name in names:
        p = folder / name
        h.update(name.encode())
        h.update(p.read_bytes() if p.exists() else b'<missing>')
    return h.hexdigest()


def current(state):
    for m in CATALOG:
        r = state['missions'].get(str(m['id']), {})
        if not r.get('flag') or r.get('source_digest') != digest(m):
            return m
    return CATALOG[-1]


def run(command, cwd=None, timeout=25, quiet=False, env=None):
    if not quiet:
        print('$ ' + shlex.join([str(x) for x in command]), flush=True)
    try:
        result = subprocess.run([str(x) for x in command], cwd=cwd or ROOT,
                                capture_output=True, text=True, timeout=timeout,
                                env=env, errors='replace')
    except FileNotFoundError as exc:
        raise CourseError(f'Missing command {command[0]}. Run ./learn doctor for setup.') from exc
    except subprocess.TimeoutExpired as exc:
        partial = (exc.stdout or b'')
        if isinstance(partial, bytes):
            partial = partial.decode(errors='replace')
        raise CourseError(f'Timed out after {timeout}s: {command[0]}. Check for an infinite loop.\n{partial[-3000:]}') from exc
    if not quiet or result.returncode:
        if result.stdout:
            print(result.stdout[-12000:], end='')
        if result.stderr:
            print(result.stderr[-12000:], end='', file=sys.stderr)
    return result


def compiler():
    command = shlex.split(os.environ.get('CC', 'cc'))
    if not command:
        raise CourseError('CC is empty.')
    return command


def cflags(plain=False, optimized=False):
    flags = ['-std=c17', '-Wall', '-Wextra', '-Wpedantic', '-Werror', '-g', '-O2' if optimized else '-O1']
    if not plain:
        flags += ['-fsanitize=address,undefined', '-fno-omit-frame-pointer', '-fno-sanitize-recover=all']
    return flags


def build_c(m, source_dir, build, plain, quiet=False):
    folder = ROOT / m['path']
    executable = build / 'lab'
    sources = [source_dir / 'lab.c']
    if m['kind'] != 'console':
        sources += [folder / 'tests.c']
    command = compiler() + cflags(plain) + m.get('flags', []) + ['-I', folder] + sources + ['-lm', '-o', executable]
    if run(command, quiet=quiet).returncode:
        return None
    return executable


def golden_vectors(build, quiet=False):
    golden = build / 'golden'
    command = compiler() + cflags() + [ROOT / 'course/golden.c', '-o', golden]
    if run(command, quiet=quiet).returncode:
        return False
    rng = random.Random(20261126)
    values = [32767, 0, 0, 0] + [0]*8 + [12000]*20 + [-32768, 32767]*20 + [-1, -2, -3, 0]
    values += [rng.randint(-32768, 32767) for _ in range(512-len(values))]
    source = build / 'samples.txt'
    expected = build / 'expected.txt'
    source.write_text(''.join(f'{x}\n' for x in values))
    result = run([golden, source, expected], quiet=quiet)
    if result.returncode:
        return False
    output = [int(x) for x in expected.read_text().split()]
    # Independent Python formula validates the C golden arithmetic, including negative rounding.
    oracle = []
    z1 = z2 = 0
    for x in values:
        acc = 8192*x + 16384*z1 + 8192*z2
        y = (abs(acc)//32768) * (-1 if acc < 0 else 1)
        oracle.append(max(-32768, min(32767, y)))
        z2, z1 = z1, x
    if output != oracle:
        raise CourseError('C golden model disagrees with Python; course validation failed.')
    (build / 'inputs.hex').write_text(''.join(f'{x & 0xffff:04x}\n' for x in values))
    (build / 'expected.hex').write_text(''.join(f'{x & 0xffff:04x}\n' for x in output))
    return True


def check(m, plain=False, source_dir=None, quiet=False):
    """Return True only when a real check executes successfully; missing tools never pass."""
    folder = ROOT / m['path']
    src = Path(source_dir) if source_dir else folder
    build = ROOT / '.build' / f'{m["id"]:02d}'
    build.mkdir(parents=True, exist_ok=True)
    if not quiet:
        print(f'\nMISSION {m["id"]:02d} · {m["title"]}')
    kind = m['kind']
    if kind in ('c', 'console'):
        binary = build_c(m, src, build, plain, quiet)
        if binary is None:
            return False
        result = run([binary], cwd=build, quiet=quiet)
        passed = result.returncode == 0
        if kind == 'console':
            passed = passed and result.stdout == 'SIGNAL STATION ONLINE\n'
            if not passed and not quiet:
                print('Expected exactly: SIGNAL STATION ONLINE followed by a newline; exit status 0.')
    elif kind == 'python':
        passed = run([sys.executable, folder / 'test_lab.py', src / 'lab.py'], quiet=quiet).returncode == 0
    elif kind == 'hdl':
        for tool in ('iverilog', 'vvp'):
            if not shutil.which(tool):
                raise CourseError(f'{tool} is not installed. HDL checks cannot run. See docs/SETUP.md; C/RF missions remain available.')
        if m.get('golden') and not golden_vectors(build, quiet):
            return False
        binary = build / 'simulation'
        result = run(['iverilog', '-g2012', '-Wall', '-s', 'tb', '-o', binary, src / 'lab.v', folder / 'tb.v'], quiet=quiet)
        if result.returncode:
            return False
        result = run(['vvp', binary], cwd=build, quiet=quiet)
        passed = result.returncode == 0 and 'PASS' in result.stdout.splitlines()
    elif kind == 'capstone':
        return check_capstone(m, src, build, plain, quiet)
    elif kind == 'design':
        p = src / 'design.md'
        words = p.read_text().split() if p.exists() else []
        required = 400 if m['id'] == 36 else 200
        passed = len(words) >= required
        if not quiet:
            print(f'Draft check: {len(words)} words; minimum {required}.')
            print('This verifies a substantial draft exists. Technical accuracy and oral explanations are self-assessed.')
    else:
        raise CourseError(f'Unknown check type: {kind}')
    if not quiet:
        print('CHECK PASSED' if passed else 'CHECK FAILED — fix the first failure, then try again.')
    return passed


def check_capstone(m, src, build, plain, quiet=False, optimized=False):
    folder = ROOT / m['path']
    modules = [src / n for n in ('decode.c', 'ring.c', 'dsp.c')]
    flags = compiler() + cflags(plain, optimized) + ['-I', src, '-I', folder]
    unit = build / 'modules'
    if run(flags + modules + [folder / 'tests.c', '-lm', '-o', unit], quiet=quiet).returncode:
        return False
    if run([unit], cwd=build, quiet=quiet).returncode:
        return False
    binary = build / 'pipeline'
    if run(flags + modules + [src / 'main.c', '-lm', '-o', binary], quiet=quiet).returncode:
        return False
    passed = run([sys.executable, ROOT / 'course/check_pipeline.py', binary], quiet=quiet).returncode == 0
    if not quiet:
        print('CHECK PASSED' if passed else 'CHECK FAILED — inspect the module/CLI diagnostic above.')
    return passed


def remember(state, m, index, correct):
    key = f'{m["id"]}:{index}'
    card = state['cards'].setdefault(key, {'stage': 0, 'correct': 0, 'misses': 0})
    if correct:
        stage = min(card['stage'], len(INTERVALS)-1)
        card['due'] = (now()+timedelta(days=INTERVALS[stage])).isoformat()
        card['stage'] = min(stage+1, len(INTERVALS)-1)
        card['correct'] += 1
    else:
        card['stage'] = 0
        card['misses'] += 1
        card['due'] = (now()+timedelta(minutes=10)).isoformat()
    card['last'] = stamp()


def card_pool(m):
    if m['id'] == 36:
        pool = [(other, i) for other in CATALOG for i in range(len(other['quiz']))]
        # Ensure core tracks appear, then mix the remaining questions.
        core = [CATALOG[i-1] for i in (5, 8, 9, 16, 17, 21, 23, 25, 26, 32)]
        selected = [(other, random.randrange(len(other['quiz']))) for other in core]
        selected += random.sample([x for x in pool if x not in selected], 2)
        random.shuffle(selected)
        return selected
    return [(m, i) for i in range(len(m['quiz']))]


def quiz(state, m):
    pool = card_pool(m)
    passed = True
    print(f'\nRecall check: {len(pool)} questions. Answer from memory; choices are shuffled.')
    for other, index in pool:
        question = other['quiz'][index]
        choices = [question['answer']] + question['distractors']
        random.shuffle(choices)
        print('\n' + question['prompt'])
        for i, text in enumerate(choices, 1):
            print(f'  {i}. {text}')
        while True:
            answer = input('Answer 1–3 (q to stop): ').strip().lower()
            if answer == 'q':
                save_state(state)
                return False
            if answer in ('1', '2', '3'):
                break
            print('Enter 1, 2, 3, or q.')
        correct = choices[int(answer)-1] == question['answer']
        remember(state, other, index, correct)
        save_state(state)
        print('Correct.' if correct else f'Not yet. Model answer: {question["answer"]}')
        passed &= correct
    r = record(state, m)
    if passed:
        r['quiz_at'] = stamp()
    else:
        r.pop('quiz_at', None)
    save_state(state)
    print('QUIZ PASSED' if passed else 'Review the missed concepts, then retake this quiz. Mistakes enter your review queue.')
    return passed


def review(state, limit=10, all_cards=False):
    due = []
    for key, card in state['cards'].items():
        if all_cards or datetime.fromisoformat(card['due']) <= now():
            due.append((key, card))
    due.sort(key=lambda x: (x[1]['due'], -x[1]['misses']))
    if not due:
        print('No cards due. Start a lesson quiz, or use ./learn review --all to practice early.')
        return
    for key, _ in due[:limit]:
        number, index = map(int, key.split(':'))
        m = mission(number)
        question = m['quiz'][index]
        print(f'\nMission {number:02d}: {question["prompt"]}')
        response = input('Recall in your own words (q stops): ').strip()
        if response.lower() == 'q':
            break
        if not response:
            print('Try to retrieve an answer before revealing the model. Blank records a miss.')
        print('Model: ' + question['answer'])
        while True:
            rating = input('Self-assess: 0=missed, 1=partial, 2=correct: ').strip()
            if rating in ('0', '1', '2'):
                break
        remember(state, m, index, bool(response) and rating == '2')
        state['cards'][key]['last_response'] = response
        save_state(state)
    print('Review saved. Correct cards use 1/3/7/14/30-day defaults; missed/partial cards return after 10 minutes.')


def explain(state, m):
    print('\n' + m['explain'])
    print('Speak aloud first. Then write a short explanation with one concrete example and one failure mode.')
    print('Enter multiple lines; finish with a line containing only a period. q cancels.')
    lines = []
    while True:
        line = input()
        if line == 'q' and not lines:
            return False
        if line == '.':
            break
        lines.append(line)
    text = '\n'.join(lines).strip()
    if len(text.split()) < 30:
        print('Write at least 30 words so there is something useful to revisit. Nothing was saved.')
        return False
    print('Rubric: correct mechanism; concrete example; boundary/failure; tradeoff or limitation.')
    answer = input('Can you explain this without notes and defend those points? [y/n]: ').strip().lower()
    r = record(state, m)
    r['explanation'] = {'text': text, 'at': stamp(), 'self_assessed': answer == 'y'}
    save_state(state)
    print('Explanation saved. This is a self-assessment, not an automatic semantic grade.')
    return answer == 'y'


def submit(state, m, plain=False):
    r = record(state, m)
    if m['id'] == 36:
        missing = [str(x['id']) for x in CATALOG[:-1]
                   if not state['missions'].get(str(x['id']), {}).get('flag')
                   or state['missions'][str(x['id'])].get('source_digest') != digest(x)]
        if missing:
            print('Final mission needs current flags for missions: ' + ', '.join(missing))
            return False
    if not check(m, plain):
        r.pop('checked_at', None)
        save_state(state)
        return False
    r['checked_at'] = stamp()
    r['checked_digest'] = digest(m)
    r['sanitized'] = m['kind'] in ('c', 'console', 'capstone') and not plain
    missing = []
    if not r.get('quiz_at'):
        missing.append(f'./learn quiz {m["id"]}')
    if not r.get('explanation', {}).get('self_assessed'):
        missing.append(f'./learn explain {m["id"]}')
    if m['id'] == 34:
        report = ROOT / m['path'] / 'ENGINEERING.md'
        if not report.exists() or len(report.read_text().split()) < 120:
            missing.append('Complete mission 34 ENGINEERING.md (at least 120 words; see its rubric).')
    if missing:
        save_state(state)
        print('Checks pass. Complete these steps before the flag:\n  ' + '\n  '.join(missing))
        return False
    token = hashlib.sha256(f'signal-station-v1:{m["id"]}:{digest(m)}'.encode()).hexdigest()[:12]
    r['flag'] = f'SIGNAL{{{m["id"]:02d}_{token}}}'
    r['source_digest'] = digest(m)
    r['awarded_at'] = stamp()
    save_state(state)
    ui.flag(r['flag'])
    if r.get('assisted'):
        print('Assisted practice recorded. Rebuild a variation from memory on a later day.')
    if plain and m['kind'] in ('c', 'console', 'capstone'):
        print('Plain build: sanitizer validation was not performed for this submission.')
    if m['id'] < 36:
        print(f'Next suggested mission: ./learn lesson {m["id"]+1}')
    else:
        print('Training route complete. Revisit due cards and request a human review of your capstones and explanations.')
    return True


def status(state, full=False):
    flags = sum(bool(state['missions'].get(str(m['id']), {}).get('flag')) for m in CATALOG)
    current_flags = sum(bool(state['missions'].get(str(m['id']), {}).get('flag')) and
                        state['missions'][str(m['id'])].get('source_digest') == digest(m) for m in CATALOG)
    due = sum(datetime.fromisoformat(c['due']) <= now() for c in state['cards'].values())
    next_mission = current(state)
    next_label = f'{next_mission["id"]:02d} · {next_mission["title"]}'
    ui.dashboard(current_flags, len(CATALOG), flags, due, next_label)
    if full:
        rows = []
        for m in CATALOG:
            r = state['missions'].get(str(m['id']), {})
            label = 'READY'
            if r.get('flag'):
                label = 'COMPLETE' if r.get('source_digest') == digest(m) else 'CHANGED'
            elif r.get('checked_digest') == digest(m):
                label = 'CODE PASSED'
            rows.append((m['id'], label, m['title'], m['track'], bool(r.get('assisted'))))
        ui.course_map(rows)
    if not ui.styled():
        print(f'\nSuggested next: {next_label}')
    if not ui.styled():
        print('Progress is local. Flags indicate practice completion, not a guarantee of mastery.')


def doctor(require_hdl=False):
    print(f'Python: {sys.version.split()[0]}\nWorkspace: {ROOT}\nProgress: {STATE}')
    backend = {'installed': 'Rich (installed)', 'pip-bundled': 'Rich bundled with pip (offline fallback)',
               'plain': 'plain text; run ./learn setup for Rich'}[ui.BACKEND]
    print(f'Interface: {backend}')
    core_ok = sys.version_info >= (3, 10)
    print('\nC / RF lessons')
    with tempfile.TemporaryDirectory(prefix='signal-doctor-') as d:
        d = Path(d)
        source = d / 'probe.c'
        source.write_text('#include <stdio.h>\nint main(void){puts("toolchain ready");return 0;}\n')
        cc = compiler()
        if not shutil.which(cc[0]):
            raise CourseError(f'C compiler missing: {cc[0]}. See docs/SETUP.md.')
        for plain in (True, False):
            exe = d / ('plain' if plain else 'sanitized')
            built = run(cc+cflags(plain)+[source, '-o', exe], quiet=True).returncode == 0
            works = built and run([exe], quiet=True).returncode == 0
            print(('C17 build/run' if plain else 'AddressSanitizer + UBSan') + ': ' + ('OK' if works else 'UNAVAILABLE'))
            core_ok &= works
        print('\nFPGA lessons — Icarus Verilog is needed when you reach these missions')
        hdl_ok = all(shutil.which(name) for name in ('iverilog', 'vvp'))
        if hdl_ok:
            hdl_source = d / 'probe.v'
            hdl_binary = d / 'simulation'
            hdl_source.write_text('module tb; reg [3:0] data=10; reg [1:0] sel=1; wire y;\n'
                                  'assign y=data[sel]; initial begin #1; '
                                  'if(y!==1\'b1)$fatal(1,"mux failed"); '
                                  '$display("PASS");$finish;end endmodule\n')
            built = run(['iverilog', '-g2012', '-s', 'tb', '-o', hdl_binary, hdl_source], quiet=True).returncode == 0
            if built:
                result = run(['vvp', hdl_binary], cwd=d, quiet=True)
                hdl_ok = result.returncode == 0 and 'PASS' in result.stdout.splitlines()
            else:
                hdl_ok = False
            print('Verilog compile + simulation: ' + ('OK' if hdl_ok else 'FAILED'))
        else:
            print('MISSING: iverilog / vvp. Optional for C; install later with ./learn setup --fpga.')
    print('\nOptional tools — these do not block the course')
    debugger = shutil.which('lldb') or shutil.which('gdb')
    print(f'Debugger: {debugger or "not installed (optional for automated checks)"}')
    print(f'GTKWave waveform viewer: {shutil.which("gtkwave") or "not installed (optional)"}')
    if platform.system() == 'Darwin' and platform.machine() in ('arm64', 'aarch64'):
        print('Valgrind: not required on Apple Silicon; use the working ASan/UBSan builds.')
    else:
        print(f'Valgrind: {shutil.which("valgrind") or "not installed (optional)"}')
    print('\nC / RF: ' + ('READY' if core_ok else 'NEEDS SETUP'))
    print('FPGA: ' + ('READY' if hdl_ok else 'NEEDS SETUP'))
    if core_ok and hdl_ok:
        print('All required tool checks passed. Start with ./learn')
    elif core_ok:
        print('You can start C now with ./learn. Only the five FPGA missions need the missing simulator.')
    return core_ok and (hdl_ok or not require_hdl)


def setup(fpga=False):
    """Set up Python packages; install/validate native FPGA tools only when explicitly selected."""
    print('Setting up Signal Station. Learner files and progress are preserved.', flush=True)
    if ui.BACKEND != 'installed':
        print('Installing Rich into .deps (project-local Python packages)...', flush=True)
        result = run([sys.executable, '-m', 'pip', 'install', '--disable-pip-version-check', '--no-cache-dir',
                      '--target', ROOT / '.deps', '-r', ROOT / 'requirements.txt'], timeout=180)
        if result.returncode:
            raise CourseError('Rich installation was blocked or failed. The existing offline interface remains usable. '
                              'Run ./learn setup in your normal terminal to install dependencies with network access.')
        ui.load_backend()
        if ui.BACKEND != 'installed':
            raise CourseError('Rich could not be imported after installation. See docs/SETUP.md.')
    if fpga and not all(shutil.which(name) for name in ('iverilog', 'vvp')):
        if platform.system() != 'Darwin':
            raise CourseError('Install Icarus Verilog with your system package manager (Debian/Ubuntu: '
                              'sudo apt install iverilog), then rerun ./learn setup --fpga. See docs/SETUP.md.')
        brew = shutil.which('brew')
        if not brew:
            raise CourseError('Homebrew is not installed. See docs/SETUP.md for the official Icarus installation guide.')
        result = run([brew, 'install', 'icarus-verilog'], timeout=600)
        if result.returncode:
            raise CourseError('Icarus installation failed or was blocked. If this ran inside the restricted '
                              'agent session, run ./learn setup --fpga once in your normal terminal. It needs '
                              'network access and permission to write Homebrew directories. '
                              'Do not change directory ownership just to bypass the agent sandbox.')
    elif fpga:
        print('Icarus Verilog is already installed; no package installation needed.')
    else:
        print('Python-only setup selected; no system packages will be installed.')
    if not doctor(require_hdl=fpga):
        return False
    if not fpga:
        print('\nSetup complete for C / RF study. Start with ./learn. Add FPGA tools later with ./learn setup --fpga.')
        return True
    print('\nVerifying the five FPGA missions against reference implementations...', flush=True)
    result = run([sys.executable, ROOT / 'tools/validate_course.py', '--hdl-only', '--require-hdl'], timeout=180)
    if result.returncode:
        print('Tools are installed, but an FPGA reference check failed. Read the diagnostic above; no flags were awarded.')
        return False
    print('\nSetup complete. Start the course with ./learn')
    return True


def benchmark(m):
    if m['id'] != 34:
        raise CourseError('Benchmark is available for mission 34.')
    build = ROOT / '.build/34'
    build.mkdir(parents=True, exist_ok=True)
    if not check_capstone(m, ROOT / m['path'], build, True, optimized=True):
        return False
    import struct
    count = 250000
    data = build / 'benchmark.iq'
    data.write_bytes(struct.pack('<hh', 1000, -2000)*count)
    elapsed = []
    for i in range(3):
        start = time.perf_counter()
        result = run([build / 'pipeline', data, build / 'benchmark_out.iq'], quiet=True)
        seconds = time.perf_counter()-start
        if result.returncode:
            return False
        elapsed.append(seconds)
    seconds = sorted(elapsed)[1]
    report = {'at': stamp(), 'samples': count, 'seconds_median': seconds,
              'samples_per_second': count/seconds, 'input_payload_MB_per_second': 4*count/seconds/1e6,
              'build': 'C17 -O2, plain', 'scope': 'offline regular-file processing, includes process and file I/O'}
    p = build / 'benchmark.json'
    p.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    print(f'Saved {p.relative_to(ROOT)}. Record the measured result and limitations in ENGINEERING.md.')
    return True


def show_solution(state, m):
    solution = ROOT / 'course/solutions' / f'{m["id"]:02d}'
    if not solution.exists():
        print('This mission uses a prose rubric. Compare your draft with the requirements in its README and docs/INTERVIEW.md.')
        return
    record(state, m)['assisted'] = stamp()
    save_state(state)
    print('REFERENCE SOLUTION — assisted practice recorded. Your files are unchanged.')
    for path in sorted(solution.iterdir()):
        print(f'\n--- {path.name} ---')
        ui.syntax(path.read_text(), path.suffix.lstrip('.').replace('v', 'verilog') if path.suffix == '.v' else
                  'python' if path.suffix == '.py' else 'c')


def menu(state):
    while True:
        m = current(state)
        status(state)
        ui.menu()
        choice = input('Choose: ').strip().lower()
        try:
            if choice == 'q':
                return 0
            if choice == '1':
                ui.markdown((ROOT / m['path'] / 'README.md').read_text())
            elif choice == '2':
                result = check(m)
                if result:
                    r = record(state, m)
                    r['checked_at'], r['checked_digest'] = stamp(), digest(m)
                    save_state(state)
            elif choice == '3':
                quiz(state, m)
            elif choice == '4':
                reveal_hint(state, m)
            elif choice == '5':
                explain(state, m)
            elif choice == '6':
                submit(state, m)
            elif choice == '7':
                review(state)
            elif choice == '8':
                status(state, True)
            elif choice == '9':
                doctor()
            else:
                print('Choose 1–9 or q. Direct commands: ./learn --help')
        except CourseError as exc:
            print(str(exc), file=sys.stderr)


def reveal_hint(state, m):
    r = record(state, m)
    index = min(r.get('hints', 0), len(m['hints'])-1)
    ui.hint(index+1, len(m['hints']), m['hints'][index])
    r['hints'] = index+1
    save_state(state)


def main(argv=None):
    parser = argparse.ArgumentParser(description='Signal Station: interactive local C + FPGA + RF course')
    parser.add_argument('command', nargs='?', default='start', choices=[
        'start', 'map', 'status', 'lesson', 'check', 'quiz', 'hint', 'explain', 'submit',
        'review', 'doctor', 'setup', 'solution', 'benchmark', 'interview', 'notes'])
    parser.add_argument('number', nargs='?', type=int, help='mission 1–36 (default: next unfinished)')
    parser.add_argument('--plain', action='store_true', help='explicitly build C without sanitizers')
    parser.add_argument('--all', action='store_true', help='review practiced cards before they are due')
    parser.add_argument('--limit', type=int, default=10, help='maximum review cards per session')
    parser.add_argument('--color', choices=['auto', 'always', 'never'], default='auto',
                        help='Rich output: auto in terminals, always for previews, never for plain text')
    parser.add_argument('--fpga', action='store_true',
                        help='include native Verilog tools in setup, or require them for doctor')
    args = parser.parse_args(argv)
    ui.configure(args.color)
    try:
        # Tool setup remains usable even if a learner's progress file needs repair.
        if args.command == 'doctor':
            return 0 if doctor(require_hdl=args.fpga) else 1
        if args.command == 'setup':
            return 0 if setup(fpga=args.fpga) else 1
        state = load_state()
        m = mission(args.number) if args.number is not None else current(state)
        if args.command == 'start':
            return menu(state)
        if args.command in ('map', 'status'):
            status(state, args.command == 'map')
        elif args.command == 'lesson':
            ui.markdown((ROOT / m['path'] / 'README.md').read_text())
        elif args.command == 'check':
            passed = check(m, args.plain)
            r = record(state, m)
            if passed:
                r['checked_at'], r['checked_digest'] = stamp(), digest(m)
            else:
                r.pop('checked_digest', None)
            save_state(state)
            return 0 if passed else 1
        elif args.command == 'quiz':
            return 0 if quiz(state, m) else 1
        elif args.command == 'hint':
            reveal_hint(state, m)
        elif args.command == 'explain':
            return 0 if explain(state, m) else 1
        elif args.command == 'submit':
            return 0 if submit(state, m, args.plain) else 1
        elif args.command == 'review':
            if args.limit < 1:
                raise CourseError('--limit must be positive.')
            review(state, args.limit, args.all)
        elif args.command == 'solution':
            show_solution(state, m)
        elif args.command == 'benchmark':
            return 0 if benchmark(m) else 1
        elif args.command == 'interview':
            prompts = [x['explain'] for x in CATALOG]
            for i, prompt in enumerate(random.sample(prompts, 5), 1):
                print(f'{i}. {prompt}\n')
            print('Speak before looking at notes; assess mechanism, example, boundary and tradeoff.')
        elif args.command == 'notes':
            r = state['missions'].get(str(m['id']), {})
            print(r.get('explanation', {}).get('text', 'No explanation saved yet. Use ./learn explain N.'))
        return 0
    except (EOFError, KeyboardInterrupt):
        print('\nSession ended. Previously saved progress is safe.')
        return 0
    except (CourseError, OSError) as exc:
        print(f'Course error: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
