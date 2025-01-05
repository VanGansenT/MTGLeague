import tkinter as tk
from PIL import Image, ImageTk
import os
import functools
import math


class MatchCreatorMenu:
    def __init__(self, organizer, master, row, column):
        self.organizer = organizer
        self.master = master
        self.player1 = PlayerSelector(organizer, master, "Player 1", row, column)
        self.player2 = PlayerSelector(organizer, master, "Player 2", row, column + 1)

class PlayerSelector:
    def __init__(self, organizer, master, playerName, row, column):
        self.match_label = tk.Label(master, text=playerName)
        self.match_label.grid(row=row, column=column)
        pass

class MatchObject:
    def __init__(self, organizer, master, image_path, row, column):
        pass

