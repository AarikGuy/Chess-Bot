import json

SECRETS_PATH = "secrets.json"
LI_CHESS_TOKEN = "LiChessToken"


class LiChessAccessor:
    def __init__(self):
        self.base_url = "TODO replace w/ base url"

        secrets = None
        with open("secrets.json") as f:
            secrets = json.load(f)

        if secrets is None or LI_CHESS_TOKEN not in secrets:
            raise Exception(f"LiChess token could not be found in {SECRETS_PATH}")

        self.token = secrets[LI_CHESS_TOKEN]

    def get_challenges_async(self):
        pass

    def accept_challenge_async(self):
        pass

    """
    Method that sends a message to the opposing player.
    Should be used for trash talk ;)
    """

    def send_message_async(self):
        pass
