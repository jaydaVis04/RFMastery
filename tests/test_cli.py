"""A real CLI/compile/quiz/flag journey in an isolated disposable course copy."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from course.engine import ROOT


class EndToEndTests(unittest.TestCase):
    def test_first_mission_complete_without_touching_real_progress(self):
        with tempfile.TemporaryDirectory(prefix='signal-e2e-') as d:
            root=Path(d)/'course'
            shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.build','.progress','.deps','__pycache__'))
            env=os.environ.copy()
            env['SIGNAL_STATION_STATE']=str(root/'.progress/state.json')
            def run(args,input=None):
                return subprocess.run([sys.executable,*args],cwd=root,env=env,input=input,
                                      text=True,capture_output=True,timeout=30)
            failed=run(['learn','check','1'])
            self.assertEqual(failed.returncode,1,failed.stderr)
            shutil.copy(root/'course/solutions/01/lab.c',root/'lessons/01_boot/lab.c')
            checked=run(['learn','check','1'])
            self.assertEqual(checked.returncode,0,checked.stderr)
            # Shuffle deterministically only inside this test subprocess.
            quiz=run(['-c', 'from course import engine as e; e.random.shuffle=lambda x:None; raise SystemExit(e.main(["quiz","1"]))'], '1\n1\n1\n')
            self.assertEqual(quiz.returncode,0,quiz.stderr)
            explanation=('The preprocessor expands includes, the compiler translates C, the assembler creates objects, '
                         'and the linker resolves external definitions. An unknown variable fails compilation, while '
                         'a declared function with no linked definition fails linking. A successful program returns zero.')
            explained=run(['learn','explain','1'],explanation+'\n.\ny\n')
            self.assertEqual(explained.returncode,0,explained.stderr)
            submitted=run(['learn','submit','1'])
            self.assertEqual(submitted.returncode,0,submitted.stderr)
            self.assertIn('FLAG EARNED: SIGNAL{01_',submitted.stdout)
            state=json.loads((root/'.progress/state.json').read_text())
            self.assertEqual(set(state['missions']),{'1'})
            menu=run(['learn'],'q\n')
            self.assertEqual(menu.returncode,0,menu.stderr)
            self.assertIn('02 · Name the telemetry',menu.stdout)
            (root/'lessons/01_boot/lab.c').write_text('int main(void){return 1;}\n')
            changed=run(['learn','map'])
            self.assertIn('CHANGED',changed.stdout)
            self.assertEqual(run(['learn','submit','1']).returncode,1)


if __name__=='__main__':
    unittest.main()
