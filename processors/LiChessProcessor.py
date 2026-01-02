import logging
import threading
import time
import concurrent.futures
from accessors import LiChessAccessor
from bots import IChessBot, DunceFishChessBot
from chess import Board


class LiChessProcessor:
    def __init__(
        self,
        lichess_accessor: LiChessAccessor.LiChessAccessor,
        logger: logging.Logger,
        number_of_workers: int = 4,
    ):
        self.lichess_accessor = lichess_accessor
        self.number_of_workers = number_of_workers
        self.logger = logger

    # Starts the LIChessProcessor. This function should never end.
    def start(self):
        challenge_thread = threading.Thread(target=self.accept_incoming_challenges)
        games_thread = threading.Thread(target=self.handle_games)
        challenge_thread.start()
        games_thread.start()

        # This code should never be reached, the bot should never stop accepting challenges and playing games.
        challenge_thread.join()
        games_thread.join()

    def accept_incoming_challenges(self):
        challenges = self.lichess_accessor.get_challenges()
        incoming_challenges = challenges.incoming_challenges
        for challenge in incoming_challenges:
            self.lichess_accessor.decline_challenge(challenge_id=challenge.id)

        while True:
            challenges = self.lichess_accessor.get_challenges()
            incoming_challenges = challenges.incoming_challenges

            if len(incoming_challenges) == 0:
                time.sleep(10)
                continue

            for challenge in incoming_challenges:
                challenge_id = challenge.id
                self.logger.info(f"Accepting challenge: {challenge_id}")
                self.lichess_accessor.accept_challenge(challenge_id=challenge_id)

            time.sleep(10)

    def handle_games(self):
        while True:
            games = self.lichess_accessor.get_ongoing_games()
            games_where_its_my_turn = list(filter(lambda game: game.is_my_turn, games))

            for game in games_where_its_my_turn:
                board = Board(fen=game.fen)
                bot = DunceFishChessBot.DunceFishChessBot(2, game.color, 0)
                move = bot.generate_move(board)

                self.lichess_accessor.make_move(game.game_id, str(move), False)
