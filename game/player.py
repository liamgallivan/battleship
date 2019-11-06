"""
Author: Liam Gallivan
Description: 'Player' base class for generic methods and attributes
             and extensions on base class:
                - HumanPlayer
"""
from .engine.board import Board
from .engine.ships import Ship, get_standard_ship_types
from .util import Directions

class Player:

    def __init__(self):
        pass

    def create_board(self, board_width, board_height) -> Board:
        pass
    
    def make_guess(self, board: Board):
        pass

class HumanPlayer(Player):

    def __init__(self):
        super(Player)

    def create_board(self, board_width, board_height) -> Board:
        ship_types = get_standard_ship_types()
        print("Please place ships on board({}x{}):\n\n".format(
            board_width, board_height))
        print("- For each ship enter starting index and direction in format:")
        print("column, row, direction")
        print("- Choices for direction are [NORTH, EAST, SOUTH, WEST]")

        ship_placements = []
        occupied_coords = set()
        for ship_type in ship_types:
            working = True
            name = ship_type[0]
            size = ship_type[1]
            while working:
                print("{} (size {})".format(name, size))
                choice = input().split(',')
                choice[0] = int(choice[0].strip())
                choice[1] = int(choice[1].strip())
                print(choice)
                if len(choice) != 3:
                    print("Incorrect format for input. Please try again.")
                else:
                    begin_coord = (choice[0], choice[1])
                    direction = Directions[choice[2].strip()]
                    new_ship = Ship(name, size, begin_coord, direction)
                    new_occupied_coordinates = new_ship.get_all_coord()
                    end_coord = new_occupied_coordinates[-1]
                    if 0 <= begin_coord[0] < board_width and \
                            0 <= begin_coord[1] < board_height \
                            and 0 <= end_coord[0] < board_width \
                            and 0 <= end_coord[1] < board_height \
                            and occupied_coords.isdisjoint(set(new_occupied_coordinates)):
                        ship_placements.append(new_ship)
                        occupied_coords.update(new_occupied_coordinates)
                        working = False
                    else:
                        print("Please enter valid coordinates")

        print("All locations entered. Good luck!")
        new_board = Board(board_width, board_height, ship_placements)
        return new_board

    def make_guess(self, board: Board) -> (int, int):
        # print("Make a guess: ")
        # coords = map(lambda a: a.strip(), input().split(','))
        # if coords[0]
        # return coords[0], coords[1]
        pass






