from chess import Board

from IChessBot import IChessBot
import random



# Incredibly stupid chess bot. Chooses a random legal move every turn. A human player can beat him easily.
class DoorMat(IChessBot):

    def __init__(self):
        pass


    def generate_move(self, chess_board: Board) -> Board:

        if chess_board.is_checkmate():

            raise Exception("Can't generate move on a completed game.")


        legal_moves = list(chess_board.legal_moves)

        legal_move = random.choice(legal_moves)


        return legal_move

