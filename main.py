"""
Author: Liam Gallivan
Description: Runs game game
"""
from game.engine.engine import BattleshipEngine
from game.player import HumanPlayer


if __name__ == '__main__':
    game = BattleshipEngine(HumanPlayer(), HumanPlayer())
    game.play()