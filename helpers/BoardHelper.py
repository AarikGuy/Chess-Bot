from chess import Board 

NUMBER_OF_STARTING_PIECES = 32

def get_turn(self: Board):
    if self.turn:
        return "White"
    
    return "Black"

def get_number_of_peices(self: Board):
    return len(self.pieces)

Board.get_turn = get_turn
Board.get_number_of_pieces = get_number_of_peices
