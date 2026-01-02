from chess import BLACK, WHITE
from accessors.models.LiChess import Player, Variant


class Game:
    def __init__(self, response):
        self.game_id = response["gameId"]
        self.full_id = response["fullId"]

        if response["color"] == "white":
            self.color = WHITE
        else:
            self.color = BLACK

        self.fen = response["fen"]
        self.has_moved = response["hasMoved"]
        self.is_my_turn = response["isMyTurn"]
        self.last_move = response["lastMove"]
        self.opponent = Player.Player(response["opponent"])
        self.perf = response["perf"]
        self.rated = response["rated"]
        if "secondsLeft" in response:
            self.seconds_left = response["secondsLeft"]
        self.source = response["source"]
        self.speed = response["speed"]
        self.variant = Variant.Variant(response["variant"])
