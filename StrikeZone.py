import Pitch


class StrikeZone():
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
