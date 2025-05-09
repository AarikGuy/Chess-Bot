from chess import Move, Board, WHITE, BLACK
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

    def __init__(self, white_bot: IChessBot, black_bot: bool):
        self.board = Board()
        self.white_bot = white_bot
        self.black_bot = black_bot

    def choose_color(self):

        color_picked = False

        while True:

            # player_choice = input("Choose color (w/b/r): ")

            player_choice = "w"

            if player_choice == "r":

                print("""Randomly choosing who will go first...""")

                player_is_white = bool(random.getrandbits(1))

                player_choice = "w" if player_is_white else "b"

            if player_choice == "w":

                print("You will be going first, choose wisely!")

                self.bots_color = BLACK

                return BLACK

            if player_choice == "b":

                print("The bot will be starting the game. Prepare yourself!")

                self.bots_color = WHITE

                return WHITE

            print("You did not select a color! Try again: (w/b/r)")

        raise Exception("No color was selected.")

    def have_bots_play(self):
        WHITE_MOVES = []
        BLACK_MOVES = []
        turn_count = 1
        moves = []

        while not self.board.is_checkmate():

            while (
                self.board.turn == WHITE and not self.board.is_checkmate()
            ):
                if len(WHITE_MOVES) > 0:
                    move = WHITE_MOVES.pop(0)
                    self.board.push_san(move)
                    continue

                move = self.white_bot.generate_move(self.board)

                self.board.push(move)

                print(f"""The white bot has played: {str(move)}, your move!""")

                moves.insert(len(moves), str(move))

            while self.board.turn == BLACK and not self.board.is_checkmate():

                if len(BLACK_MOVES) > 0:

                    move = BLACK_MOVES.pop(0)

                    self.board.push_san(move)

                    continue

                move = self.black_bot.generate_move(self.board)

                self.board.push(move)

                print(f"""The black bot has played: {str(move)}, your move!""")
                moves.insert(len(moves), str(move))
        start_board = Board()
        print(start_board.variation_san(
            [Move.from_uci(m) for m in moves]))

    def play_against_bot(self):

        WHITE_MOVES = ["d4", "Bf4", "Nf3", "e3", "Bd3", "Bd6+"]

        BLACK_MOVES = ["d5", "Bf5", "Nf6", "e6", "Bd6"]

        while not self.board.is_checkmate():
            while (
                not self.board.turn == self.bots_color and not self.board.is_checkmate()
            ):

                if self.bots_color == WHITE and len(BLACK_MOVES) > 0:
                    move = BLACK_MOVES.pop(0)
                    self.board.push_san(move)
                    continue

                if self.bots_color == BLACK and len(WHITE_MOVES) > 0:
                    move = WHITE_MOVES.pop(0)
                    self.board.push_san(move)
                    continue

                players_color = "black" if self.bots_color == WHITE else "white"

                legal_moves = [
                    self.board.san(move) for move in list(self.board.legal_moves)
                ]
                print(
                    f"""Choose from {players_color}'s legal moves: {str(legal_moves)}"""
                )

                player_move = input("Your move: ")

                if player_move in legal_moves:

                    self.board.push_san(player_move)

                else:

                    print("""No valid move was selected pick again!""")

            while self.board.turn == self.bots_color and not self.board.is_checkmate():

                if self.bots_color == WHITE and len(WHITE_MOVES) > 0:

                    move = WHITE_MOVES.pop(0)

                    self.board.push_san(move)

                    continue

                if self.bots_color == BLACK and len(BLACK_MOVES) > 0:

                    move = BLACK_MOVES.pop(0)

                    self.board.push_san(move)

                    continue

                move = self.bot.generate_move(self.board)

                self.board.push(move)

                print(f"""The bot has played: {str(move)}, your move!""")

        print("GAME OVER!")

        print(str(self.board.result))
