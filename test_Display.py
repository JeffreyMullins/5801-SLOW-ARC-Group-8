# from unittest import TestCase
# from unittest import main
from Display import Display
from Pitch import Pitch
import unittest
import os


class test_display(unittest.TestCase):
    def test_init(self):
        # Test the initialization of all Display object attributes

        test_dislay = Display()
        self.assertEqual(test_dislay.current_result, "")
        
    def test_display(self):
        test_display = Display()
        test_pitch = Pitch()
        
        test_display.display(test_pitch)

        self.assertEqual(test_display.current_result, "")

        test_pitch.pitch_status = "strike"
        test_display.display(test_pitch)

        self.assertEqual(test_display.current_result, "strike")
        
        test_pitch.pitch_status = "ball"
        test_display.display(test_pitch)

        self.assertEqual(test_display.current_result, "ball")

        
    
    def test_display_bad_input(self):
        test_display = Display()
        test_pitch = Pitch()

        test_pitch.pitch_status = "aaaaaaaa"
        test_display.display(test_pitch)
    
        self.assertEqual(test_display.current_result, "")

if __name__=='__main__':
        unittest.main()