import logging
import uuid

from src.models.PlayerObject import PlayerObject

class MatchObject:
    def __init__(self, player1: PlayerObject, player2: PlayerObject):
        self.match_id = str(uuid.uuid4())
        self.player1 = player1
        self.player2 = player2
        self.player1Name = player1.get_name()
        self.player2Name = player2.get_name()
        self.scores = {self.player1Name: 0, self.player2Name: 0} 
        self.victorious_player = "Neutral" 

    def set_victorious(self, player):
        self.set_score(player, 2)

    def get_match_id(self):
        return self.match_id

    def set_score(self, player, score):
        if player not in self.scores:
            raise ValueError("Player must be one of the participating players")
        self.scores[player] = score

    def is_draw(self):
        return self.scores[self.player1Name] == self.scores[self.player2Name]

    def print_match_result(self) -> str:
        if self.is_draw():
            logging.info(f"Match between {self.player1Name} and {self.player2Name} is ongoing or is a draw.")
        else:
            logging.info(f"{self.get_winning_player()} won the match.")
    
    def get_winning_player(self):
        if(self.is_draw()):
            return None
        return max(self.scores, key=self.scores.get)
