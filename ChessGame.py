from chess import Move, Board, WHITE, BLACK
import random
from bots.IChessBot import IChessBot

class ChessGame:
    def set_up_board(self):
        self.moves = []
        self.white_debug_moves = ["d4", "Bf4", "Nf3", "e3", "Bd3", "Bd6+"]
        self.black_debug_moves = ["d5", "Bf5", "Nf6", "e6", "Bd6"]

    def __init__(self, chess_bot: IChessBot, bots_color: bool = None):
        self.board = Board()

        if bots_color is None:
            self.bots_color = self.choose_color()
        else:
            self.bots_color = bots_color
        self.bot = chess_bot

        self.set_up_board()

    def __init__(self, white_bot: IChessBot, black_bot: bool):
        self.board = Board()
        self.white_bot = white_bot
        self.black_bot = black_bot
        self.set_up_board()

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
                self.bots_color = BLACK

                return BLACK

            if player_choice == "b":
                print("The bot will be starting the game. Prepare yourself!")
                self.bots_color = WHITE

                return WHITE

            print("You did not select a color! Try again: (w/b/r)")

        raise Exception("No color was selected.")

    def have_bots_play(self):
        turn_count = 1
        last_to_move = WHITE

        while not self.is_game_over():
            while (
                self.board.turn == WHITE and not self.is_game_over()
            ):
                last_to_move = WHITE

                if self.push_debug_moves():
                    continue

                move = self.white_bot.generate_move(self.board)
                self.board.push(move)
                self.moves.insert(len(self.moves), str(move))

            while self.board.turn == BLACK and not self.is_game_over():
                last_to_move = BLACK
                if self.push_debug_moves():
                    continue

                move = self.black_bot.generate_move(self.board)
                self.board.push(move)
                self.moves.insert(len(self.moves), str(move))

        start_board = Board()

        print(start_board.variation_san(
            [Move.from_uci(m) for m in self.moves]))
        
        winner = "White" if last_to_move == WHITE else "Black"
        print(f"{winner} wins!")

        return last_to_move

    def play_against_bot(self):
        while not self.is_game_over():
            while (
                not self.board.turn == self.bots_color and not self.is_game_over()
            ):
                if self.push_debug_moves():
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

            while self.board.turn == self.bots_color and not self.is_game_over():
                if self.push_debug_moves():
                    continue

                move = self.bot.generate_move(self.board)
                self.board.push(move)
                print(f"""The bot has played: {str(move)}, your move!""")

        print("GAME OVER!")
        print(str(self.board.result))

    def is_game_over(self):
        return self.board.is_checkmate() or self.board.is_stalemate() or len(list(self.board.legal_moves)) == 0

    def push_debug_moves(self):
        if self.board.turn == WHITE and len(self.white_debug_moves) > 0:
            move = self.white_debug_moves.pop(0)
            self.board.push_san(move)
            self.moves.insert(len(self.moves), str(self.board.peek()))

            return True

        if self.board.turn == BLACK and len(self.black_debug_moves) > 0:
            move = self.black_debug_moves.pop(0)
            self.board.push_san(move)
            self.moves.insert(len(self.moves), str(self.board.peek()))

            return True

        return False
