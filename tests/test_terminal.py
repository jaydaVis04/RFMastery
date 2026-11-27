"""Presentation regressions: literal safety, narrow output and quiet pipelines."""
import io
import os
from pathlib import Path
import re
import subprocess
import sys
import unittest
from unittest.mock import patch

from course import terminal as ui

ANSI = re.compile(r'\x1b\[[0-9;]*[mK]')


class TerminalTests(unittest.TestCase):
    def setUp(self):
        self.old_mode = ui.MODE
        self.environ = patch.dict(os.environ)
        self.environ.start()
        os.environ.pop('NO_COLOR', None)

    def tearDown(self):
        ui.configure(self.old_mode)
        self.environ.stop()

    def test_redirected_output_is_plain_by_default(self):
        ui.configure('auto')
        out = io.StringIO()
        ui.print('CHECK PASSED', file=out)
        self.assertEqual(out.getvalue(), 'CHECK PASSED\n')

    def test_no_color_is_respected_even_when_forced(self):
        os.environ['NO_COLOR']='1'
        ui.configure('always')
        out=io.StringIO()
        ui.print('CHECK FAILED',file=out)
        self.assertNotIn('\x1b',out.getvalue())

    def test_never_mode_is_plain(self):
        ui.configure('never')
        out=io.StringIO()
        ui.print('SIGNAL STATION',file=out)
        self.assertEqual(out.getvalue(),'SIGNAL STATION\n')

    @unittest.skipIf(ui.BACKEND=='plain','Rich is optional for basic course logic')
    def test_rich_emits_color_and_does_not_interpret_learner_markup(self):
        ui.configure('always')
        out=io.StringIO()
        ui.print('Correct. [red]literal user text[/red]',file=out)
        self.assertIn('\x1b[',out.getvalue())
        self.assertEqual(ANSI.sub('',out.getvalue()),'Correct. [red]literal user text[/red]\n')

    @unittest.skipIf(ui.BACKEND=='plain','Rich is optional for basic course logic')
    def test_narrow_dashboard_and_menu_fit_without_losing_actions(self):
        ui.configure('always')
        out=io.StringIO()
        c=ui.console(out,width=48)
        with patch.object(ui,'console',return_value=c):
            ui.dashboard(0,36,0,0,'01 · Bring the receiver console online')
            ui.menu()
        visible=ANSI.sub('',out.getvalue())
        self.assertIn('NEXT TARGET',visible)
        for i in range(1,10):self.assertIn(f'[{i}]',visible)
        self.assertIn('Submit for flag',visible)
        self.assertTrue(all(len(line)<=48 for line in visible.splitlines()))

    @unittest.skipIf(ui.BACKEND=='plain','Rich is optional for basic course logic')
    def test_lessons_highlight_source_without_changing_content(self):
        ui.configure('always')
        out=io.StringIO()
        c=ui.console(out,width=80)
        with patch.object(ui,'console',return_value=c):
            ui.markdown('# Memory\n\n```c\nint *p = NULL;\n```\n')
        visible=ANSI.sub('',out.getvalue())
        self.assertIn('Memory',visible)
        self.assertIn('int *p = NULL;',visible)
        self.assertIn('\x1b[',out.getvalue())

    def test_missing_rich_keeps_basic_output_usable(self):
        ui.configure('always')
        out=io.StringIO()
        with patch.object(ui,'BACKEND','plain'):
            ui.print('CHECK PASSED',file=out)
        self.assertEqual(out.getvalue(),'CHECK PASSED\n')

    @unittest.skipIf(ui.BACKEND=='plain','Rich is optional for basic course logic')
    def test_cli_color_flag_and_plain_flag(self):
        root=Path(__file__).resolve().parents[1]
        for mode,colored in [('always',True),('never',False)]:
            result=subprocess.run([sys.executable,'learn','map','--color',mode],cwd=root,
                                  env=os.environ.copy(),capture_output=True,text=True,timeout=15)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual('\x1b[' in result.stdout,colored)
            self.assertIn('SIGNAL STATION',ANSI.sub('',result.stdout))


if __name__=='__main__':
    unittest.main()
