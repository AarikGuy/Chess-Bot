import chess
import random

from helpers.BoardHelper import Board, NUMBER_OF_STARTING_PIECES, get_number_of_peices
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
    def __init__(self, random_move_frequency=0):
        self.move_black_list = set()
        self.random_move_frequency = random_move_frequency
        self.moves_made = 0
        self.pieces_on_board = NUMBER_OF_STARTING_PIECES

    def black_list_move(self, move: Move, board: Board):
        chess_board = str(board)
        move_san = board.san(move)
        move_key = f"{move_san} - {chess_board}"

        if move_key in self.move_black_list:
            raise Exception(
                "A duplicate board is being added to the previous boards set"
            )

        self.move_black_list.add(move_key)

    def is_move_black_listed(self, move: Move, board: Board):
        chess_board = str(board)
        move_san = board.san(move)
        move_key = f"{move_san} - {chess_board}"

        return move_key in self.move_black_list

    def generate_move(self, chess_board: Board) -> Move:
        if chess_board.is_checkmate():
            raise Exception("Can't generate move on a completed game.")

        selected_move = None
        legal_moves = list(chess_board.legal_moves)
        self.moves_made += 1

        if len(legal_moves) == 0:
            raise Exception(
                "Attempting to generate a move from a board that has no legal moves!"
            )

        """
        Choose a random move
        if the bot was configured
        to do so."""
        if (
            self.random_move_frequency > 0
            and self.moves_made % self.random_move_frequency == 0
        ):
            selected_move = random.choice(legal_moves)

        while selected_move is None:
            move = self.choose_move(legal_moves, chess_board)

            if self.is_move_black_listed(move, chess_board):
                legal_moves.remove(move)
                print(
                    f"{chess_board.get_turn()} to move - {chess_board.san(move)} is black listed, trying another move!"
                )

            else:
                print(f"{chess_board.get_turn()} plays {chess_board.san(move)}")
                self.black_list_move(move, chess_board)
                selected_move = move

        """
        If the number of pieces on the board was reduced,
        all of the black listed moves can't happen again
        so the list can be cleared.
        """
        if chess_board.is_capture(selected_move):
            self.move_black_list.clear()

        return selected_move

    @abstractmethod
    def choose_move(self, legal_moves: list, chess_board: Board):
        pass

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
