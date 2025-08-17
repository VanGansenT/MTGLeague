import tkinter as tk
from PIL import Image, ImageTk
from src.models import MatchObject
from src.models.PlayerObject import PlayerObject
import tkinter.font as tkFont

class MatchView:
    def __init__(self, master, matchObject : MatchObject, row, column):
        self.default_bg = "#d3d3d3"  
        self.hover_bg = "#c0c0c0"    
        self.clicked_bg = "#a9a9a9" 

        self.is_clicked = False 

        self.frame = tk.Frame(
            master,
            bg=self.default_bg,
            padx=5,
            pady=5,
            relief="raised",
            bd=2
        )
        self.frame.grid(row=row, column=column, columnspan=2, sticky="nsew", pady=5)

        self.label = tk.Label(self.frame, text="Match Info", bg=self.default_bg)
        self.label.grid(0,0, padx=5, pady=5)

        self.matchObject = matchObject
        self.create_player_labels(matchObject.player1, matchObject.player2, 0, 0)
        self.label_match = tk.Label(self.frame, text=f"Match ID: {matchObject.match_id}", bg=self.default_bg)

        # Optional: placeholder for an image label
        # self.label_image = tk.Label(self.frame, image=..., bg=self.default_bg)
        # self.label_image.pack()

        # Bind events
        self.frame.bind("<Enter>", self.on_hover)
        self.frame.bind("<Leave>", self.on_leave)
        self.frame.bind("<Button-1>", self.on_click)
        self.frame.bind("<ButtonRelease-1>", self.on_release)

    def create_player_labels(self, player1: PlayerObject, player2: PlayerObject, row, column):
        # Load and resize the profile images
        loading_image1 = Image.open(player1.imagePath)
        loading_image1 = loading_image1.resize((50, 50))
        self.profile_picture1 = ImageTk.PhotoImage(loading_image1)

        loading_image2 = Image.open(player2.imagePath)
        loading_image2 = loading_image2.resize((50, 50))
        self.profile_picture2 = ImageTk.PhotoImage(loading_image2)

        # Add player profile images inside the frame
        self.label_image1 = tk.Label(self.frame, image=self.profile_picture1, bg=self.default_bg)
        self.label_image1.grid(row=row, column=column, padx=5, pady=5)

        self.label_image2 = tk.Label(self.frame, image=self.profile_picture2, bg=self.default_bg)
        self.label_image2.grid(row=row, column=column+1, padx=5, pady=5)

    def on_hover(self, event):
        if not self.is_clicked:
            self.frame.configure(bg=self.hover_bg)
            self.label.configure(bg=self.hover_bg)

    def on_leave(self, event):
        if not self.is_clicked:
            self.frame.configure(bg=self.default_bg)
            self.label.configure(bg=self.default_bg)

    def on_click(self, event):
        self.is_clicked = True
        self.frame.configure(bg=self.clicked_bg)
        self.label.configure(bg=self.clicked_bg)

    def on_release(self, event):
        self.is_clicked = False
        self.frame.configure(bg=self.default_bg)
        self.label.configure(bg=self.default_bg)
