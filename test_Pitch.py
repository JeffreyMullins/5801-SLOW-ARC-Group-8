# from unittest import TestCase
# from unittest import main
from Pitch import Pitch
from Camera import Camera
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
        
    
    def test_set_pitch_status(self):
        # Tests to make sure that the new status of a pitch is correctly updated
        test_pitch = Pitch()
        
        test_pitch.set_pitch_status(new_status="strike")
        self.assertEqual(test_pitch.pitch_status, "strike")
        
        test_pitch.set_pitch_status(new_status="00000")
        self.assertEqual(test_pitch.pitch_status, "00000")



        
        



if __name__=='__main__':
        unittest.main()

