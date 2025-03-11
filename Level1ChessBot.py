from chess import Board
from IChessBot import IChessBot

class Level1ChessBot(IChessBot):

    def __init__(self):
        self.ply_cutoff = 1

    def __init__(self, ply_cutoff):
        self.ply_cutoff = ply_cutoff

    def generate_move(self, chess_board: Board) -> Board:
        if chess_board.is_checkmate():
            raise Exception("Can't generate move on a completed game.")

        legal_moves_copy = chess_board.legal_moves.copy()

        for legal_move in legal_moves_copy:
            chess_board.push_san(legal_move)

            if self.ply_cutoff > 1
            
    def get_max_move(self, chess_board)