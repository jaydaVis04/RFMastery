#!/usr/bin/env python3
"""Create deterministic little-endian signed-int16 I/Q; no NumPy or radio required."""
import argparse
import math
from pathlib import Path
import random
import struct


def generate(path, count=4096, rate=48000., tone=2000., amplitude=12000, mode='tone', seed=17):
    if count < 0 or not math.isfinite(rate) or rate <= 0 or not math.isfinite(tone) or not 0 <= amplitude <= 32767:
        raise ValueError('invalid signal parameters')
    rng = random.Random(seed)
    with Path(path).open('wb') as f:
        for n in range(count):
            if mode == 'tone':
                angle = 2*math.pi*tone*n/rate
                i, q = round(amplitude*math.cos(angle)), round(amplitude*math.sin(angle))
            elif mode == 'impulse':
                i, q = (amplitude, -amplitude) if n == 0 else (0, 0)
            elif mode == 'random':
                i, q = rng.randint(-amplitude, amplitude), rng.randint(-amplitude, amplitude)
            elif mode == 'zeros':
                i = q = 0
            elif mode == 'extrema':
                i, q = (32767, -32768) if n % 2 == 0 else (-32768, 32767)
            else:
                raise ValueError(f'unknown mode {mode}')
            f.write(struct.pack('<hh', i, q))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('output', type=Path)
    p.add_argument('--count', type=int, default=4096)
    p.add_argument('--rate', type=float, default=48000)
    p.add_argument('--tone', type=float, default=2000)
    p.add_argument('--amplitude', type=int, default=12000)
    p.add_argument('--mode', choices=['tone', 'impulse', 'random', 'zeros', 'extrema'], default='tone')
    p.add_argument('--seed', type=int, default=17)
    a = p.parse_args()
    try:
        generate(a.output, a.count, a.rate, a.tone, a.amplitude, a.mode, a.seed)
        print(f'Wrote {a.count} complex samples / {a.count*4} bytes to {a.output}')
        print(f'Format: little-endian signed-int16 I,Q; rate={a.rate:g} samples/s; amplitude units=raw counts')
    except (ValueError, OSError) as exc:
        p.error(str(exc))
