from chess import Board 

def get_turn(self: Board):
    if self.turn:
        return "White"
    
    return "Black"

Board.get_turn = get_turn
