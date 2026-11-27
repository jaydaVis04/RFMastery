"""Independent binary and CLI integration tests; no third-party dependencies."""
import json
from pathlib import Path
import random
import struct
import subprocess
import sys
import tempfile


def oracle(samples):
    z = [[0, 0], [0, 0]]
    result = []
    for pair in samples:
        output = []
        for channel, x in enumerate(pair):
            acc = 8192*x + 16384*z[channel][0] + 8192*z[channel][1]
            y = (abs(acc)//32768) * (-1 if acc < 0 else 1)
            output.append(max(-32768, min(32767, y)))
            z[channel] = [x, z[channel][0]]
        result.append(tuple(output))
    return b''.join(struct.pack('<hh', *s) for s in result)


def verify(binary):
    rng = random.Random(47321)
    cases = [[], [(32767, -32768)], [(0, 0)]*20,
             [(32767, -32768), (0, 0), (0, 0), (0, 0)],
             [(10000, -12000)]*99, [(32767, -32768), (-32768, 32767)]*43,
             [(rng.randint(-32768, 32767), rng.randint(-32768, 32767)) for _ in range(5003)]]
    with tempfile.TemporaryDirectory(prefix='signal-pipeline-') as d:
        d = Path(d)
        source, output = d/'input.iq', d/'output.iq'
        for index, samples in enumerate(cases):
            source.write_bytes(b''.join(struct.pack('<hh', *x) for x in samples))
            output.unlink(missing_ok=True)
            run = subprocess.run([binary, source, output], capture_output=True, text=True, timeout=20)
            assert run.returncode == 0, f'case {index}: {run.stderr}'
            assert output.exists(), f'case {index}: output file missing'
            assert output.read_bytes() == oracle(samples), f'case {index}: binary FIR mismatch'
            info = json.loads(run.stdout)
            assert set(info) == {'samples', 'mean_power'}, 'stdout must contain specified JSON keys only'
            assert info['samples'] == len(samples), 'wrong sample count'
            want = sum(i*i+q*q for i, q in samples)/len(samples) if samples else 0
            assert abs(info['mean_power']-want) <= 1e-7*max(1, want), 'wrong mean power / units'
        for suffix in (b'\x00', b'\x00\x01', b'\x00\x01\x02'):
            source.write_bytes(struct.pack('<hh', 10, -20)+suffix)
            run = subprocess.run([binary, source, output], capture_output=True, text=True, timeout=20)
            assert run.returncode != 0, 'truncated sample accepted'
        source.write_bytes(b'unchanged')
        run = subprocess.run([binary, source, source], capture_output=True, text=True, timeout=20)
        assert run.returncode != 0 and source.read_bytes() == b'unchanged', 'identical path must be rejected before opening output'
        for args in ([], [str(source)], [str(d/'missing'), str(output)], [str(source), str(d/'missingdir/out')]):
            run = subprocess.run([binary, *args], capture_output=True, text=True, timeout=20)
            assert run.returncode != 0, f'error path accepted: {args}'
    print('PASS: seven signal cases, module-independent oracle, power, malformed lengths, paths and CLI errors')


if __name__ == '__main__':
    try:
        verify(str(Path(sys.argv[1]).resolve()))
    except (AssertionError, ValueError, OSError, subprocess.TimeoutExpired) as exc:
        print(f'Pipeline check failed: {exc}', file=sys.stderr)
        raise SystemExit(1)
