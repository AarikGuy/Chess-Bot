class Player:
    def __init__(self, response):
        self.id = response["id"]
        self.rating = response["rating"]
        if "name" in response:
            self.name = response["name"]

        if "username" in response:
            self.username = response["username"]
