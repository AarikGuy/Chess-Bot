import threading
import time
from accessors import LiChessAccessor
from bots import IChessBot


class LiChessProcessor:
    def __init__(
        self,
        lichess_accessor: LiChessAccessor.LiChessAccessor,
        chess_bot: IChessBot.IChessBot,
    ):
        self.lichess_accessor = lichess_accessor
        self.chess_bot = chess_bot

    # Starts the LIChessProcessor. This function should never end.
    def start(self):
        challenge_thread = threading.Thread(target=self.accept_incoming_challenges)
        games_thread = threading.Thread(target=self.handle_games)
        challenge_thread.join()
        games_thread.join()

    def accept_incoming_challenges(self):
        while True:
            challenges = self.lichess_accessor.get_challenges()
            incoming_challenges = challenges["in"]

            if len(incoming_challenges) == 0:
                time.sleep(0.05)
                continue

            for challenge in incoming_challenges:
                challenge_id = challenge.id
                self.lichess_accessor.accept_challenge(challenge_id=challenge_id)

    def handle_games(self):
        while True:
            games = self.lichess_accessor.get_ongoing_games()
