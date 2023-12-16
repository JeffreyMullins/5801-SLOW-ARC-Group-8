# from unittest import TestCase
# from unittest import main
from Pitch import Pitch
import unittest


class test_pitch(unittest.TestCase):
    def test_init(self):
        test_pitch = Pitch()
        self.assertEqual(test_pitch.speed, -1)
        self.assertEqual(test_pitch.position, [])
        self.assertEqual(test_pitch.current_count, [])
        self.assertEqual(test_pitch.pitch_status, "")
        self.assertEqual(test_pitch.time_thrown, "")
        self.assertEqual(test_pitch.pitcher, None)
        self.assertEqual(test_pitch.umpire, None)
        
    def test_compute_pitch_status(self):
        # not done
        test_pitcher = Pitch()
        
        



if __name__=='__main__':
        unittest.main()

