import logging

class MatchObject:
    def __init__(self, player1: str, player2: str):
        self.player1 = player1
        self.player2 = player2
        self.scores = {player1: 0, player2: 0} 
        self.victorious_player = "Neutral" 

    def set_victorious(self, player):
        self.set_score(player, 2)

    def set_score(self, player, score):
        if player not in self.scores:
            raise ValueError("Player must be one of the participating players")
        self.scores[player] = score

    def is_draw(self):
        return self.scores[self.player1] == self.scores[self.player2]

    def print_match_result(self) -> str:
        if self.is_draw():
            logging.info(f"Match between {self.player1} and {self.player2} is ongoing or is a draw.")
        else:
            logging.info(f"{self.get_winning_player()} won the match.")
    
    def get_winning_player(self):
        if(self.is_draw()):
            return None
        return max(self.scores, key=self.scores.get)
