import chess
import random
from IChessBot import IChessBot


class ChessGame:

    def __init__(self, chess_bot: IChessBot):
        self.board = chess.Board()
        self.bots_color = choose_color()
        self.bot = chess_bot

    def choose_color(self):
        color_picked = False

        while True:
            player_choice = input("Choose color (w/b/r): ")

            if player_choice == "r":
                print("""Randomly choosing who will go first...""")
                player_is_white = bool(random.getrandbits(1))
                player_choice = "w" if player_is_white else "b"

            if player_choice == "w":
                print("You will be going first, choose wisely!")
                return chess.BLACK

            if player_choice == "b":
                print("The bot will be starting the game. Prepare yourself!")
                self.chess_color = chess.WHITE
                return chess.White

            print("You did not select a color! Try again: (w/b/r)")

        raise Exception("No color was selected.")

    def play_game(self):
        while not self.board.is_checkmate():
            while not self.board.turn == self.bots_color:
                print(
                    f"""Choose from {self.bots_color}'s legal moves: {self.board.legal_moves}"""
                )
                player_move = input("Your move: ")

                if player_move in self.board.legal_moves:
                    self.board.push(player_move)
                else:
                    print("""No valid move was selected pick again!""")

            while self.board.turn == self.bots_color:
                move = self.bot.generate_move(self.board)
                self.board.push(move)
                print(f"""The bot has played: {move}, your move!""")
