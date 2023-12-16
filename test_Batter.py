# from unittest import TestCase
# from unittest import main
from Batter import Batter
import unittest


class test_Batter(unittest.TestCase):
    def test_init(self):
        test_batter = Batter()
        self.assertEqual(test_batter.strike_zone, -1)
        self.assertEqual(test_batter.shoulder1, [])
        self.assertEqual(test_batter.shoulder2, [])
        self.assertEqual(test_batter.knee1, "")
        self.assertEqual(test_batter.knee2, "")
        
        

if __name__=='__main__':
        unittest.main()

