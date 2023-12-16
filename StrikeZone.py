import Pitch


class StrikeZone:
    """
    Represents a strike zone in a baseball game.

    Attributes:
        strike_zone (list): A list representing the boundaries of the strike zone. It is of the form [x, y] coordinates in integers.
        status (bool): The current status of the strike zone, indicating whether it is active or not.
        front_close_corner (list): Coordinates of the front close corner of the strike zone in the form [x, y].
        back_close_corner (list): Coordinates of the back close corner of the strike zone in the form [x, y].
        point (list): Coordinates representing a point within the strike zone in the form [x, y].
        back_far_corner (list): Coordinates of the back far corner of the strike zone in the form [x, y].
        front_far_corner (list): Coordinates of the front far corner of the strike zone in the form [x, y].
    """
    def __init__(self) -> None:
        self.strike_zone = []
        self.status = False
        self.front_close_corner = []
        self.back_close_corner = []
        self.point = []
        self.back_far_corner = []
        self.front_far_corner = []

    def get_status(self):
        return self.status

    def generate_strike_zone(self):
        return None
