from chess import Board


from IChessBot import IChessBot
import random


# Incredibly stupid chess bot. Chooses a random legal move every turn. A human player can beat him easily.


class DoorMatChessBot(IChessBot):

    def __init__(self):
        pass

    def choose_move(self, legal_moves: list, chess_board: Board):
        if legal_moves is None or len(legal_moves) == 0:
            raise Exception("Attempting to pick a move when there are no choices.")

        legal_move = random.choice(legal_moves)

        self.get_fitness_scores(chess_board)

        return legal_move
