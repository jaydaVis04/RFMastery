import importlib.util,sys,unittest,csv,tempfile
from pathlib import Path
spec=importlib.util.spec_from_file_location('learner',sys.argv.pop(1));lab=importlib.util.module_from_spec(spec);spec.loader.exec_module(lab)
class Mock:
    def __init__(self,values):self.values=iter(values);self.calls=0
    def query(self,cmd):
        assert cmd=='MEAS:POW?';self.calls+=1;v=next(self.values)
        if isinstance(v,Exception):raise v
        return v
class Tests(unittest.TestCase):
    def test_retries(self):
        m=Mock([TimeoutError(),'bad','NaN','-32'])
        self.assertEqual(lab.measure(m,4,-33,-31),{'power_dbm':-32.,'pass':True,'attempts':4})
        self.assertEqual(m.calls,4)
        m=Mock(['-20','-32']);self.assertFalse(lab.measure(m,2,-33,-31)['pass']);self.assertEqual(m.calls,1)
        m=Mock([TimeoutError(),'-32'])
        with self.assertRaises(RuntimeError):lab.measure(m,1,-33,-31)
        self.assertEqual(m.calls,1)
        for v in ['-33','-31']:self.assertTrue(lab.measure(Mock([v]),1,-33,-31)['pass'])
        m=Mock([])
        for args in [(0,-33,-31),(True,-33,-31),(1,-31,-33),(1,float('nan'),0)]:
            with self.assertRaises(ValueError):lab.measure(m,*args)
        self.assertEqual(m.calls,0)
        with self.assertRaises(OSError):lab.measure(Mock([OSError('device gone')]),3,-33,-31)
    def test_csv(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'log.csv';lab.save_csv(p,[{'power_dbm':-32,'pass':True,'attempts':1}])
            with p.open(newline='') as f:
                reader=csv.DictReader(f);self.assertEqual(reader.fieldnames,['power_dbm','pass','attempts']);rows=list(reader)
            self.assertEqual(len(rows),1);self.assertEqual(float(rows[0]['power_dbm']),-32)
unittest.main()
