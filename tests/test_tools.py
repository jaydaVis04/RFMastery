import math
from pathlib import Path
import struct
import tempfile
import unittest

from course.check_pipeline import oracle
from tools.generate_iq import generate
from tools.signal_lab import spectrum


class SignalToolsTests(unittest.TestCase):
    def test_impulse_binary_format_and_negative_truncation(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'impulse.iq'
            generate(path,4,mode='impulse',amplitude=32767)
            pairs=list(struct.iter_unpack('<hh',path.read_bytes()))
            self.assertEqual(pairs,[(32767,-32767),(0,0),(0,0),(0,0)])
            self.assertEqual(list(struct.iter_unpack('<hh',oracle(pairs))),
                             [(8191,-8191),(16383,-16383),(8191,-8191),(0,0)])

    def test_negative_frequency_axis_and_unit_amplitude(self):
        rows=spectrum(-1000,8000,64,'rect')
        peak=max(rows,key=lambda row:row[1])
        self.assertEqual(peak[0],-1000)
        self.assertAlmostEqual(peak[1],0,places=9)
        for frequency,db in rows:
            if frequency!=-1000:self.assertLess(db,-180)

    def test_sandbox_rejects_invalid_ranges(self):
        for args in [(1,0,64,'rect'),(1,1000,0,'hann'),(math.nan,1000,64,'rect')]:
            with self.assertRaises(ValueError):spectrum(*args)


if __name__=='__main__':
    unittest.main()
