"""
TODO: Ensure attributes can only take the following values:

Standard shot:
- Holed: True / False
- Direction: Correct / Left / Right
- Distance: Correct / Long / Short
- Flight: Straight Draw / Hook / Fade / Slice
- Connection: Pure / Fat / Thin

Putting:
- Holed: True / None
- Direction: Correct / Left / Right
- Distance: Correct / Long / Short
- Connection: Push / Pull
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List

import pandas as pd


@dataclass
class Shot:
    """
    Describes a golf shot.
    """
    club: str
    distance: str
    direction: str
    connection: str
    holed: bool = False
    flight: str = None


@dataclass
class Hole:
    """
    Describes a golf hole.
    """
    hole_number: int
    shots: List[Shot]


class Round:
    def __init__(self,
                 holes: List[Hole],
                 course: str = None):
        """
        Describes a round of golf.
        """
        self.holes = holes
        self.course = course or 'round'

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
        for hole_number, hole_data in enumerate(self.holes, start=1):
            for hole_shot_n, shot in enumerate(hole_data.shots, start=1):
                shot_data = {
                    'hole': hole_number,
                    'hole_shot': hole_shot_n
                }
                shot_data.update(shot.__dict__)
                shot_data['total_shots'] = shot_number
                data.append(shot_data)
                shot_number += 1

        return pd.DataFrame(data)

    def save_round(self, dir_path: str = None):
        if dir_path and dir_path[-1] == '/':
            dir_path = dir_path[:-1]

        round_data = self.get_round_data()
        now = datetime.now()
        round_name = f'{self.course}_{now.date()}'
        round_data.to_csv(f'{dir_path}/{round_name}.csv')
