import json

class PlayerObject:
    def __init__(self, name, image_path, victories=0):
        self.name = name
        self.imagePath = image_path
        self.victories = victories

    def get_name(self):
        return self.name
    
    def get_image_path(self):
        return self.imagePath

    def add_victory(self):
        self.victories += 1

    def __repr__(self):
        return f"Player(name={self.name}, victories={self.victories})"

    def to_dict(self):
        return {
            "name": self.name,
            "imagePath": self.imagePath,
            "victories": self.victories
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return f"Player(name={self.name}, victories={self.victories})"
