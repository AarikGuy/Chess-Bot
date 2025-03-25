from chess import WHITE, BLACK
from ChessGame import ChessGame
from DoorMatChessBot import DoorMatChessBot
from DunceFishChessBot import DunceFishChessBot

# bot = DoorMatChessBot()
bot = DunceFishChessBot(3)
chess_game = ChessGame(bot)

chess_game.play_game()
