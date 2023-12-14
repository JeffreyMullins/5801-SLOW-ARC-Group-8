import globals


class Display:
    """
    Used to display the result of pitch's to the terminal
    and prompt for the umpire to change the pitch's result.

    Attributes:
        current_result (str): The result/status of the current pitch being displayed.
    """

    def __init__(self) -> None:
        self.current_result = ""

    def display(self, pitch):
        """
        Displays the result of a pitch object to the terminal.

        :param pitch: The pitch that's status will be displayed.
        :return: None
        """
        if pitch is None:
            return None

        # Print out the result of the pitch
        print("\n==================")
        if pitch.pitch_status == "ball":
            print("====== BALL ======")
            self.current_result = "ball"
        elif pitch.pitch_status == "strike":
            print("===== STRIKE =====")
            self.current_result = "strike"
        else:
            print("===== ERROR =====")
        print("==================")

        return None

    def read_user_decision(self, pitch, umpire):
        """
        Reads the decision of the umpire on a pitch's result. Then displays the result of the pitch.

        :param pitch: The pitch object that will be sent to the umpire.
        :param umpire: The umpire object whose decision will be read.
        :return: None
        """
        # Get the umpire's determination of the pitch
        print("\n[Display][read_user_decision]: calling umpire.change_pitch_status") if globals.DEBUG_MODE else None
        umpire.change_pitch_status(pitch)

        # Display the pitch result
        print("\n[Display][read_user_decision]: calling self.display") if globals.DEBUG_MODE else None
        self.display(pitch)

        return None