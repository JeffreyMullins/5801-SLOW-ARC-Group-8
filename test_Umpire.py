# from unittest import TestCase
# from unittest import main
from Umpire import Umpire
import unittest
import os
import threading
import time
import config


class test_Umpire(unittest.TestCase):
    def test_init(self):
        test_umpire = Umpire()
        self.assertEqual(test_umpire.permissions, False)
        self.assertEqual(test_umpire.decision, False)
        self.assertEqual(test_umpire.umpire_input, "")

        
    def test_terminal_input(self):
        # not done
        test_umpire = Umpire()

        test_umpire.get_terminal_input()
        
        self.assertEqual(test_impire.umpire_input, "ENTER NEW PITCH STATUS: ")




if __name__=='__main__':
        unittest.main()

