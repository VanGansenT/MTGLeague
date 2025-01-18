class PlayerObject:
    def __init__(self, name, image_path, victories=0):
        self.name = name
        self.imagePath = image_path
        self.victories = victories

    def add_victory(self):
        self.victories += 1

    def __repr__(self):
        return f"Player(name={self.name}, victories={self.victories})"
