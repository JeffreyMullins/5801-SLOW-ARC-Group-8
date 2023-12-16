# from unittest import TestCase
# from unittest import main
from Camera import Camera
import unittest
import csv
import os
import config


class test_Camera(unittest.TestCase):
    def test_init(self):
        # Test the initialization of all Camera object attributes
        test_camera = Camera()
        self.assertEqual(test_camera.locations, [])
        self.assertEqual(test_camera.status, False)
        self.assertEqual(test_camera.parsed_files, [])

        
    def test_read_data(self):
        # Tests to make sure that the read_data can parse a CSV file and correctly increment the number of parsed files

        test_camera = Camera()

        file = open("datafiles/pitch_005130.csv", 'r')

        test_camera.parse_csv_file(file)
        
        self.assertEqual(len(test_camera.parsed_files), 1)

        data = test_camera.read_data()

        self.assertEqual(len(test_camera.parsed_files), 0)



if __name__=='__main__':
        unittest.main()

