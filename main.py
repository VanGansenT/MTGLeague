import tkinter as tk
from itertools import combinations

class EventOrganizer:
    def __init__(self, master):
        self.master = master
        self.master.title("1v1 Event Organizer")

        self.players = {}
        self.matches = []

        self.setup_ui()

    def setup_ui(self):
        self.player_label = tk.Label(self.master, text="Player Name:")
        self.player_label.grid(row=0, column=0)

        self.player_entry = tk.Entry(self.master)
        self.player_entry.grid(row=0, column=1)

        self.add_player_button = tk.Button(self.master, text="Add Player", command=self.add_player)
        self.add_player_button.grid(row=0, column=2)

        self.match_label = tk.Label(self.master, text="Match (Player1, Player2, ...):")
        self.match_label.grid(row=1, column=0)

        self.match_entry = tk.Entry(self.master)
        self.match_entry.grid(row=1, column=1)

        self.winner_label = tk.Label(self.master, text="Winner:")
        self.winner_label.grid(row=1, column=2)

        self.winner_entry = tk.Entry(self.master)
        self.winner_entry.grid(row=1, column=3)

        self.add_match_button = tk.Button(self.master, text="Add Match", command=self.add_match)
        self.add_match_button.grid(row=1, column=4)

        self.result_label = tk.Label(self.master, text="Results:")
        self.result_label.grid(row=2, column=0, columnspan=5)

        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.grid(row=3, column=0, columnspan=5)

    def add_player(self):
        player_name = self.player_entry.get()
        if player_name:
            if player_name not in self.players:
                self.players[player_name] = 0
                self.result_text.insert(tk.END, f"Added player: {player_name}\n")
            else:
                self.result_text.insert(tk.END, f"Player {player_name} already exists!\n")
        else:
            self.result_text.insert(tk.END, "Please enter a player name!\n")

    def add_match(self):
        match_str = self.match_entry.get()
        winner = self.winner_entry.get()
        if match_str:
            players = match_str.split(", ")
            if len(players) >= 2:
                valid_players = all(player in self.players for player in players)
                if valid_players:
                    if winner in players or winner == "":
                        self.matches.append((players, winner))  # Store match with winner
                        self.result_text.insert(tk.END, f"Added match: {', '.join(players)} - Winner: {winner}\n")
                        if winner:
                            for player in players:
                                if player == winner:
                                    self.players[player] += 1
                    else:
                        self.result_text.insert(tk.END, "Winner is not part of this match!\n")
                else:
                    self.result_text.insert(tk.END, "One or more players don't exist!\n")
            else:
                self.result_text.insert(tk.END, "A match needs at least 2 players!\n")
        else:
            self.result_text.insert(tk.END, "Please enter a match!\n")

    def display_results(self):
        self.result_text.delete(1.0, tk.END)
        for player, wins in self.players.items():
            self.result_text.insert(tk.END, f"{player}: {wins} wins\n")
        self.result_text.insert(tk.END, "\nMatches:\n")
        for i, (match_players, winner) in enumerate(self.matches):
            result_str = f"{', '.join(match_players)}"
            if winner:
                result_str += f" - Winner: {winner}"
            self.result_text.insert(tk.END, f"{i+1}. {result_str}\n")

    def suggest_matches(self):
        print('go fuck yourself')

if __name__ == "__main__":
    root = tk.Tk()
    event_organizer = EventOrganizer(root)
    display_results_button = tk.Button(root, text="Display Results", command=event_organizer.display_results)
    display_results_button.grid(row=4, column=0, columnspan=5)
    display_results_button = tk.Button(root, text="Suggest new matches", command=event_organizer.suggest_matches)
    display_results_button.grid(row=5, column=0, columnspan=5)
    root.mainloop()