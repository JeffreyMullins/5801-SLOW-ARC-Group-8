import globals
from Pitch import Pitch


class Pitcher:
    def __init__(self) -> None:
        self.state = False
        self.pitches_list = []
        self.num_pitches = -1
        self.umpire = None
        self.camera = None
        self.display = None

    def throw_pitch(self):
        """
        Creates a new pitch object for the pitcher and computes whether it was a ball or strike.

        :return: None
        """
        if self.state is False:
            return None

        print("\n[Pitcher][throw_pitch]: throwing pitch") if globals.DEBUG_MODE else None

        # Initialize a new pitch object
        pitch = Pitch()
        pitch.umpire = self.umpire
        pitch.pitcher = self

        # Update pitcher attributes
        self.num_pitches += 1
        self.pitches_list.append(pitch)

        # Compute the result of the pitch
        print("[Pitcher][throw_pitch]: calling pitch.compute_pitch_status") if globals.DEBUG_MODE else None
        pitch.compute_pitch_status(self.camera)
        print("[Pitcher][throw_pitch]: compute_pitch_status finished") if globals.DEBUG_MODE else None

        # Read user decision on the pitch
        print("[Pitcher][throw_pitch]: calling display.read_user_decision") if globals.DEBUG_MODE else None
        self.display.read_user_decision(pitch, self.umpire)

        return None

    def get_all_pitches_status(self):
        return None
