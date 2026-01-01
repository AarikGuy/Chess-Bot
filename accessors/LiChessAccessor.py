import json
import requests

SECRETS_PATH = "secrets.json"
LI_CHESS_TOKEN = "LiChessToken"
LI_CHESS_BASE_URL = "https://lichess.org/"


class LiChessAccessor:
    def __init__(self):
        secrets = None
        with open("secrets.json") as f:
            secrets = json.load(f)

        if secrets is None or LI_CHESS_TOKEN not in secrets:
            raise Exception(f"LiChess token could not be found in {SECRETS_PATH}")

        self.token = secrets[LI_CHESS_TOKEN]

    def get_challenges(self):
        response = requests.get(
            f"{LI_CHESS_BASE_URL}/api/challenge", headers={"Authorization": self.token}
        )

        if response.status_code != 200:
            raise Exception("Unable to fetch challenges from LiChess.")

        return response.json()

    def accept_challenge(self, challenge_id: str):
        response = requests.post(
            f"{LI_CHESS_BASE_URL}/api/challenge/{challenge_id}/accept",
            headers={"Authorization": self.token},
        )

        if response.status_code != 200:
            raise Exception(f"Unable to accept challenge {challenge_id}")

    def decline_challenge(self, challenge_id):
        response = requests.post(
            f"{LI_CHESS_BASE_URL}/api/challenge/{challenge_id}/decline",
            headers={"Authorization": self.token},
            data={"reason": "generic"},
        )

        if response.status_code != 200:
            raise Exception(f"Failed to decline challenge {challenge_id}")

    def make_move(self, game_id: str, move: str, offering_draw: bool):
        response = requests.post(
            f"{LI_CHESS_BASE_URL}/api/bot/game/{game_id}/move/{move}",
            headers={"Authorization": self.token},
            data={"offeringDraw": offering_draw},
        )

        if response.status_code != 200:
            raise Exception(f"Failed to push move {move} to game {game_id}")

    """
    Method that sends a message to the opposing player.
    Should be used for trash talk ;)
    """

    def send_message_async(self):
        pass
