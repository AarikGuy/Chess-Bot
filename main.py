from chess import WHITE, BLACK
from ChessGame import ChessGame
from DoorMatChessBot import DoorMatChessBot

bot = DoorMatChessBot()
chess_game = ChessGame(bot)

chess_game.play_game()
