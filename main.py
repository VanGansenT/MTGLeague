import tkinter as tk
from tkinter import ttk
from itertools import combinations
from PIL import Image, ImageTk

image_path = "resources/images/"
class LoadingScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Loading...")

        self.loading_width = 600
        self.loading_height = 600



        # Load your image for the loading screen
        self.loading_image = Image.open(image_path + "LoadingScreenMTG.jpg")
        self.loading_image = self.loading_image.resize((self.loading_width, self.loading_height))
        self.loading_photo = ImageTk.PhotoImage(self.loading_image)

        # Display the loading image
        self.loading_label = tk.Label(self.master, image=self.loading_photo)
        self.loading_label.pack()

        # After a certain delay, destroy the loading screen and start the main application
        self.master.after(3500, self.load_main_app)

    def load_main_app(self):
        self.loading_x = self.master.winfo_x()
        self.loading_y = self.master.winfo_y()

        self.loading_width = self.master.winfo_width()
        self.loading_height = self.master.winfo_height()

        self.master.destroy()
        self.root = tk.Tk()
        self.root.geometry(f"{self.loading_width}x{self.loading_height}+{self.loading_x}+{self.loading_y}")
        event_organizer = EventOrganizer(self.root)




class EventOrganizer:
    def __init__(self, master):
        self.master = master
        self.master.title("MTG LEAGUE")

        self.players = {}
        self.matches = []

        #self.setup_ui()
        self.create_tabs()

    def setup_ui(self, tab):

        self.add_player_ui(tab)

        self.add_matches_ui(tab)

        self.result_ui(tab)


    def add_player_ui(self, tab):
        self.player_label = tk.Label(tab, text="Player Name:")
        self.player_label.grid(row=0, column=0)

        self.player_entry = tk.Entry(tab)
        self.player_entry.grid(row=0, column=1)

        self.add_player_button = tk.Button(tab, text="Add Player", command=self.add_player)
        self.add_player_button.grid(row=0, column=2)

    def add_matches_ui(self,tab):
        self.match_label = tk.Label(tab, text="Match (Player1, Player2, ...):")
        self.match_label.grid(row=1, column=0)

        self.match_entry = tk.Entry(tab)
        self.match_entry.grid(row=1, column=1)

        self.winner_label = tk.Label(tab, text="Winner:")
        self.winner_label.grid(row=1, column=2)

        self.winner_entry = tk.Entry(tab)
        self.winner_entry.grid(row=1, column=3)

        self.add_match_button = tk.Button(tab, text="Add Match", command=self.add_match)
        self.add_match_button.grid(row=1, column=4)

    def result_ui(self,tab):
        display_results_button = tk.Button(tab, text="Display Results", command=self.display_results)
        display_results_button.grid(row=4, column=0, columnspan=5)
        display_results_button = tk.Button(tab, text="Suggest new matches",
                                           command=self.suggest_matches)
        display_results_button.grid(row=5, column=0, columnspan=5)



        self.result_label = tk.Label(tab, text="Results:")
        self.result_label.grid(row=2, column=0, columnspan=5)

        self.result_text = tk.Text(tab, height=10, width=50)
        self.result_text.grid(row=3, column=0, columnspan=5)
    def create_tabs(self):
        self.notebook = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text='All info')
        self.notebook.add(self.tab2, text='Add players')
        self.notebook.add(self.tab3, text='Add matches')
        self.notebook.add(self.tab4, text='Player scores')
        self.notebook.grid(row=0, column=0, sticky="nsew")


        # Add widgets to the tabs
        self.add_widgets_to_tab1()
        self.add_widgets_to_tab2()
        self.add_widgets_to_tab3()
        self.add_widgets_to_tab4()

    def add_widgets_to_tab1(self):
        # Widgets for the first tab
        #self.label1 = ttk.Label(self.tab1, text='Content for Tab 1')
        #self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.setup_ui(self.tab1)

    def add_widgets_to_tab2(self):

        self.add_player_ui(self.tab2)

    def add_widgets_to_tab3(self):

        self.add_matches_ui(self.tab3)

    def add_widgets_to_tab4(self):

        self.result_ui(self.tab4)

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
    root_loading = tk.Tk()
    loading_screen = LoadingScreen(root_loading)
    root_loading.mainloop()