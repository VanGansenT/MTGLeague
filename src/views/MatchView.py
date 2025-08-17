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

        self.winner = None

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
        self.label.grid(row=row, column=column, padx=5, pady=5)

        self.matchObject = matchObject
        self.create_player_labels(matchObject.player1, matchObject.player2, 0, 0)
        self.label_match = tk.Label(self.frame, text=f"Match ID: {matchObject.match_id}", bg=self.default_bg)


        # Bind events
        self.frame.bind("<Enter>", self.on_hover)
        self.frame.bind("<Leave>", self.on_leave)
        self.frame.bind("<Button-1>", self.on_click)
        self.frame.bind("<ButtonRelease-1>", self.on_release)

    def create_player_labels(self, player1: PlayerObject, player2: PlayerObject, row, column):
        img1 = Image.open(player1.imagePath).resize((50, 50))
        self.profile_picture1 = ImageTk.PhotoImage(img1)

        img2 = Image.open(player2.imagePath).resize((50, 50))
        self.profile_picture2 = ImageTk.PhotoImage(img2)

        self.player1_button = tk.Button(
            self.frame,
            image=self.profile_picture1,
            text=player1.name,
            compound="top", 
            font=("Arial", 12, "bold"),
            bg=self.default_bg,
            command=lambda: self.set_winner(player1)
        )
        self.player1_button.grid(row=row, column=column, padx=5, pady=5)

        self.vs_label = tk.Label(
            self.frame,
            text="VS",
            bg=self.default_bg,
            font=("Arial", 14, "bold")
        )
        self.vs_label.grid(row=row, column=column+1, padx=10, pady=5)

        self.player2_button = tk.Button(
            self.frame,
            image=self.profile_picture2,
            text=player2.name,
            compound="top",
            font=("Arial", 12, "bold"),
            bg=self.default_bg,
            command=lambda: self.set_winner(player2)
        )
        self.player2_button.grid(row=row, column=column+2, padx=5, pady=5)

    def set_winner(self, winner: PlayerObject):
        self.toggle_winner(winner)

    def toggle_winner(self, winner: PlayerObject):
        if self.winner == winner:
            self.winner = None
            self.player1_button.config(bg=self.default_bg)
            self.player2_button.config(bg=self.default_bg)
        else:
            self.winner = winner
            if winner.name == self.player1_button.cget("text"):
                self.player1_button.config(bg="green")
                self.player2_button.config(bg=self.default_bg)
            else:
                self.player2_button.config(bg="green")
                self.player1_button.config(bg=self.default_bg)

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

