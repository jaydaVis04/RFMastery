"""Rich presentation with literal-safe input, a terminal theme, and plain fallbacks."""
import builtins
import importlib
import os
from pathlib import Path
import re
import sys

DEPENDENCIES = Path(__file__).resolve().parents[1] / '.deps'
if DEPENDENCIES.is_dir():
    sys.path.insert(0, str(DEPENDENCIES))

STYLES = {
    'station': 'bold cyan', 'action': 'bold cyan', 'ready': 'bold green',
    'caution': 'yellow', 'fault': 'bold red', 'capture': 'bold magenta',
    'secondary': 'dim', 'body': 'default',
}
MODE = 'auto'
BACKEND = 'plain'
MODULES = {}


def load_backend():
    """Prefer the supported dependency; pip's real Rich is a practical offline fallback."""
    global BACKEND, MODULES
    if DEPENDENCIES.is_dir() and str(DEPENDENCIES) not in sys.path:
        sys.path.insert(0, str(DEPENDENCIES))
    for prefix, label in (('rich', 'installed'), ('pip._vendor.rich', 'pip-bundled')):
        try:
            modules = {name: importlib.import_module(f'{prefix}.{name}') for name in (
                'console', 'panel', 'table', 'text', 'theme', 'syntax', 'progress_bar', 'box')}
        except ImportError:
            continue
        MODULES = modules
        BACKEND = label
        return
    BACKEND, MODULES = 'plain', {}


load_backend()


def configure(mode='auto'):
    global MODE
    MODE = mode


def styled(stream=None):
    stream = stream if stream is not None else sys.stdout
    if BACKEND == 'plain' or MODE == 'never' or 'NO_COLOR' in os.environ:
        return False
    if MODE == 'always':
        return True
    return bool(getattr(stream, 'isatty', lambda: False)()) and os.environ.get('TERM') != 'dumb'


def console(stream=None, record=False, width=None):
    stream = stream if stream is not None else sys.stdout
    kwargs = dict(file=stream, record=record, theme=MODULES['theme'].Theme(STYLES),
                  highlight=False, markup=False, force_terminal=True, color_system='standard')
    if width is not None:
        kwargs['width'] = width
    return MODULES['console'].Console(**kwargs)


def tone(text):
    text = text.strip()
    if text.startswith(('FAIL', 'CHECK FAILED', 'Course error:', 'Pipeline check failed')):
        return 'fault'
    if text.startswith(('CHECK PASSED', 'QUIZ PASSED', 'Correct.', 'PASS', 'Setup complete')) or text.endswith(': OK'):
        return 'ready'
    if text.startswith(('Not yet.', 'MISSING:', 'UNVERIFIED', 'Review the missed', 'Plain build:', 'Assisted practice')) or 'NEEDS SETUP' in text:
        return 'caution'
    if text.startswith(('MISSION ', 'SIGNAL STATION', 'Recall check:', 'FPGA lessons', 'C / RF lessons')):
        return 'station'
    if text.startswith(('Next suggested', 'Suggested next:', '$ ')):
        return 'action'
    return 'body'


def print(*objects, sep=' ', end='\n', file=None, flush=False):
    """A print-compatible renderer. Learner text and compiler output are never markup."""
    stream = file if file is not None else sys.stdout
    text = sep.join(str(x) for x in objects)
    if not styled(stream):
        return builtins.print(text, end=end, file=stream, flush=flush)
    content = MODULES['text'].Text(text, style=tone(text))
    if tone(text) == 'body':
        content.highlight_regex(r'\./learn(?: [a-z]+)?(?: [0-9]+)?', style='action')
        content.highlight_regex(r'\b(?:READY|OK)\b', style='ready')
    console(stream).print(content, end=end, soft_wrap=True)
    if flush:
        stream.flush()


def ask(prompt=''):
    if styled():
        console().print(MODULES['text'].Text(prompt, style='action'), end='')
        return builtins.input()
    return builtins.input(prompt)


def panel(title, body, role='station'):
    if not styled():
        print(f'\n{title}\n{body}')
        return
    Text = MODULES['text'].Text
    console().print(MODULES['panel'].Panel(
        Text(body), title=Text(title, style=role), border_style=role,
        padding=(1, 2), title_align='left'))


def dashboard(flags, total, earned, due, next_label):
    if not styled():
        print(f'\nSIGNAL STATION  /  C · FPGA · RF\n{flags}/{total} current flags · {earned} earned historically · {due} review cards due')
        return
    c = console()
    Text, Table = MODULES['text'].Text, MODULES['table'].Table
    meter = Table.grid(expand=True, padding=(0, 1))
    meter.add_column(ratio=1)
    meter.add_column(justify='right')
    meter.add_row(MODULES['progress_bar'].ProgressBar(total=total, completed=flags,
                  width=None, style='secondary', complete_style='ready', finished_style='capture'),
                  Text(f'{flags:02d} / {total:02d} FLAGS', style='ready'))
    body = MODULES['console'].Group(
        Text('C  /  FPGA  /  RF', style='secondary'), Text(''), meter,
        Text(f'{due} review cards due   ·   {earned} flags earned historically', style='secondary'),
        Text(''), Text('NEXT TARGET', style='station'), Text(next_label, style='bold'),
    )
    c.print(MODULES['panel'].Panel(body, title=Text('SIGNAL STATION', style='station'),
            subtitle=Text('RECEIVER ENGINEERING LAB', style='secondary'),
            border_style='cyan', padding=(1, 2), title_align='left'))


