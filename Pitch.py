import config
from Batter import Batter
from Camera import Camera
from StrikeZone import StrikeZone


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
        pitcher (Pitcher): An object representing the pitcher who threw the pitch.
        umpire (Umpire): An object representing the umpire who will make the call on the pitch.
    """

    def __init__(self) -> None:
        self.speed = -1
        self.position = []
        self.current_count = []
        self.pitch_status = ""
        self.time_thrown = ""
        self.pitcher = None
        self.umpire = None

    def compute_pitch_status(self, camera: Camera):
        """
        Computes the status of the pitch based on input data.

        :param camera: The camera to get input data from.
        :return: None
        """
        print("\n[Pitch][compute_pitch_status]: computing pitch status") if config.DEBUG_MODE_ON else None

        # Get data of a pitch from the camera
        data = camera.read_data()
        print(f"[Pitch][compute_pitch_status]: strike_zone data -> {[data[i] for i in range(0, 5)]}") \
            if config.DEBUG_MODE_ON else None
        print(f"[Pitch][compute_pitch_status]: batter data -> {[data[i] for i in range(5, 9)]}") \
            if config.DEBUG_MODE_ON else None
        print(f"[Pitch][compute_pitch_status]: pitch data -> {data[9]}") if config.DEBUG_MODE_ON else None

        # Set up the strike zone
        strike_zone = StrikeZone()
        strike_zone.front_close_corner = data[0]
        strike_zone.back_close_corner = data[1]
        strike_zone.point = data[2]
        strike_zone.back_far_corner = data[3]
        strike_zone.front_far_corner = data[4]
        strike_zone.generate_strike_zone()

        # Set up the batter
        batter = Batter()
        batter.shoulder1 = data[5]
        batter.shoulder2 = data[6]
        batter.knee1 = data[7]
        batter.knee2 = data[8]

        # Set up the pitch data
        pitch_data = data[9]
        timestamps = [pitch_data[i][0] for i in range(len(pitch_data))]
        ball_left_xy = [[pitch_data[i][3], pitch_data[i][4]] for i in range(len(pitch_data))]
        ball_center_xy = [[pitch_data[i][1], pitch_data[i][2]] for i in range(len(pitch_data))]
        ball_right_xy = [[pitch_data[i][5], pitch_data[i][6]] for i in range(len(pitch_data))]

        print(f"[Pitch][compute_pitch_status]: timestamps -> {timestamps}") if config.DEBUG_MODE_ON else None
        print(f"[Pitch][compute_pitch_status]: ball_left_xy -> {ball_left_xy}") if config.DEBUG_MODE_ON else None
        print(f"[Pitch][compute_pitch_status]: ball_center_xy -> {ball_center_xy}") if config.DEBUG_MODE_ON else None
        print(f"[Pitch][compute_pitch_status]: ball_right_xy -> {ball_right_xy}") if config.DEBUG_MODE_ON else None

        # cook the algorithm here

        print(f"[Pitch][compute_pitch_status]: pitch status -> {self.pitch_status}\n") if config.DEBUG_MODE_ON else None

        return None

    def set_pitch_status(self, new_status: str):
        """
        Sets the status of the pitch object to the given new status.

        :param new_status: The new status of the pitch
        :return: None
        """
        self.pitch_status = new_status

        return None
