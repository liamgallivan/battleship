"""
Author: Liam Gallivan
Description: Classes and functions for dealing with ship info
"""
from ..util import Directions


class Ship:
    def __init__(self, name, size, begin_coord, direction):
        self.name = name
        self.size = size
        self.begin_coord = begin_coord
        self.dir = direction
        self.coordinates = self.get_all_coord()

    def get_all_coord(self) -> list:
        vert_mod = 0
        horiz_mod = 0
        if self.dir == Directions.NORTH:
            vert_mod = 1
        elif self.dir == Directions.EAST:
            horiz_mod = 1
        elif self.dir == Directions.SOUTH:
            vert_mod = -1
        elif self.dir == Directions.WEST:
            horiz_mod = -1

        return set([(self.begin_coord[0] + horiz_mod * i,
                 self.begin_coord[1] + vert_mod * i) for i in range(self.size)])


def get_standard_ship_types() -> list:
    return [("Carrier", 5),
            ("Battleship", 4),
            ("Cruiser", 3),
            ("Submarine", 3),
            ("Destroyer", 2)]