def course_map(rows):
    if not styled():
        print('\n  ID  STATUS       MISSION')
        for number, label, title, track, assisted in rows:
            print(f'  {number:02d}  {label:12} {title}' + (' [assisted]' if assisted else ''))
        return
    c = console()
    Text = MODULES['text'].Text
    table = MODULES['table'].Table(box=MODULES['box'].SIMPLE, padding=(0, 1), expand=True,
                                    header_style='station', border_style='secondary')
    table.add_column('ID', width=2, no_wrap=True)
    table.add_column('STATE', width=11)
    table.add_column('MISSION', ratio=1)
    wide = c.width >= 100
    if wide:
        table.add_column('TRACK', style='secondary', max_width=24)
    for number, label, title, track, assisted in rows:
        role = {'COMPLETE': 'ready', 'CHANGED': 'caution', 'CODE PASSED': 'ready'}.get(label, 'secondary')
        cells = [Text(f'{number:02d}', style='action'), Text(label, style=role),
                 Text(title + (' [assisted]' if assisted else ''))]
        if wide:
            cells.append(Text(track, style='secondary'))
        table.add_row(*cells)
    c.print(table)


def menu():
    actions = [('1', 'Read mission'), ('2', 'Run checks'), ('3', 'Quiz'),
               ('4', 'Hint'), ('5', 'Explain'), ('6', 'Submit for flag'),
               ('7', 'Review'), ('8', 'Course map'), ('9', 'Setup check')]
    if not styled():
        print('\n  1 Read mission       2 Run checks       3 Quiz\n  4 Hint               5 Explain          6 Submit for flag\n  7 Review             8 Course map       9 Setup check\n  q Save and exit')
        return
    c = console()
    Text = MODULES['text'].Text
    table = MODULES['table'].Table.grid(expand=True, padding=(0, 2))
    count = 3 if c.width >= 72 else 1
    for _ in range(count):
        table.add_column(ratio=1)
    for i in range(0, len(actions), count):
        cells = []
        for key, label in actions[i:i+count]:
            text = Text(f'[{key}] ', style='action')
            text.append(label, style='default')
            cells.append(text)
        table.add_row(*cells)
    c.print(table)
    print('\n[q] Save and exit', end='\n\n')


def syntax(code, language='c'):
    if not styled():
        print(code)
        return
    if BACKEND == 'installed':
        console().print(MODULES['syntax'].Syntax(code, language or 'text', theme='ansi_dark',
                        background_color='default', line_numbers=True, word_wrap=True, padding=(1, 1)))
        return
    # pip also trims Pygments' C/Verilog lexers. Render literal source with Rich
    # Text spans offline; the normal dependency uses full Pygments highlighting.
    Text = MODULES['text'].Text
    table = MODULES['table'].Table.grid(padding=(0, 1), expand=True)
    table.add_column(width=4, justify='right', style='secondary')
    table.add_column(ratio=1)
    keywords = ('int void char long short unsigned signed const static return if else for while '
                'struct enum union typedef sizeof switch case break continue include define '
                'uint8_t uint16_t uint32_t int16_t int32_t int64_t size_t '
                'module endmodule wire reg input output assign always begin end posedge '
                'def class import from as try except raise with lambda True False None NULL')
    tokens = re.compile(r'(?P<comment>//[^\n]*|/\*.*?\*/)|'
                        r'(?P<string>"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')|'
                        r'(?P<keyword>\b(?:'+'|'.join(keywords.split())+r')\b)|'
                        r'(?P<number>\b(?:0x[0-9a-fA-F]+|\d+(?:\.\d+)?)\b)')
    styles = {'comment':'secondary', 'string':'green', 'keyword':'bold cyan', 'number':'magenta'}
    for number,line in enumerate(code.splitlines(),1):
        text = Text(line, tab_size=4)
        for match in tokens.finditer(line):
            text.stylize(styles[match.lastgroup], match.start(), match.end())
        table.add_row(str(number),text)
    console().print(table)


def _inline(line):
    Text = MODULES['text'].Text
    text = Text()
    for part in re.split(r'(`[^`]+`|\*\*[^*]+\*\*)', line):
        if part.startswith('`'):
            text.append(part[1:-1],style='action')
        elif part.startswith('**'):
            text.append(part[2:-2],style='bold')
        else:
            text.append(part)
    return text


def markdown(source):
    if not styled():
        print(source)
        return
    # The complete supported Rich install includes Markdown. pip strips that module,
    # so its offline fallback still uses actual Rich Syntax / Text / rules for lessons.
    if BACKEND == 'installed':
        Markdown = importlib.import_module('rich.markdown').Markdown
        console().print(Markdown(source, code_theme='ansi_dark', hyperlinks=False))
        return
    code, language, in_code = [], '', False
    c = console()
    for line in source.splitlines():
        if line.startswith('```'):
            if in_code:
                syntax('\n'.join(code), language)
                code = []
            else:
                language = line[3:].strip()
            in_code = not in_code
        elif in_code:
            code.append(line)
        elif line.startswith('#'):
            c.rule(MODULES['text'].Text(line.lstrip('# ').strip(), style='station'), style='secondary', align='left')
        else:
            c.print(_inline(line), soft_wrap=False)
    if code:
        syntax('\n'.join(code), language)


def hint(index, total, body):
    if not styled():
        print(f'Hint {index}/{total}: {body}')
    else:
        panel(f'HINT {index} / {total}', body, 'caution')


def flag(value):
    if not styled():
        print(f'\nFLAG EARNED: {value}')
    else:
        panel('FLAG EARNED', value, 'capture')
