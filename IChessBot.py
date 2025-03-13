from abc import ABC, abstractmethod
from chess import Board


class IChessBot(ABC):

    def generate_move(self, chess_board: Board) -> Board:
        if chess_board.is_checkmate():
            raise Exception("Can't generate move on a completed game.")

        legal_moves = list(chess_board.legal_moves)
        legal_move = self.choose_move(legal_moves)

        return legal_move

    @abstractmethod
    def choose_move(self, legal_moves: list):
        pass
