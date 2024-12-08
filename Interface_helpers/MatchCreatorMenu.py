import tkinter as tk
from PIL import Image, ImageTk
import os
import functools
import math

class MatchCreatorMenu:
    def __init__(self, organizer, master, row, column):
        self.organizer = organizer
        self.master = master
        self.match_label = tk.Label(master, text="Match (Player1, Player2, ...):")
        self.match_label.grid(row=row, column=column)

        self.match_entry = tk.Entry(master)
        self.match_entry.grid(row=row, column=column + 1)

        self.winner_label = tk.Label(master, text="Winner:")
        self.winner_label.grid(row=row, column=column + 2)

        self.winner_entry = tk.Entry(master)
        self.winner_entry.grid(row=row, column=column + 3)

        self.add_match_button = tk.Button(master, text="Add Match")
        self.add_match_button.grid(row=row, column=column + 4)

