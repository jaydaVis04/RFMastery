"""Meaningful regression checks for state, gating, quiz/review and non-spoiling validation."""
from datetime import timedelta
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from course import engine as e


class CourseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.state_patch = patch.object(e, 'STATE', Path(self.temp.name)/'state.json')
        self.state_patch.start()
        self.stdout = patch('sys.stdout', new_callable=io.StringIO)
        self.stdout.start()

    def tearDown(self):
        self.stdout.stop()
        self.state_patch.stop()
        self.temp.cleanup()

    def test_catalog_has_all_contracts_and_files(self):
        self.assertEqual([x['id'] for x in e.CATALOG], list(range(1, 37)))
        for m in e.CATALOG:
            self.assertEqual(len(m['quiz']), 3)
            for question in m['quiz']:
                self.assertEqual(len(set([question['answer']]+question['distractors'])), 3)
            for name in m['files']:
                self.assertTrue((e.ROOT/m['path']/name).is_file(), f'{m["id"]} {name}')
            self.assertTrue((e.ROOT/m['path']/'README.md').is_file())

    def test_progress_roundtrip_and_corruption_preserved(self):
        state = e.load_state()
        state['missions']['1'] = {'explanation': {'text': 'my notes'}}
        e.save_state(state)
        self.assertEqual(e.load_state(), state)
        e.STATE.write_text('{broken')
        with self.assertRaises(e.CourseError):
            e.load_state()
        self.assertEqual(e.STATE.read_text(), '{broken')

    def test_flag_needs_all_gates_and_rechecks(self):
        state = e.load_state()
        m = e.mission(1)
        with patch.object(e, 'check', return_value=True) as checker:
            self.assertFalse(e.submit(state, m))
            r = e.record(state, m)
            self.assertNotIn('flag', r)
            r['quiz_at'] = e.stamp()
            r['explanation'] = {'self_assessed': True}
            self.assertTrue(e.submit(state, m))
            self.assertTrue(r['flag'].startswith('SIGNAL{01_'))
            self.assertEqual(checker.call_count, 2)
        with patch.object(e, 'digest', return_value='changed'):
            self.assertEqual(e.current(state)['id'], 1)

    def test_failed_checks_never_award_flag(self):
        state=e.load_state(); m=e.mission(1)
        e.record(state,m).update({'quiz_at':e.stamp(),'explanation':{'self_assessed':True}})
        with patch.object(e,'check',return_value=False):
            self.assertFalse(e.submit(state,m))
        self.assertNotIn('flag',e.record(state,m))

    def test_final_requires_all_current_prior_flags(self):
        state=e.load_state()
        with patch.object(e,'check') as checker:
            self.assertFalse(e.submit(state,e.mission(36)))
            checker.assert_not_called()

    def test_capstone_requires_engineering_record(self):
        state=e.load_state();m=e.mission(34)
        e.record(state,m).update({'quiz_at':e.stamp(),'explanation':{'self_assessed':True}})
        with patch.object(e,'check',return_value=True):
            self.assertFalse(e.submit(state,m))
        self.assertNotIn('flag',e.record(state,m))

    def test_missed_review_returns_soon_and_correct_is_spaced(self):
        state=e.load_state();m=e.mission(8)
        e.remember(state,m,0,False)
        card=state['cards']['8:0']
        self.assertEqual(card['misses'],1)
        due=e.datetime.fromisoformat(card['due'])
        self.assertLess(due-e.now(),timedelta(minutes=11))
        e.remember(state,m,0,True)
        self.assertEqual(card['stage'],1)
        self.assertGreater(e.datetime.fromisoformat(card['due'])-e.now(),timedelta(hours=23))

    def test_quiz_requires_correct_session_and_tracks_misses(self):
        state=e.load_state();m=e.mission(1)
        with patch.object(e.random,'shuffle',lambda x:None),patch('builtins.input',side_effect=['1','2','1']):
            self.assertFalse(e.quiz(state,m))
        self.assertNotIn('quiz_at',e.record(state,m))
        self.assertEqual(state['cards']['1:1']['misses'],1)
        with patch.object(e.random,'shuffle',lambda x:None),patch('builtins.input',side_effect=['1','1','1']):
            self.assertTrue(e.quiz(state,m))
        self.assertIn('quiz_at',e.record(state,m))

    def test_explanation_is_explicit_self_assessment(self):
        state=e.load_state();m=e.mission(1)
        text=' '.join(['reasoning']*35)
        with patch('builtins.input',side_effect=[text,'.','n']):
            self.assertFalse(e.explain(state,m))
        self.assertFalse(e.record(state,m)['explanation']['self_assessed'])
        self.assertEqual(e.record(state,m)['explanation']['text'],text)

    def test_solution_does_not_change_learner_files(self):
        state=e.load_state();m=e.mission(1)
        before=e.digest(m)
        e.show_solution(state,m)
        self.assertEqual(e.digest(m),before)
        self.assertIn('assisted',e.record(state,m))

    def test_missing_hdl_never_passes(self):
        with patch.object(e.shutil,'which',return_value=None):
            with self.assertRaises(e.CourseError):
                e.check(e.mission(18),quiet=True)


if __name__ == '__main__':
    unittest.main()
