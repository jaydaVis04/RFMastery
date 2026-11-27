#!/usr/bin/env python3
"""Compare a pipeline result to the independent three-tap Python reference."""
import argparse
from pathlib import Path
import struct
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from course.check_pipeline import oracle


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input', type=Path)
    p.add_argument('filtered', type=Path)
    a = p.parse_args()
    raw = a.input.read_bytes()
    actual = a.filtered.read_bytes()
    if len(raw) % 4 or len(actual) % 4:
        p.error('input/output contains a partial I/Q record')
    expected = oracle(list(struct.iter_unpack('<hh', raw)))
    if actual != expected:
        for i in range(max(len(actual), len(expected))//4):
            got = actual[4*i:4*i+4]
            want = expected[4*i:4*i+4]
            if got != want:
                print(f'FAIL sample {i}: actual={got.hex()} expected={want.hex()}')
                return 1
    print(f'PASS: {len(raw)//4} samples agree exactly, including negative truncation and zero initial history')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
