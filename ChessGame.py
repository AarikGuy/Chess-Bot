from chess import Move, Board, WHITE, BLACK
import random
from bots.IChessBot import IChessBot

class ChessGame:
    def set_up_board(self):
        self.moves = []

        '''
        Pre programmed moves that both sides
        will start with. Useful for debugging
        '''
        self.white_initial_moves = []
        self.black_initial_moves = []

    def __init__(self, chess_bot: IChessBot, bots_color: bool = None):
        self.board = Board()
        self.bots_color = self.choose_color() if bots_color is None else bots_color
        self.bot = chess_bot

        self.set_up_board()

    def __init__(self, white_bot: IChessBot, black_bot: bool):
        self.board = Board()
        self.white_bot = white_bot
        self.black_bot = black_bot
        self.set_up_board()
        self.last_to_move = WHITE

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

    def have_bots_play(self):
        while not self.is_game_over():
            while (
                self.board.turn == WHITE and not self.is_game_over()
            ):
                self.last_to_move = WHITE

                # Use white's pre programmed moves before using bot's choosing logic.
                if self.push_debug_moves():
                    continue

                move = self.white_bot.generate_move(self.board)
                self.board.push(move)
                self.moves.insert(len(self.moves), str(move))

            while self.board.turn == BLACK and not self.is_game_over():
                self.last_to_move = BLACK
                
                # Use white's pre programmed moves before using bot's choosing logic.
                if self.push_debug_moves():
                    continue

                move = self.black_bot.generate_move(self.board)
                self.board.push(move)
                self.moves.insert(len(self.moves), str(move))

        start_board = Board()

        # Print out the game that was played by the two bots.
        print(start_board.variation_san(
            [Move.from_uci(m) for m in self.moves]))
        print(f"{self.get_winner_of_last_game()}")

        return self.last_to_move

    '''
    Works out the outcome of the chess game.
    Throws an exception if the status there's
    no clear ending to the game or the game 
    is in progress.
    '''
    def get_winner_of_last_game(self):
        if (not self.board.is_game_over()):
            raise Exception("Can't get the game outcome for a game that is not over!")

        if (self.board.is_stalemate() or self.board.is_insufficient_material()):
            return "Draw!"

        if (not self.board.is_checkmate):
            raise Exception("Can't determine the outcome of the game in it's current state!")

        if (self.last_to_move == WHITE):
            return "White won!"

        return "Black won!"

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
        if self.board.turn == WHITE and len(self.white_initial_moves) > 0:
            move = self.white_initial_moves.pop(0)
            self.board.push_san(move)
            self.moves.insert(len(self.moves), str(self.board.peek()))

            return True

        if self.board.turn == BLACK and len(self.black_initial_moves) > 0:
            move = self.black_initial_moves.pop(0)
            self.board.push_san(move)
            self.moves.insert(len(self.moves), str(self.board.peek()))

            return True

        return False
