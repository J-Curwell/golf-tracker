"""
Standard shot:
- Holed: True / None
- Direction: Correct / Left / Right
- Distance: Correct / Long / Short
- Flight: Straight / Hook / Slice
- Connection: Pure / Fat / Thin

Putting:
- Holed: True / None
- Direction: Correct / Left / Right
- Distance: Correct / Long / Short
- Connection: Push / Pull

"""
from typing import List


class Shot:
    def __init__(self,
                 club: str,
                 direction: str,
                 distance: str,
                 flight: str,
                 connection: str,
                 holed: bool = None):
        """
        Describes a golf shot.
        """
        self.club = club
        self.direction = direction
        self.distance = distance
        self.flight = flight
        self.connection = connection
        self.holed = holed or False


class Hole:
    def __init__(self,
                 hole_number: int,
                 shots: List[Shot]):
        """
        Describes a golf hole.
        """
        self.hole_number = hole_number
        self.shots = shots


class Round:
    def __init__(self,
                 holes: List[Hole]):
        """
        Describes a round of golf.
        """
        self.holes = holes

    def get_round_data(self):
        pass
