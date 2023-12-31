import config
from Pitch import Pitch


class Pitcher:
    """
       Represents a pitcher in a baseball game.

       Attributes:
           state (bool): The current state of the pitcher, indicating whether they are active or not.
           pitches_list (list): A list of pitch objects thrown by the pitcher.
           num_pitches (int): The total number of pitches thrown by the pitcher.
           umpire: Reference to the umpire object responsible for making pitch status decisions.
           camera: Reference to the camera object used to capture the pitch.
           display: Reference to the display object for user interactions.
    """
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

        print("\n[Pitcher][throw_pitch]: throwing pitch") if config.DEBUG_MODE_ON else None

        # Initialize a new pitch object
        pitch = Pitch()
        pitch.umpire = self.umpire
        pitch.pitcher = self

        # Update pitcher attributes
        self.num_pitches += 1
        self.pitches_list.append(pitch)

        # Compute the result of the pitch
        print("[Pitcher][throw_pitch]: calling pitch.compute_pitch_status") if config.DEBUG_MODE_ON else None
        pitch.compute_pitch_status(self.camera)
        print("[Pitcher][throw_pitch]: compute_pitch_status finished") if config.DEBUG_MODE_ON else None

        # Read user decision on the pitch
        print("[Pitcher][throw_pitch]: calling display.read_user_decision") if config.DEBUG_MODE_ON else None
        self.display.read_user_decision(pitch, self.umpire)

        return None

    def get_all_pitches_status(self):
        pitch_statuses = []
        for p in pitches_list:
            pitch_statuses.append(p.pitch_status)

        return pitch_statuses
