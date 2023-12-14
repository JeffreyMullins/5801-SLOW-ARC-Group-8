# NOT OFFICAL COMMENT, PLEASE EDIT LATER: this is the main file for the SLOW-ARC system
import os
import sys

import globals
from Camera import Camera
from Display import Display
from Pitcher import Pitcher
from Umpire import Umpire


def main():
    print("Hi I'm the slow arc system, I'll go do things now.")

    # Initialize the umpire for the game
    umpire = Umpire()

    # Initialize the camera for the game
    camera = Camera()
    input_directory_path = "datafiles/"
    camera.process_directory(input_directory_path)

    # Initialize the display for the game
    display = Display()

    # Initialize the pitcher for the game
    pitcher = Pitcher()
    pitcher.umpire = umpire
    pitcher.camera = camera
    pitcher.display = display
    pitcher.state = True

    print(f'[main]: camera.parsed_files length -> {len(camera.parsed_files)}') if globals.DEBUG_MODE else None

    i = 0
    for i in range(len(camera.parsed_files)):
        print(f"\n[main]: calling pitcher.throw_pitch() number > {i}") if globals.DEBUG_MODE else None
        pitcher.throw_pitch()
        i += 1

    print("Finished, have a good day!")

    umpire.exit()



if __name__ == "__main__":
    # first func that runs the main function
    main()
