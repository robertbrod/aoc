class Participant:
    def __init__(self, name = "", position = 0, stars = 0):
        self.name = name
        self.position = position
        self.stars = stars
        
    def to_json(self) -> dict:
        return {
            "name": self.name,
            "position": self.position,
            "stars": self.stars,
        }

    @staticmethod
    def load(data: dict):
        return Participant(data["name"], data["position"], data["stars"])