"""
Author: Liam Gallivan
Description: class for board object, represents a grid of ships, guesses, and ship info
"""
from functools import reduce


class Board:

    def __init__(self, width, height, ships=None):
        self.width = width
        self.height = height
        self.guess_matrix = [[0] * height for _ in range(width)]
        self.guesses = []
        self.hits = []
        self.misses = []
        self.ships = ships

    def print_board(self):
        edge_line = "-" * (self.width * 5 + 4)
        print(edge_line)
        ship_coords = None
        if self.ships is not None:
            ship_coords = set()
            for ship in self.ships:
                for tup in ship.coordinates:
                    ship_coords.add(tup)
        for i in range(self.width - 1, -1, -1):
            line = "| " + str(i) + "|"
            for j in range(self.height):
                symbol = '-'
                if self.guess_matrix[j][i] == 1:
                    symbol = 'X'
                elif self.guess_matrix[j][i] == -1:
                    symbol = 'O'
                elif ship_coords is not None and (j, i) in ship_coords:
                    symbol = "="
                line += "  " + symbol + " |"
            print(line)
            print(edge_line)

        print("|  " + " ".join(["|  " + str(i) for i in range(self.height)]) +
              " |")
        print(edge_line)
