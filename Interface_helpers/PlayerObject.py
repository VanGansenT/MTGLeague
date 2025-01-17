import tkinter as tk
from PIL import Image, ImageTk
import os
import functools
import math
import tkinter.font as tkFont

class PlayerObject:
    def __init__(self, organizer, master, player, row, column):
        # Define default and hover background colors
        self.default_bg = "#d3d3d3"  # Light gray
        self.hover_bg = "#c0c0c0"    # Slightly darker gray for hover

        # Create a frame with a 3D appearance
        self.frame = tk.Frame(
            master,
            bg=self.default_bg,
            padx=5,
            pady=5,
            relief="raised",
            bd=2
        )
        self.frame.grid(row=row, column=column, columnspan=2, sticky="nsew", pady=5)

        # Load and resize the profile image
        loading_image = Image.open(organizer.players[player]["profile_image"])
        loading_image = loading_image.resize((50, 50))
        self.profile_picture = ImageTk.PhotoImage(loading_image)

        # Add player profile image inside the frame
        self.label_image = tk.Label(self.frame, image=self.profile_picture, bg=self.default_bg)
        self.label_image.grid(row=0, column=0, padx=5, pady=5)

        # Add player name inside the frame
        self.label = tk.Label(self.frame, text=organizer.players[player]["name"], bg=self.default_bg)
        self.label.grid(row=0, column=1, padx=5, pady=5)

        # Bind hover events
        self.frame.bind("<Enter>", self.on_hover)
        self.frame.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        """Change the background color when the mouse enters the frame."""
        self.frame.configure(bg=self.hover_bg)
        self.label_image.configure(bg=self.hover_bg)
        self.label.configure(bg=self.hover_bg)

    def on_leave(self, event):
        """Revert the background color when the mouse leaves the frame."""
        self.frame.configure(bg=self.default_bg)
        self.label_image.configure(bg=self.default_bg)
        self.label.configure(bg=self.default_bg)
