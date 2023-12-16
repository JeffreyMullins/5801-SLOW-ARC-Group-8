import config
from Batter import Batter
from Camera import Camera
from StrikeZone import StrikeZone
from shapely.geometry import LineString, Polygon


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
        plate_close_width = strike_zone.back_close_corner[0] - strike_zone.front_close_corner[0]
        plate_far_width = strike_zone.back_far_corner[0] - strike_zone.front_far_corner[0]

        print(f"[Pitch][compute_pitch_status]: plate_close_width -> {plate_close_width}") if config.DEBUG_MODE_ON else None
        print(f"[Pitch][compute_pitch_status]: plate_far_width -> {plate_far_width}") if config.DEBUG_MODE_ON else None

        # Set up the batter
        batter = Batter()
        batter.shoulder1 = data[5]
        batter.shoulder2 = data[6]
        batter.knee1 = data[7]
        batter.knee2 = data[8]

        # Set up the pitch data
        pitch_data = data[9]
        timestamps = [pitch_data[i][0] for i in range(len(pitch_data))]
        ball_center_x = [pitch_data[i][1] for i in range(len(pitch_data))]
        ball_center_y = [pitch_data[i][2] for i in range(len(pitch_data))]
        ball_left_x = [pitch_data[i][3] for i in range(len(pitch_data))]
        ball_left_y = [pitch_data[i][4] for i in range(len(pitch_data))]
        ball_right_x = [pitch_data[i][5] for i in range(len(pitch_data))]
        ball_right_y = [pitch_data[i][6] for i in range(len(pitch_data))]

        print(f"[Pitch][compute_pitch_status]: timestamps -> {timestamps}") if config.DEBUG_MODE_ON else None
        print(f"[Pitch][compute_pitch_status]: ball_left_x -> {ball_left_x}") if config.DEBUG_MODE_ON else None
        print(f"[Pitch][compute_pitch_status]: ball_center_x -> {ball_center_x}") if config.DEBUG_MODE_ON else None
        print(f"[Pitch][compute_pitch_status]: ball_right_x -> {ball_right_x}") if config.DEBUG_MODE_ON else None

        # cook the algorithm here
        call_reason = ""
        for i in range(len(pitch_data)):
            print(f"\n[Pitch][compute_pitch_status]: i -> {i}") if config.DEBUG_MODE_ON else None

            ball_width = ball_right_x[i] - ball_left_x[i]
            ball_ppi = ball_width / 3.8
            print(f"[Pitch][compute_pitch_status]: ball_width -> {ball_width}") if config.DEBUG_MODE_ON else None
            print(f"[Pitch][compute_pitch_status]: ball_ppi -> {ball_ppi}") if config.DEBUG_MODE_ON else None

            # If the ball's x value is past either knee's x value
            if batter.knee2[0] <= ball_right_x[i] or batter.knee1[0] <= ball_right_x[i]:
                # If the ball is below either knee
                if ball_right_y[i] <= batter.knee2[1] or ball_right_y[i] <= batter.knee1[1]:
                    print(f"[Pitch][compute_pitch_status]: BALL: ball past plate and below knee. "
                          f"Knee1 x -> {batter.knee1[0]} OR Knee2 x -> {batter.knee2[0]} <= Ball x -> {ball_right_x[i]} "
                          f"Ball y -> {ball_right_y[i]} <= Knee1 y -> {batter.knee1[1]} OR Knee2 y -> {batter.knee1[1]}") if config.DEBUG_MODE_ON else None
                    self.set_pitch_status("ball")
                    call_reason += "/short & too low/"

                # if ball_width < 8 or 12 < ball_width:
                #     self.set_pitch_status("ball")
                #     call_reason += "/not on plate/"

        # ball_line = LineString(pitch_data)
        # strike_zone_polygon = Polygon()

        print(f"[Pitch][compute_pitch_status]: pitch status -> {self.pitch_status}\n") if config.DEBUG_MODE_ON else None
        print(f"[Pitch][compute_pitch_status]: call reason -> {call_reason}\n") if config.DEBUG_MODE_ON else None

        return None

    def set_pitch_status(self, new_status: str):
        """
        Sets the status of the pitch object to the given new status.

        :param new_status: The new status of the pitch
        :return: None
        """
        self.pitch_status = new_status

        return None
