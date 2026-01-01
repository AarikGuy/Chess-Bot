import Challenge


class ChallengeList:
    def __init__(self, response):
        self.incoming_challenges = []
        self.outgoing_challenges = []

        incoming_challenges = response["in"]
        for incoming_challenge in incoming_challenges:
            challenge = Challenge.Challenge(incoming_challenge)
            self.incoming_challenges.append(challenge)

        outgoing_challenges = response["out"]
        for outgoing_challenge in outgoing_challenges:
            challenge = Challenge.Challenge(outgoing_challenge)
            self.outgoing_challenges.append(challenge)
