import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class PlayerSelector:
    def __init__(self, master, label_text, player_map, row, column):

        self.player_map = player_map

        players = self.get_player_names()
        if not players:
            self.selected_player = tk.StringVar(value="No players available")  # Make it a StringVar
            self.image_path = os.path.join("resources", "images", "profile", "ajaniGoldmanes.jpg")
            self.dropdown_state = "disabled"
        else:
            self.selected_player = tk.StringVar(value=players[0])  # Make it a StringVar
            self.image_path = self.get_player_profile_image(self.selected_player.get())
            self.dropdown_state = "readonly"

        # Frame to encapsulate the player selector
        self.frame = tk.Frame(master, relief="groove", bd=2, padx=10, pady=10)
        self.frame.grid(row=row, column=column, padx=10, pady=10)

        # Label to identify the player (e.g., "Player 1")
        self.label = tk.Label(self.frame, text=label_text, font=("Arial", 14, "bold"))
        self.label.pack(pady=5)

        # Load and display a default profile image
        self.profile_image = self.load_image(self.image_path, (100, 100))
        self.image_label = tk.Label(self.frame, image=self.profile_image)
        self.image_label.pack(pady=5)

        # Dropdown menu for selecting players
        self.dropdown = ttk.Combobox(
            self.frame,
            textvariable=self.selected_player,
            values=players,
            state=self.dropdown_state
        )
        self.dropdown.pack(pady=5)

         # Add a listener for the dropdown change to update the profile image
        self.dropdown.bind("<<ComboboxSelected>>", self.update_profile_image)

    def get_player_names(self):
        player_names = list(self.player_map.keys())
        return player_names
  
    def get_player_profile_image(self, player_name):
        player_object = self.player_map[player_name]
        return player_object.imagePath
    
    def get_dropdown_state(self):
        return self.dropdown_state

    def load_image(self, path, size):
        """Helper method to load and resize an image."""
        try:
            image = Image.open(path)
            image = image.resize(size)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
    
    def update_profile_image(self, event):
        """Update the displayed profile image based on the selected player."""
        selected_player_name = self.selected_player.get()
        self.image_path = self.get_player_profile_image(selected_player_name)
        self.profile_image = self.load_image(self.image_path, (100, 100))
        self.image_label.config(image=self.profile_image)
        

