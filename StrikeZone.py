import Pitch


class StrikeZone(Pitch):
    def __init__(self) -> None:
        self.strike_zone = []
        self.status = False

    def get_status(self):
        return self.status

    def generate_strike_zone(self):
        return None
