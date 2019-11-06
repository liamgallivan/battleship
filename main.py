"""
Author: Liam Gallivan
Description: For testing and running game
"""
from game.engine.engine import BattleshipEngine
from game.player import HumanPlayer


if __name__ == '__main__':
    game = BattleshipEngine(HumanPlayer(), HumanPlayer())
    game.play()