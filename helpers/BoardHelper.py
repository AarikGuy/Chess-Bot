from chess import Board 

NUMBER_OF_STARTING_PIECES = 32

def get_turn(self: Board):
    if self.turn:
        return "White"
    
    return "Black"

def get_number_of_peices(self: Board):
    return len(self.pieces)

def get_legal_moves(self: Board):
    return list(self.legal_moves)

Board.get_turn = get_turn
Board.get_number_of_pieces = get_number_of_peices
Board.get_legal_moves = get_legal_moves
