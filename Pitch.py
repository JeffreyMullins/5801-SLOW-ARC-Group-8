import globals


class Pitch:
    """
    Used to capture the characteristics of each pitch thrown, to be used to compute the pitch determination.

    Attributes:
        speed (float): The speed of the pitch in miles per hour.
        position (list): A list storing the coordinates of the ball at various points during its flight.
        current_count (list): Keeps track of the current ball and strike count before the pitch is thrown.
        pitch_status (str): A string describing the status of the pitch, either "ball" or "strike".
        time_thrown (str): A string representing the time when the pitch was thrown, in a specific
            date-time format.
        pitcher: An object representing the pitcher who threw the pitch.
        umpire: An object representing the umpire who will make the call on the pitch.
    """

    def __init__(self) -> None:
        self.speed = -1
        self.position = []
        self.current_count = []
        self.pitch_status = ""
        self.time_thrown = ""
        self.pitcher = None
        self.umpire = None

    def compute_pitch_status(self, camera):
        """
        Computes the status of the pitch based on input data.

        :param camera: The camera to get input data from.
        :return: None
        """
        print("\n[Pitch][compute_pitch_status]: computing pitch status") if globals.DEBUG_MODE else None
        pitch_data = camera.read_data()

        print(f"[Pitch][compute_pitch_status]: pitch data -> {pitch_data[9]}") if globals.DEBUG_MODE else None

        # algorithm here
        print(f"[Pitch][compute_pitch_status]: pitch status -> {self.pitch_status}\n") if globals.DEBUG_MODE else None

        return None

    def set_pitch_status(self, new_status):
        """
        Sets the status of the pitch object to the new status.

        :param new_status: The new status of the pitch
        :return: None
        """
        self.pitch_status = new_status

        return None
