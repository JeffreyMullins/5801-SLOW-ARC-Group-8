import csv
import os

import config


class Camera:
    """
    Used to hold the status of and the data read in by a camera.
    In this implementation of SLOW-ARC, uses data files in a directory as input instead of video.

    Attributes:
        locations (list): List of strings storing the location on the field the camera is
        status (bool): The status of the camera
        parsed_files (list): List of parsed file data. Each entry represents a full set of pitch data.
    """

    def __init__(self) -> None:
        self.locations = []
        self.status = False
        self.parsed_files = []

    def parse_csv_file(self, csv_file):
        csv_reader = csv.reader(csv_file)

        # Holds all data from the file
        file_data = []

        # Holds only data for the pitch. Gets put into file_data.
        pitch_data = []

        line_counter = 0
        for row in csv_reader:
            # Read data for strike zone and batter
            if line_counter < 9:
                pair = [row[i] for i in range(2)]
                file_data.append(pair)
            # Read pitch data
            else:
                line = [row[i] for i in range(7)]
                pitch_data.append(line)
            line_counter += 1

        # Add the pitch data to the file data
        file_data.append(pitch_data)

        # Add the file data to the camera's parsed files
        self.parsed_files.append(file_data)

        return None

    def process_directory(self, directory_path: str):
        """
        Traverses the given directory path for regular files and runs parse_csv_file() on each one.

        :param directory_path: The directory to traverse.
        :return: None
        """
        if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
            print("ERROR: given input path is not a directory or doesn't exist")

        print("\n[Camera][process_directory]: starting traversal") if config.DEBUG_MODE_ON else None
        # Traverse the given directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Ensure the file is a regular file
            if os.path.isfile(file_path):
                file = open(file_path, 'r')
                print(f"[Camera][process_directory]: parsing file -> {file_path}") if config.DEBUG_MODE_ON else None
                self.parse_csv_file(file)

        print("[Camera][process_directory]: traversal done\n") if config.DEBUG_MODE_ON else None
        return None

    def read_data(self):
        """
        Returns a list of data from a pitch data file.

        :return: data of one pitch
        """
        data = self.parsed_files.pop()

        return data

    def stop_read_data(self):
        return None

    def save_data(self):
        return None
