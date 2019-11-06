"""
Author: Liam Gallivan
Description: Game engine cloning 'Battleship' board game
    features:
"""

import random
from ..player import Player


class BattleshipEngine:
    GRID_HEIGHT = 10
    GRID_WIDTH = 10

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.curr_turn = random.randrange(1,3) # rand int 1 or 2
        self.board1 = None
        self.board2 = None

    def play(self):
        self.setup()
        print("Here is your board: ")
        self.board1.print_board()

    def setup(self):
        # Initializes player game boards
        self.board1 = self.player1.create_board(BattleshipEngine.GRID_WIDTH,
                                                BattleshipEngine.GRID_HEIGHT)
        # self.board2 = self.player2.create_board(BattleshipEngine.GRID_WIDTH,
        #                                         BattleshipEngine.GRID_HEIGHT)


    def take_turn(self):
        pass

    def print_game_status(self):
        pass

    def __copy__(self):
        pass
