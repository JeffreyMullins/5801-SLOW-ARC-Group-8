import os
import threading
import time

import globals


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
        self.umpire_input = input("ENTER NEW PITCH STATUS: ")

    def change_pitch_status(self, pitch):
        """
        Changes the status of a given pitch to the umpire's new determination.
        The umpire has 2 seconds to make a determination before no change is assumed.

        :param pitch: The pitch object that's status needs to be changed.
        :return: True if the pitch status was changed, otherwise False.
        """
        print("\n[Umpire][change_pitch_status]: starting") if globals.DEBUG_MODE else None

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
        print(f"[Umpire][change_pitch_status]: start_time -> {start_time}") if globals.DEBUG_MODE else None

        # Receive and validate umpire input. The umpire has global.UMPIRE_TIMEOUT_TIME seconds before none is assumed.
        while True:
            print(f"\n[Umpire][change_pitch_status]: creating input_thread") if globals.DEBUG_MODE else None
            input_thread = threading.Thread(target=self.get_terminal_input)
            input_thread.start()

            # Wait global.UMPIRE_TIMEOUT_TIME then continue on
            input_thread.join(timeout=globals.UMPIRE_TIMEOUT_TIME)

            # If the thread is still alive then exit the loop as that means over global.UMPIRE_TIMEOUT_TIME has passed
            if input_thread.is_alive():
                break

            # If valid input was received from the thread then exit the loop
            if self.umpire_input in all_valid_inputs:
                break

            # If elapsed time is greater than globals.UMPIRE_TIMEOUT_TIME then exit the loop
            elapsed_time = time.time() - start_time
            if elapsed_time >= globals.UMPIRE_TIMEOUT_TIME:
                break

        # Set the pitch status or return false if the umpire did not change the status
        if self.umpire_input in none_inputs:
            return False
        elif self.umpire_input in ball_inputs:
            pitch.set_pitch_status("ball")
        elif self.umpire_input in strike_inputs:
            pitch.set_pitch_status("strike")

        return True

    def exit(self):
        """
        Exits the program.
        Uses exit with os to terminate still waiting umpire.read_terminal_input threads
        """
        os._exit(0)

    def create_output_file(self, pitches_list):
        """
        Creates an output file containing the result of each pitch in pitches_list.

        :param pitches_list: A list of pitch objects to create an output file for.
        :return: None
        """
        output_file = open("output.txt", "w")

        pitch_count = len(pitches_list)
        output_file.write(f"pitch count, {pitch_count}\n")

        for index, pitch in enumerate(pitches_list):
            pitch_status = pitch.pitch_status
            output_file.write(f"{index}, {pitch_status}\n")

        return None
