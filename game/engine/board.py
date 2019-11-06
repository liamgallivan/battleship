"""
Author: Liam Gallivan
Description: class for board object, represents a grid of ships, guesses,
            and ship info
"""


class Board:

    def __init__(self, width, height, ships=None):
        self.width = width
        self.height = height
        self.guess_matrix = [[0] * height for _ in range(width)]
        self.guesses = set()
        self.hits = set()
        self.misses = set()
        self.ships = ships
        self.sunk_ships = {}
        self.valid_hits = None
        if self.ships is not None:
            self.valid_hits = set()
            for ship in self.ships:
                for tup in ship.coordinates:
                    self.valid_hits.add(tup)

    def print_stats(self):
        print("Stats for board:")
        if self.check_win():
            print("Winning board")
        else:
            print("Ongoing board")

        print("Number of guesses: {}".format(len(self.guesses)))
        print("Number of hits: {}".format(len(self.hits)))
        print("Number of misses: {}".format(len(self.misses)))
        print("Hit percentage: {}".format(float(len(self.hits)) / float(len(self.guesses))))

    def print_board(self, show_ships=False):
        edge_line = "-" * (self.width * 5 + 4)
        print(edge_line)
        for i in range(self.width - 1, -1, -1):
            line = "| " + str(i) + "|"
            for j in range(self.height):
                symbol = '-'
                if self.guess_matrix[j][i] == 1:
                    symbol = 'X'
                elif self.guess_matrix[j][i] == -1:
                    symbol = 'O'
                elif show_ships is True and self.valid_hits is not None \
                        and (j, i) in self.valid_hits:
                    symbol = "="
                line += "  " + symbol + " |"
            print(line)
            print(edge_line)

        print("|  " + " ".join(["|  " + str(i) for i in range(self.height)]) +
              " |")
        print(edge_line)

    def is_hit(self, coord: (int, int)):
        if coord in self.valid_hits:
            return True
        else:
            return False

    def add_guess(self, coord: (int, int), hit_status: bool):
        """
        Adds guess to sets and returns Ship object if it sinks a ship
        """
        if coord in self.guesses:
            return None

        self.guesses.add(coord)
        if hit_status is True:
            self.hits.add(coord)
            self.guess_matrix[coord[0]][coord[1]] = 1
            curr_ship = None
            for ship in self.ships:
                if coord in set(ship.coordinates):
                    curr_ship = ship
                    break

            if curr_ship is not None and \
                    set(curr_ship.coordinates).issubset(self.hits):
                # records coord when ship sunk
                self.sunk_ships[curr_ship.name] = coord
                return curr_ship
            else:
                return None
        else:
            self.misses.add(coord)
            self.guess_matrix[coord[0]][coord[1]] = -1
            return None

    def check_win(self):
        return len(self.valid_hits) <= len(self.hits)


