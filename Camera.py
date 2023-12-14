import csv
import os

import globals


class Camera:
    """
    Used to hold the status of, and the data read in by a camera.
    In this implementation of SLOW-ARC, using data files in a directory as input instead of video.

    Attributes:
        locations (list): List of strings storing the location on the field the camera is
        status (bool):
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
            if line_counter < 9:
                pair = [row[i] for i in range(2)]
                file_data.append(pair)
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
        print("\n[Camera][process_directory]: starting traversal") if globals.DEBUG_MODE else None
        # Traverse the given directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Ensure the file is a regular file
            if os.path.isfile(file_path):
                file = open(file_path, 'r')
                print(f"[Camera][process_directory]: parsing file -> {file_path}") if globals.DEBUG_MODE else None
                self.parse_csv_file(file)

        print("[Camera][process_directory]: traversal done\n") if globals.DEBUG_MODE else None
        return None

    def read_data(self):
        """
        Returns a list of data from a pitch data file.

        :return: data
        """
        data = self.parsed_files.pop()

        return data

    def stop_read_data(self):
        return None

    def save_data(self):
        return None
