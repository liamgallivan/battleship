"""
Author: Liam Gallivan
Description: For testing and running game
"""
from game.engine.engine import BattleshipEngine
from game.player import HumanPlayer, SimpleAIPlayer


if __name__ == '__main__':
    game = BattleshipEngine(HumanPlayer("Player 1"), SimpleAIPlayer("AI"))
    game.play()
