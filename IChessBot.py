from abc import ABC, abstractmethod
from chess import Board


class IChessBot(ABC):

    @abstractmethod
    def generate_move(self, chess_board: Board) -> Board:
        pass
