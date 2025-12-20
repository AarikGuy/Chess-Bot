from chess import WHITE, BLACK
from ChessGame import ChessGame
from bots.DoorMatChessBot import DoorMatChessBot
from bots.DunceFishChessBot import DunceFishChessBot

# bot = DoorMatChessBot()
# bot = DunceFishChessBot(3)

white_bot = DoorMatChessBot()
black_bot = DunceFishChessBot(ply_cutoff=1, random_move_frequency=5)
# black_bot = DunceFishChessBot(ply_cutoff=2, random_move_frequency=5)

chess_game = ChessGame(white_bot, black_bot)
chess_game.have_bots_play()
# chess_game.play_against_bot()
