import tkinter as tk
from PIL import Image, ImageTk
import os
import functools
import math


class MatchCreatorMenu:
    def __init__(self, organizer, master, row, column):
        self.organizer = organizer
        self.master = master
        # self.player1 = PlayerSelector(organizer, master, "Player 1", row, column)
        # self.player2 = PlayerSelector(organizer, master, "Player 2", row, column + 1)

    def close_player_selector(self):
        if self.profile_selector is not None:
            self.profile_selector.destroy()
            self.profile_selector = None

class PlayerSelector:
    def __init__(self, player_selector_controller, row, column):
        self.master = tk.Toplevel()
        self.master.title("player selection")
        self.controller = player_selector_controller
        # self.playerObjects = playerObjects



        # Bind the close_window() function to the WM_DELETE_WINDOW event
        self.master.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):
        self.controller.close_player_selector()

class MatchObject:
    def __init__(self, organizer, master, image_path, row, column):
        pass
