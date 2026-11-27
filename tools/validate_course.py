#!/usr/bin/env python3
"""Validate fixtures without replacing any learner source or earning any flags."""
import argparse
import contextlib
import io
from pathlib import Path
import shutil
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from course.engine import CATALOG, ROOT, CourseError, check, golden_vectors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--starters', action='store_true', help='verify unfinished shipped starters fail')
    parser.add_argument('--require-hdl', action='store_true', help='treat missing HDL simulator as a failure')
    parser.add_argument('--mission', type=int, help='validate one mission')
    args = parser.parse_args()
    failed, skipped, passed = [], [], []
    for m in CATALOG:
        if args.mission and m['id'] != args.mission:
            continue
        if m['kind'] == 'design':
            print(f'{m["id"]:02d} RUBRIC — prose requires self/human assessment')
            continue
        if m['kind'] == 'hdl' and (not shutil.which('iverilog') or not shutil.which('vvp')):
            skipped.append(m['id'])
            print(f'{m["id"]:02d} UNVERIFIED — Icarus Verilog is unavailable')
            continue
        source = ROOT / m['path'] if args.starters else ROOT / 'course/solutions' / f'{m["id"]:02d}'
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                result = check(m, source_dir=source, quiet=True)
            good = (not result) if args.starters else result
        except CourseError as exc:
            good = False
            output.write(str(exc))
        if good:
            passed.append(m['id'])
            print(f'{m["id"]:02d} PASS — ' + ('unfinished starter rejected' if args.starters else 'reference passes'))
        else:
            failed.append(m['id'])
            print(f'{m["id"]:02d} FAILED\n{output.getvalue()[-10000:]}')
    if not args.starters:
        build = ROOT / '.build/golden-validation'
        build.mkdir(parents=True, exist_ok=True)
        if not golden_vectors(build, quiet=True):
            failed.append('C golden')
    print(f'\n{len(passed)} passed; {len(skipped)} HDL checks unverified; {len(failed)} failed. Learner files/progress unchanged.')
    return 1 if failed or (args.require_hdl and skipped) else 0


if __name__ == '__main__':
    raise SystemExit(main())
