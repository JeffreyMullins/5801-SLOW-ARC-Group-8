# from unittest import TestCase
# from unittest import main
from Umpire import Umpire
import unittest
import os
import threading
import time
import config


class test_umpire(unittest.TestCase):
    def test_init(self):
        # test to make sure the initialization works correctly for Umpire object
        test_umpire = Umpire()
        self.assertEqual(test_umpire.permissions, False)
        self.assertEqual(test_umpire.decision, False)
        self.assertEqual(test_umpire.umpire_input, "")

    def test_terminal_input_strike(self):
        # when run enter "strike" into the terminal for this test to work

        test_umpire = Umpire()
        
        test_umpire.get_terminal_input()
        self.assertEqual(test_umpire.umpire_input, "strike")

    # def test_terminal_input_ball(self):
    #     # when run enter "ball" into the terminal
    #     test_umpire = Umpire()

    #     test_umpire.get_terminal_input()
    #     monkeypatch.setattr('builtins.input', lambda _: "strike")

    #     self.assertEqual(test_umpire.umpire_input, "ball")

    # def test_terminal_input_blank(self):
    #     # when run enter "" into the terminal
    #     test_umpire = Umpire()

    #     test_umpire.get_terminal_input()
    #     self.assertEqual(test_umpire.umpire_input, "")

    # def test_terminal_input_bad(self):
    #     # when run enter any number into the terminal
    #     test_umpire = Umpire()

    #     test_umpire.get_terminal_input()
    #     self.assertEqual(test_umpire.umpire_input, "")



if __name__=='__main__':
        unittest.main()
    

