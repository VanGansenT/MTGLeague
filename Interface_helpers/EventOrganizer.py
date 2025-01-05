import tkinter as tk
from tkinter import ttk
# Import the tkinter font module
import tkinter.font as tkFont
from PIL import Image, ImageTk


from Interface_helpers.ProfileCreatorMenu import ProfileCreatorMenu
from Interface_helpers.MatchCreatorMenu import MatchCreatorMenu
from Interface_helpers.PlayerObject import PlayerObject

image_path = "resources/images/"


class EventOrganizer:
    def __init__(self, master):
        self.image_cache = []
        self.master = master
        self.master.title("MTG LEAGUE")

        self.player_data_label = []

        self.players = {}
        self.matches = []

        # self.setup_ui()
        self.create_tabs()

    def get_window_size(self):
        # Update the window to ensure correct width measurement
        self.master.update_idletasks()

        # Get the width of the window
        window_height = self.master.winfo_height()
        window_width = self.master.winfo_width()
        return (window_height, window_width)

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

    def add_player_ui2(self, tab):
        (window_width, window_height) = self.get_window_size()

        # Create a black background
        black_background = tk.Canvas(tab, bg="black", width=window_width, height=window_height)
        black_background.grid(row=0, column=0, sticky="nsew")

        # Create a frame for the profile selector UI
        profile_frame = tk.Frame(tab, bg="white")
        profile_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Player Name Label
        player_label = tk.Label(profile_frame, text="Player Name:", bg="white", font=("Helvetica", 12))
        player_label.grid(row=0, column=1, padx=5, pady=5)

        # Player Name Entry with rounded corners and light gray background
        player_entry = tk.Entry(profile_frame, bg="#F0F0F0", bd=2, relief=tk.GROOVE)
        player_entry.grid(row=0, column=2, padx=5, pady=5)

        # Add Player Button with rounded corners and gradient background
        add_player_button = tk.Button(profile_frame, text="Add Player", command=self.add_player,
                                      bg="#4CAF50", fg="white", bd=2, relief=tk.GROOVE, font=("Helvetica", 10),
                                      activebackground="#45a049", activeforeground="white")
        add_player_button.grid(row=0, column=3, padx=5, pady=5, ipadx=10)

    def add_matches_ui(self, tab):
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

    def result_ui(self, tab):
        display_results_button = tk.Button(tab, text="Display Results", command=self.display_results)
        display_results_button.grid(row=4, column=0, columnspan=5)
        display_results_button = tk.Button(tab, text="Suggest new matches",
                                           command=self.suggest_matches)
        display_results_button.grid(row=5, column=0, columnspan=5)

        self.result_label = tk.Label(tab, text="Results:")
        self.result_label.grid(row=2, column=0, columnspan=5)

        self.result_text = tk.Text(tab, height=10, width=50)
        self.result_text.grid(row=3, column=0, columnspan=5)

    def player_database_ui(self, tab, row, column):

        self.player_data_label.clear()  # Removes references to previous labels

        # Create a bold font
        bold_font = tkFont.Font(weight="bold")

        # Create title label with bold text
        label = tk.Label(tab, text="Players:", font=bold_font)
        label.grid(row=row, column=column)

        # Go over every player and create a label for it
        i = 1
        for player in self.players.keys():
            # Create and add a new PlayerObject
            player_object = PlayerObject(self, tab, player, row + i, column)
            self.player_data_label.append(player_object)
            i += 1

    def create_tabs(self):
        self.notebook = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)
        self.tab5 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text='All info')
        self.notebook.add(self.tab2, text='Add players')
        self.notebook.add(self.tab3, text='Add matches')
        self.notebook.add(self.tab4, text='Player scores')
        self.notebook.add(self.tab5, text='No bitches')
        self.notebook.grid(row=0, column=0, sticky="nsew")

        # Add widgets to the tabs
        self.add_widgets_to_tab1()
        self.add_widgets_to_tab2()
        self.add_widgets_to_tab3()
        self.add_widgets_to_tab4()
        self.add_widgets_to_tab5()

    def add_widgets_to_tab1(self):
        # Widgets for the first tab
        # self.label1 = ttk.Label(self.tab1, text='Content for Tab 1')
        # self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.setup_ui(self.tab1)

    def add_widgets_to_tab2(self):

        # self.add_player_ui(self.tab2)
        # self.add_player_ui2(self.tab2)
        ProfileCreatorMenu(self, self.tab2, "resources/images/profile", 0, 0)
        self.player_database_ui(self.tab2,1,0)

    def add_widgets_to_tab3(self):
        MatchCreatorMenu(self, self.tab3, 0, 0)
        # ProfileSelectorMenu(self, self.tab2, "resources/images/profile", 0, 0)
        # self.player_database_ui(self.tab2,1,0)
        # self.add_matches_ui(self.tab3)

    def add_widgets_to_tab4(self):

        self.result_ui(self.tab4)

    def add_widgets_to_tab5(self):

        # Get the height of the window
        (_, window_height) = self.get_window_size()
        # Load the image
        loading_image = Image.open(image_path + "Nobitches.jpg")

        # Resize the image to fit the window width while maintaining aspect ratio
        wpercent = (window_height / float(loading_image.size[1]))
        wsize = int((float(loading_image.size[1]) * float(wpercent)))
        loading_image = loading_image.resize((window_height, wsize))

        # Convert image to PhotoImage
        self.loading_photo = ImageTk.PhotoImage(loading_image)

        # Display the loading image
        self.no_bitches_label = tk.Label(self.tab5, image=self.loading_photo)
        self.no_bitches_label.grid(row=0, column=0)

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

    def add_player(self, player_name, profile_image):
        player_added = False
        if player_name and profile_image:
            if player_name not in self.players:
                # Set up the player
                self.players[player_name] = {"name": player_name, "profile_image": profile_image}
                print("player name is " + self.players[player_name]["name"])
                print("Player profile image is " + self.players[player_name]["profile_image"])
                player_added = True
                #Updata label database
                self.player_database_ui(self.tab2,1,0)

        return player_added

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
            self.result_text.insert(tk.END, f"{i + 1}. {result_str}\n")

    def suggest_matches(self):
        print('go fuck yourself')
