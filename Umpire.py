import os
import threading
import time
from typing import List

import config
from Pitch import Pitch


class Umpire:
    """
    Can change the status of a pitch and create output files.

    Attributes:
        permissions (bool): Records whether the umpire has the required permissions to override a call
        decision (bool): The decision made by the umpire upon reviewing the pitch, ball or strike, True or False respectively
    """

    def __init__(self) -> None:
        self.permissions = False
        self.decision = False
        self.umpire_input = ""

    def get_terminal_input(self):
        """
        Returns:
        """
        new_status = input("ENTER NEW PITCH STATUS: ")
        if new_status in ["strike", "ball", "s", "b"]:
            self.umpire_input = new_status

        return None

    def change_pitch_status(self, pitch: Pitch):
        """
        Changes the status of a given pitch to the umpire's new determination.
        The umpire has time to make a determination before no change is assumed.
        The amount of time to wait for the umpire is set in config as UMPIRE_TIMEOUT_TIME.

        :param pitch: The pitch object that's status needs to be changed.
        :return: True if the pitch status was changed, otherwise False.
        """
        print("\n[Umpire][change_pitch_status]: starting") if config.DEBUG_MODE_ON else None

        # Ensure pitch is not None
        if pitch is None:
            return False

        # Create valid inputs lists
        ball_inputs = ["ball", "b", "bal"]
        strike_inputs = ["strike", "s", "str"]
        none_inputs = ["none", "n", "no"]
        all_valid_inputs = ball_inputs + strike_inputs + none_inputs

        # Create time
        start_time = time.time()
        print(f"[Umpire][change_pitch_status]: start_time -> {start_time}") if config.DEBUG_MODE_ON else None

        # Receive and validate umpire input. The umpire has global.UMPIRE_TIMEOUT_TIME seconds before none is assumed.
        while True:
            print(f"\n[Umpire][change_pitch_status]: creating input_thread") if config.DEBUG_MODE_ON else None
            input_thread = threading.Thread(target=self.get_terminal_input)
            input_thread.start()

            # Wait global.UMPIRE_TIMEOUT_TIME then continue on
            input_thread.join(timeout=config.UMPIRE_TIMEOUT_TIME)

            # If the thread is still alive then exit the loop as that means over global.UMPIRE_TIMEOUT_TIME has passed
            if input_thread.is_alive():
                break

            # If valid input was received from the thread then exit the loop
            if self.umpire_input in all_valid_inputs:
                break

            # If elapsed time is greater than config.UMPIRE_TIMEOUT_TIME then exit the loop
            elapsed_time = time.time() - start_time
            if elapsed_time >= config.UMPIRE_TIMEOUT_TIME:
                break

        # Set the pitch status or return false if the umpire did not change the status
        if self.umpire_input in none_inputs:
            print(f"\n[Umpire][change_pitch_status]: pitch_status not changed") if config.DEBUG_MODE_ON else None
            return False
        elif self.umpire_input in ball_inputs:
            pitch.set_pitch_status("ball")
        elif self.umpire_input in strike_inputs:
            pitch.set_pitch_status("strike")

        print(f"\n[Umpire][change_pitch_status]: pitch_status -> {pitch.pitch_status}") \
            if config.DEBUG_MODE_ON else None

        return True

    def exit(self):
        """
        Exits the program.
        Uses exit with os to terminate any still waiting umpire.read_terminal_input threads.
        """
        os._exit(0)

    def create_output_file(self, pitches_list: List[Pitch]):
        """
        Creates an output file containing the result of each pitch in pitches_list.

        :param pitches_list: A list of pitch objects to create an output file for.
        :return: None
        """
        print(f"\n[Umpire][create_output_file]: creating output file") if config.DEBUG_MODE_ON else None
        print(f"\n[Umpire][create_output_file]: cwd -> {os.getcwd()}") if config.DEBUG_MODE_ON else None

        # Create the name of the output file
        # output_file_name = config.OUTPUT_DIRECTORY_PATH + "output.txt"
        output_file_name = os.path.join(config.OUTPUT_DIRECTORY_PATH, "output.csv")
        print(f"[Umpire][create_output_file]: output_file_name -> {output_file_name}") if config.DEBUG_MODE_ON else None

        # Ensure that the output directory exists. If not, create it
        if not os.path.exists(config.OUTPUT_DIRECTORY_PATH):
            print(f"[Umpire][create_output_file]: creating OUTPUT_DIRECTORY_PATH") if config.DEBUG_MODE_ON else None
            os.makedirs(config.OUTPUT_DIRECTORY_PATH)

        # Try to create and print to the file
        output_file = None
        try:
            output_file = open(output_file_name, "w")

            pitch_count = len(pitches_list)
            output_file.write(f"pitch count, {pitch_count}\n")
            print(f"[Umpire][create_output_file]: pitch_count -> {pitch_count}") if config.DEBUG_MODE_ON else None

            for index, pitch in enumerate(pitches_list):
                pitch_status = pitch.pitch_status
                print(
                    f"[Umpire][create_output_file]: index, pitch_status -> [{index+1}, {pitch_status}]") if config.DEBUG_MODE_ON else None
                output_file.write(f"{index+1}, {pitch_status}\n")

        except Exception as e:
            print(
                f"[Umpire][create_output_file]: error occurred creating output file") if config.DEBUG_MODE_ON else None

        finally:
            output_file.close()

        return None
