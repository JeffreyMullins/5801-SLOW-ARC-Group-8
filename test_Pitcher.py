# from unittest import TestCase
# from unittest import main
from Pitcher import Pitcher
import unittest


class test_pitcher(unittest.TestCase):
    def test_init(self):
        test_pitcher = Pitcher()
        self.assertEqual(test_pitcher.state, False)
        self.assertEqual(test_pitcher.pitches_list, [])
        self.assertEqual(test_pitcher.num_pitches, 1)
        self.assertEqual(test_pitcher.umpire, None)
        self.assertEqual(test_pitcher.camera, None)
        self.assertEqual(test_pitcher.display, None)
        


if __name__=='__main__':
        unittest.main()

