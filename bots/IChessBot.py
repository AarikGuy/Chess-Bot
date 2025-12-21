import chess

from helpers.BoardHelper import Board
from abc import ABC, abstractmethod
from chess import Board, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, WHITE, BLACK, Move

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

    def __init__(self):
        self.move_black_list = set() 

    def black_list_move(self, move: Move, board: Board):
        chess_board = str(board)
        move_san = board.san(move)
        move_key = f"{move_san} - {chess_board}"

        if (move_key in self.move_black_list):
            raise Exception("A duplicate board is being added to the previous boards set")

        self.move_black_list.add(move_key)

    def is_move_black_listed(self, move: Move, board: Board):
        chess_board = str(board)
        move_san = board.san(move)
        move_key = f"{move_san} - {chess_board}"

        return move_key in self.move_black_list
        
    def generate_move(self, chess_board: Board) -> Board:
        if chess_board.is_checkmate():
            raise Exception("Can't generate move on a completed game.")

        retVal = None
        legal_moves = self.get_legal_moves_list(chess_board)

        while retVal is None:
            move = self.choose_move(legal_moves, chess_board)

            if (self.is_move_black_listed(move, chess_board)):
                legal_moves.remove(move)
                print(f"{chess_board.get_turn()} to move - {chess_board.san(move)} is black listed, trying another move!")
            else:
                print(f"{chess_board.get_turn()} plays {chess_board.san(move)}")
                self.black_list_move(move, chess_board)
                retVal = move

        return retVal 

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
    
    
