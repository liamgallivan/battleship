"""
Author: Liam Gallivan
Description: 'Player' base class for generic methods and attributes
             and extensions on base class:
                - HumanPlayer
"""
from .engine.board import Board
from .engine.ships import Ship, get_standard_ship_types
from .util import Directions
import random


class Player:

    def __init__(self, player_name):
        self.player_name = player_name

    def create_board(self, board_width, board_height) -> Board:
        pass
    
    def make_guess(self, board: Board):
        pass

    def record_win(self, winning_board: Board, losing_board: Board):
        pass

    def record_loss(self, losing_board: Board, winning_board: Board):
        pass


class HumanPlayer(Player):
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
                    direction = Directions[choice[2].strip().upper()]
                    new_ship = Ship(name, size, begin_coord, direction)
                    new_occupied_coordinates = new_ship.coordinates
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
        working = True
        coord = None
        while working:
            board.print_board()
            print("Please enter coordinates to strike: ")
            choices = input().split(',')
            coord = (int(choices[0].strip()), int(choices[1].strip()))
            if 0 <= coord[0] < board.width and 0 <= coord[1] < board.height:
                if coord in board.guesses:
                    print("{} has already been tried".format(coord))
                else:
                    working = False
            else:
                print("Only accepts coordinates in range (0-{}, 0-{})".format(
                    board.width - 1, board.height - 1))

        if board.is_hit(coord):
            print("Hit at coordinate {}!".format(coord))
            sunk_ship = board.add_guess(coord, True)
            if sunk_ship is not None:
                print("Sunk enemy {}. Last shot at {}".format(
                    sunk_ship.name, coord))
        else:
            board.add_guess(coord, False)
            print("Miss at coordinate {}!".format(coord))

    def record_win(self, winning_board: Board, losing_board: Board):
        print("Congratulations {}, you have won!".format(self.player_name))
        winning_board.print_board(show_ships=True)
        print("Winning stats:")
        winning_board.print_stats()


class SimpleAIPlayer(Player):

    def create_board(self, board_width, board_height) -> Board:
        # pre-generated board
        ship_placements = []
        ship_placements.append(Ship("Carrier", 5, (3, 4), Directions.NORTH))
        ship_placements.append(Ship("Battleship", 4, (0, 0), Directions.EAST))
        ship_placements.append(Ship("Cruiser", 3, (8, 9), Directions.WEST))
        ship_placements.append(Ship("Submarine", 3, (9, 9), Directions.SOUTH))
        ship_placements.append(Ship("Destroyer", 2, (4, 6), Directions.NORTH))
        return Board(board_width, board_height, ship_placements)

    def make_guess(self, board: Board):
        working = True
        coord = None
        while working:
            coord = (random.randrange(0, board.width),
                     random.randrange(0, board.height))
            if 0 <= coord[0] < board.width and 0 <= coord[1] < board.height \
                    and coord not in board.guesses:
                working = False

        board.add_guess(coord, board.is_hit(coord))
