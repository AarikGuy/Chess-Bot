import chess
import random


class ChessGame:

    def __init__(self):
        self.board = chess.Board()
        self.choose_color()
        self.bot = 

    def choose_color(self):
        color_picked = False

        while not color_picked:
            player_choice = input("Choose color (w/b/r): ")

            if player_choice == "r":
                print("""Randomly choosing who will go first...""")
                player_is_white = bool(random.getrandbits(1))
                player_choice = "w" if player_is_white else "b"

            if player_choice == "w":
                print("You will be going first, choose wisely!")
                self.color = chess.BLACK
                return

            if player_choice == "b":
                print("The bot will be starting the game. Prepare yourself!")
                self.color = chess.WHITE
                return
            
            print('You did not select a color! Try again: (w/b/r)')

     