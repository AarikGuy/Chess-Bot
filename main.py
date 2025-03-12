from chess import WHITE, BLACK
from ChessGame import ChessGame
from Level1ChessBot import Level1ChessBot

bot = Level1ChessBot()
chess_game = ChessGame(bot, bots_color=WHITE)

chess_game.play_game()
