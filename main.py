from chess import WHITE, BLACK
from ChessGame import ChessGame
from DoorMatChessBot import DoorMatChessBot
from DunceFishChessBot import DunceFishChessBot

# bot = DoorMatChessBot()
# bot = DunceFishChessBot(3)

# white_bot = DoorMatChessBot()
white_bot = DunceFishChessBot(1)
black_bot = DunceFishChessBot(3)

chess_game = ChessGame(white_bot, black_bot)
chess_game.have_bots_play()
# chess_game.play_against_bot()
