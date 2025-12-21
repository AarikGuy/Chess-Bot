import random

from chess import Board
from bots.IChessBot import IChessBot

"""
Chess bot that makes random moves.
Any human player or chess bot with a
strategy that plays for a win should
be able to beat this bot.
"""
class DoorMatChessBot(IChessBot):

    def __init__(self):
        IChessBot.__init__(self)

    def choose_move(self, legal_moves: list, chess_board: Board):
        if legal_moves is None or len(legal_moves) == 0:
            raise Exception("Attempting to pick a move when there are no choices.")

        legal_move = random.choice(legal_moves)

        self.get_fitness_scores(chess_board)

        return legal_move
