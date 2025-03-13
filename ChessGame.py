from chess import Board, WHITE, BLACK
import random
from IChessBot import IChessBot


class ChessGame:

    def __init__(self, chess_bot: IChessBot, bots_color: bool = None):
        self.board = Board()

        if bots_color is None:
            self.bots_color = self.choose_color()
        else:
            self.bots_color = bots_color

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
                return BLACK

            if player_choice == "b":
                print("The bot will be starting the game. Prepare yourself!")
                return WHITE

            print("You did not select a color! Try again: (w/b/r)")

        raise Exception("No color was selected.")

    def play_game(self):
        while not self.board.is_checkmate():
            while (
                not self.board.turn == self.bots_color and not self.board.is_checkmate()
            ):

                bots_color = "black" if self.bots_color == WHITE else "white"
                legal_moves = [
                    self.board.san(move) for move in list(self.board.legal_moves)
                ]
                print(f"""Choose from {bots_color}'s legal moves: {str(legal_moves)}""")
                player_move = input("Your move: ")

                if player_move in legal_moves:
                    self.board.push_san(player_move)
                else:
                    print("""No valid move was selected pick again!""")

            while self.board.turn == self.bots_color and not self.board.is_checkmate():
                move = self.bot.generate_move(self.board)
                self.board.push(move)
                print(f"""The bot has played: {str(move)}, your move!""")

        print("GAME OVER!")
        print(str(self.board.result))
