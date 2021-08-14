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
import pandas as pd


class Shot:
    def __init__(self,
                 club: str,
                 distance: str,
                 direction: str,
                 connection: str,
                 flight: str = None,
                 holed: bool = None):
        """
        Describes a golf shot.
        """
        self.club = club
        self.distance = distance
        self.direction = direction
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

        # Log the total number of shots
        total_shots = 0
        for hole in self.holes:
            total_shots += len(hole.shots)
        self.total_shots = total_shots

        # Also log the total number of putts
        total_putts = 0
        for hole in self.holes:
            for shot in hole.shots:
                if shot.club == 'putter':
                    total_putts += 1
        self.total_putts = total_putts

    def get_round_data(self):
        data = []
        shot_number = 1
        for hole in self.holes:
            for shot in hole.shots:
                shot_data = shot.__dict__
                shot_data['shot_number'] = shot_number
                data.append(shot_data)
                shot_number += 1

        return pd.DataFrame(data)
