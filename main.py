from chess import WHITE, BLACK
from ChessGame import ChessGame
from bots.DoorMatChessBot import DoorMatChessBot
from bots.DunceFishChessBot import DunceFishChessBot

white_bot = DunceFishChessBot(ply_cutoff=2)
black_bot = DunceFishChessBot(ply_cutoff=1)

chess_game = ChessGame(white_bot, black_bot)
chess_game.have_bots_play()