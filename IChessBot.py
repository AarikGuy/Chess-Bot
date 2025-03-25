import chess
from abc import ABC, abstractmethod
from chess import Board, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, WHITE, BLACK

PIECE_WEIGHTS = {
    PAWN: 1,
    KNIGHT: 2.5,
    BISHOP: 2.51,
    ROOK: 5,
    QUEEN: 10,
    KING: 10000000000,
}

FILES = ["a", "b", "c", "d", "e", "f", "g", "h"]
ROWS = ["1", "2", "3", "4", "5", "6", "7", "8"]


class IChessBot(ABC):

    def generate_move(self, chess_board: Board) -> Board:
        if chess_board.is_checkmate():
            raise Exception("Can't generate move on a completed game.")

        legal_moves = self.get_legal_moves_list(chess_board)
        legal_move = self.choose_move(legal_moves, chess_board)

        return legal_move

    @abstractmethod
    def choose_move(self, legal_moves: list, chess_board: Board):
        pass

    def get_legal_moves_list(self, chess_board: Board):
        return list(chess_board.legal_moves)

    def get_fitness_scores(self, chess_board: Board):
        white_fitness_score = 0
        black_fitness_score = 0

        for file in FILES:
            for row in ROWS:
                square = chess.parse_square(file + row)
                piece = chess_board.piece_at(square)

                if piece is None:
                    continue

                piece_weight = PIECE_WEIGHTS.get(piece.piece_type)

                if piece.color == WHITE:
                    white_fitness_score += piece_weight
                else:
                    black_fitness_score += piece_weight

        return [white_fitness_score, black_fitness_score]
