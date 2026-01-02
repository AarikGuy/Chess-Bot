from accessors.models.LiChess import Player, Variant, TimeControl, Perf


class Challenge:
    def __init__(self, response):
        self.id = response["id"]
        self.url = response["url"]
        self.status = response["status"]
        self.challenger = Player.Player(response["challenger"])
        self.dest_user = Player.Player(response["destUser"])
        self.variant = Variant.Variant(response["variant"])
        self.rated = response["rated"]
        self.speed = response["speed"]
        self.time_control = TimeControl.TimeControl(response["timeControl"])
        self.color = response["color"]
        self.final_color = response["finalColor"]
        self.perf = Perf.Perf(response["perf"])
        self.direction = response["direction"]
