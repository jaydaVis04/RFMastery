import importlib.util, sys, unittest
spec=importlib.util.spec_from_file_location('learner',sys.argv.pop(1));lab=importlib.util.module_from_spec(spec);spec.loader.exec_module(lab)
class Tests(unittest.TestCase):
    def test_units(self):
        self.assertEqual(lab.payload_bps(5e6,4),80e6)
        self.assertEqual(lab.payload_bps(10,2,8),160)
        self.assertAlmostEqual(lab.block_ms(4096,1e6),4.096)
        self.assertEqual(lab.block_ms(0,1),0)
        for args in [(0,1),(1,0),(-1,2),(float('nan'),1)]:
            with self.assertRaises(ValueError):lab.payload_bps(*args)
        with self.assertRaises(ValueError):lab.block_ms(2,0)
        with self.assertRaises(ValueError):lab.block_ms(-1,2)
    def test_gaps(self):
        self.assertEqual(lab.missing_blocks([]),0)
        self.assertEqual(lab.missing_blocks([5]),0)
        self.assertEqual(lab.missing_blocks([0,1,4,5]),2)
        self.assertEqual(lab.missing_blocks([7,11,20]),11)
        for seq in [[1,1],[3,2],[-1,0],[1,2.5]]:
            with self.assertRaises(ValueError):lab.missing_blocks(seq)
unittest.main()
