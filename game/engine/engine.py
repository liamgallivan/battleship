"""
Author: Liam Gallivan
Description: Game engine cloning 'Battleship' board game
    features:
"""

import random
from ..player import Player
from .board import Board


class BattleshipEngine:
    GRID_HEIGHT = 10
    GRID_WIDTH = 10

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        # rand int 1 or 2
        self.curr_turn = random.randrange(1, 3)
        self.board1: Board or None = None
        self.board2: Board or None = None

    def play(self):
        self.setup()
        game_on = True
        winner = 0
        while game_on:
            if self.curr_turn == 1:
                self.player1.make_guess(self.board2)
                self.curr_turn = 2
                if self.board2.check_win():
                    game_on = False
                    winner = 1
            else:
                self.player2.make_guess(self.board1)
                self.curr_turn = 1
                if self.board2.check_win():
                    game_on = False
                    winner = 2

        winner_board = self.board2
        if winner == 1:
            winner_board = self.board1

        print("Congratulations Player {}. You have won!".format(winner))
        winner_board.print_board()
        print("Winning stats:")
        winner_board.print_stats()


    def setup(self):
        # Initializes player game boards
        self.board1 = self.player1.create_board(BattleshipEngine.GRID_WIDTH,
                                                BattleshipEngine.GRID_HEIGHT)
        self.board2 = self.player2.create_board(BattleshipEngine.GRID_WIDTH,
                                                BattleshipEngine.GRID_HEIGHT)

