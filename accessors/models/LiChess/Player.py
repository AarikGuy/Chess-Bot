class Player:
    def __init__(self, response):
        self.id = response["id"]
        self.rating = response["rating"]
        self.username = response["username"]
