import config
from Camera import Camera
from Display import Display
from Pitcher import Pitcher
from Umpire import Umpire


def main():
    #print("Hi I'm the slow arc system, I'll go do things now.")

    # Initialize the umpire for the game
    umpire = Umpire()

    # Initialize the camera for the game
    camera = Camera()
    if config.COMMAND_LINE_MODE is False:
        if config.INPUT_DIRECTORY_PATH is None or config.INPUT_DIRECTORY_PATH == "":
            print("ERROR: please specify an input directory in config.py")
            return
        camera.process_directory(config.INPUT_DIRECTORY_PATH)
        print(f'[main]: camera.parsed_files length -> {len(camera.parsed_files)}') if config.DEBUG_MODE_ON else None

    # Initialize the display for the game
    display = Display()

    # Initialize the pitcher for the game
    pitcher = Pitcher()
    pitcher.umpire = umpire
    pitcher.camera = camera
    pitcher.display = display
    pitcher.state = True

    if config.COMMAND_LINE_MODE is False:
        i = 0
        for i in range(len(camera.parsed_files)):
            print(f"\n[main]: calling pitcher.throw_pitch() number -> {i}") if config.DEBUG_MODE_ON else None
            pitcher.throw_pitch()
            i += 1

    elif config.COMMAND_LINE_MODE is True:
        print("|-----| SLOW-ARC MANUAL MODE |-----|")
        print("type 'exit' or 'e' to exit")

        while True:
            file_name = None
            try:
                file_name = input("\nEnter a filename: ")

                # Exit the loop
                if file_name.lower() in ["exit", "e"]:
                    break

                # Don't allow no input
                if file_name == "":
                    print(f"Error: No file given.")
                    continue

                # Find and parse the file
                file_path = config.INPUT_DIRECTORY_PATH + file_name
                file = open(file_path, 'r')
                camera.parse_csv_file(file)

                # Have the pitcher throw the pitch
                pitcher.throw_pitch()

            except FileNotFoundError:
                print(f"Error: File '{file_name}' not found.")

            except Exception as e:
                print(f"An unexpected error occurred: {e}")

            # pitch_005130.csv
            # pitch_005829.csv
            # pitch_006480.csv

    print("Finished, have a good day!")

    # Create an output file then exit
    umpire.create_output_file(pitcher.pitches_list)
    umpire.exit()


if __name__ == "__main__":
    # first func that runs the main function
    main()
