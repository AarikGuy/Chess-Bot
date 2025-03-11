from abc import ABC, abstractmethod


class IChessBot(ABC):

    @abstractmethod
    def generate_move(self, chess_board: Board) -> Board:
        pass
