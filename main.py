import config
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
    input_directory_path = config.INPUT_DIRECTORY_PATH
    if input_directory_path is None or input_directory_path == "":
        print("ERROR: please specify an input directory in config.py")
        return
    camera.process_directory(input_directory_path)

    # Initialize the display for the game
    display = Display()

    # Initialize the pitcher for the game
    pitcher = Pitcher()
    pitcher.umpire = umpire
    pitcher.camera = camera
    pitcher.display = display
    pitcher.state = True

    print(f'[main]: camera.parsed_files length -> {len(camera.parsed_files)}') if config.DEBUG_MODE_ON else None

    i = 0
    for i in range(len(camera.parsed_files)):
        print(f"\n[main]: calling pitcher.throw_pitch() number -> {i}") if config.DEBUG_MODE_ON else None
        pitcher.throw_pitch()
        i += 1

    print("Finished, have a good day!")

    # Create an output file then exit
    umpire.create_output_file(pitcher.pitches_list)
    umpire.exit()


if __name__ == "__main__":
    # first func that runs the main function
    main()
