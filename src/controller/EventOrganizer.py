import tkinter as tk
from tkinter import ttk
# Import the tkinter font module
import tkinter.font as tkFont
from PIL import Image, ImageTk
import logging


from src.models.MatchObject import MatchObject
from src.controller.ProfileCreatorMenu import ProfileCreatorMenu
from src.controller.MatchCreatorMenu import MatchCreatorMenu
from src.models.PlayerObject import PlayerObject
from src.views.PlayerView import PlayerView
from src.views.MatchView import MatchView

image_path = "resources/images/"


class EventOrganizer:
    def __init__(self, master):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.image_cache = []
        self.master = master
        self.master.title("MTG LEAGUE")

        self.player_data_label = []
        self.match_data_label = []

        self.players = {}
        self.matches = {}

        self.notebook = ttk.Notebook(self.master)

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
            player_object = PlayerView(tab, self.players[player], row + i, column)
            self.player_data_label.append(player_object)
            i += 1
    
    def match_database_ui(self, tab, row, column):
        self.match_data_label.clear()

        # Create a bold font
        bold_font = tkFont.Font(weight="bold")

        # Create title label with bold text
        label = tk.Label(tab, text="Matches:", font=bold_font)
        label.grid(row=row, column=column)

        # Go over every player and create a label for it
        i = 1
        for match in self.matches.keys():
            match_object = MatchView(tab, self.matches[match], row + i, column)
            self.match_data_label.append(match_object)
            i += 1

    def create_tabs(self):
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text='Add players')
        self.notebook.add(self.tab2, text='Add matches')
        self.notebook.add(self.tab3, text='Player scores')
        self.notebook.add(self.tab4, text='No bitches')
        self.notebook.grid(row=0, column=0, sticky="nsew")

        # Add widgets to the tabs
        self.add_widgets()

    def add_widgets(self):
        self.add_player_menu(self.tab1)
        self.match_creator_menu(self.tab2)
        self.player_scores_menu(self.tab3)
        self.no_bitches_menu(self.tab4)

    def update_tabs(self):
        current_tab = self.notebook.select()
        self.add_widgets()
        self.notebook.select(current_tab)


    def add_player_menu(self, tab):
        ProfileCreatorMenu(self, tab, "resources/images/profile", 0, 0)
        self.player_database_ui(tab,1,0)

    def match_creator_menu(self, tab):
        MatchCreatorMenu(self, tab, 0, 0)
        self.match_database_ui(tab,1,0)
        
    def player_scores_menu(self,tab):
        pass

    def no_bitches_menu(self,tab):

        (_, window_height) = self.get_window_size()
        loading_image = Image.open(image_path + "Nobitches.jpg")

        wpercent = (window_height / float(loading_image.size[1]))
        wsize = int((float(loading_image.size[1]) * float(wpercent)))
        loading_image = loading_image.resize((window_height, wsize))

        self.loading_photo = ImageTk.PhotoImage(loading_image)
        self.no_bitches_label = tk.Label(tab, image=self.loading_photo)
        self.no_bitches_label.grid(row=0, column=0)

    def add_player(self, player_name, profile_image):
        player_added = False
        if player_name and profile_image:
            if player_name not in self.players:
                self.players[player_name] = PlayerObject(player_name, profile_image)
                logging.info("player name is " + self.players[player_name].name)
                logging.info("Player profile image is " + self.players[player_name].imagePath)
                player_added = True

                self.update_tabs()

        return player_added
    
    def player_exists(self, player_name):
        return player_name in self.players
    
    def get_player(self, player_name):
        if self.player_exists(player_name):
            return self.players[player_name]
        else:
            return None
    
    def add_match(self, player1, player2):
        match_added = False
        if self.player_exists(player1) and self.player_exists(player2):
            playerObject1 = self.get_player(player1)
            playerObject2 = self.get_player(player2)
            match = MatchObject(playerObject1, playerObject2)
            self.matches[match.get_match_id()] = match
            match_added = True
            self.update_tabs()

        return match_added
    
    def get_players(self):
        return self.players
