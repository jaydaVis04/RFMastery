#!/usr/bin/env python3
"""A standard-library signal sandbox: predict, change parameters, inspect the result."""
import argparse
import cmath
import csv
import math
from pathlib import Path


def spectrum(tone, rate, count, window):
    if not all(math.isfinite(x) for x in (tone, rate)) or rate <= 0 or not 8 <= count <= 1024:
        raise ValueError('use finite tone/rate, rate>0, and 8<=count<=1024')
    weights = [0.5-0.5*math.cos(2*math.pi*n/(count-1)) if window == 'hann' else 1. for n in range(count)]
    x = [cmath.exp(2j*math.pi*tone*n/rate)*weights[n] for n in range(count)]
    gain = sum(weights)
    rows = []
    # A direct DFT makes the calculation inspectable. It is intentionally not a fast FFT.
    for signed_bin in range(-(count//2), count-count//2):
        value = sum(sample*cmath.exp(-2j*math.pi*signed_bin*n/count) for n, sample in enumerate(x)) / gain
        rows.append((signed_bin*rate/count, 20*math.log10(max(abs(value), 1e-12))))
    return rows


def display_spectrum(tone, rate, count, window, output=None):
    rows = spectrum(tone, rate, count, window)
    peak = max(rows, key=lambda r:r[1])
    print(f'\nComplex tone={tone:g} Hz; fs={rate:g} samples/s; N={count}; window={window}')
    print(f'Bin spacing={rate/count:.6g} Hz; largest bin={peak[0]:.6g} Hz at {peak[1]:.3f} dB relative to unit complex-tone amplitude.')
    print('Coherent-gain normalized amplitude; not PSD, calibrated dBm, or measured hardware data.')
    print('Strongest bins:')
    for hz, db in sorted(rows, key=lambda r:r[1], reverse=True)[:12]:
        bar = '#' * max(0, int((max(-80., db)+80)/2))
        print(f'{hz:12.3f} Hz {db:8.2f} dB |{bar}')
    if output:
        output = Path(output)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open('w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['frequency_hz', 'amplitude_db_relative_unit_complex_tone'])
            w.writerows(rows)
        print(f'Full spectrum saved to {output}')
    print('Try a bin-centered tone, then move it half a bin. Compare rectangular and Hann windows.')


def alias_demo(tone, rate):
    if not math.isfinite(tone) or not math.isfinite(rate) or rate <= 0:
        raise ValueError('finite tone/rate and positive rate required')
    folded = abs(tone) % rate
    folded = min(folded, rate-folded)
    print(f'\nReal cosine {tone:g} Hz at {rate:g} samples/s aliases to {folded:g} Hz.')
    print(' n      original cosine      folded cosine')
    for n in range(12):
        print(f'{n:2} {math.cos(2*math.pi*tone*n/rate):20.8f} {math.cos(2*math.pi*folded*n/rate):20.8f}')
    print('This folding is for real cosines. Complex baseband retains frequency sign.')


def constellation():
    print('\nQPSK mapping (unit symbol energy; no pulse shaping/noise):')
    for a in range(2):
        for b in range(2):
            z = complex(1-2*a, 1-2*b)/math.sqrt(2)
            print(f'{a}{b}: I={z.real:+.6f}, Q={z.imag:+.6f}, phase={math.degrees(cmath.phase(z)):+.1f}°')
    print('Question: what changes if the channel rotates every symbol by 30 degrees?')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode', choices=['spectrum','alias','qpsk'])
    p.add_argument('--tone', type=float, default=1003)
    p.add_argument('--rate', type=float, default=8000)
    p.add_argument('--count', type=int, default=256)
    p.add_argument('--window', choices=['rect','hann'], default='rect')
    p.add_argument('--output', type=Path, help='optional full-spectrum CSV')
    a = p.parse_args()
    try:
        if a.mode == 'spectrum':
            display_spectrum(a.tone,a.rate,a.count,a.window,a.output)
        elif a.mode == 'alias':
            alias_demo(a.tone,a.rate)
        elif a.mode == 'qpsk':
            constellation()
        else:
            while True:
                print('\nSIGNAL SANDBOX\n1 Real aliasing\n2 Complex spectrum / leakage\n3 QPSK\nq Exit')
                choice=input('Choose: ').strip().lower()
                if choice == 'q':return 0
                if choice in ('1','2'):
                    tone=float(input('Tone frequency Hz: '));rate=float(input('Sample rate samples/s: '))
                    input('Predict the alias or peak bin aloud, then press Enter: ')
                    if choice == '1':alias_demo(tone,rate)
                    else:
                        count=int(input('DFT size 8..1024: '))
                        window=input('Window rect/hann [rect]: ').strip() or 'rect'
                        if window not in ('rect','hann'):raise ValueError('window must be rect or hann')
                        display_spectrum(tone,rate,count,window)
                elif choice == '3':constellation()
        return 0
    except (EOFError,KeyboardInterrupt):
        print('\nSandbox closed.')
        return 0
    except (ValueError,OSError) as exc:
        p.error(str(exc))


if __name__ == '__main__':
    raise SystemExit(main())
