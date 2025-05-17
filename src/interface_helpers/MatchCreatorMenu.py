import tkinter as tk
from tkinter import ttk
from src.interface_helpers.PlayerSelector import PlayerSelector
import logging

class MatchCreatorMenu:
    def __init__(self, organizer, master, row, column):
        logging.basicConfig(level=logging.INFO)
        self.organizer = organizer
        self.master = master

        available_players = organizer.get_players()

        # Create player selectors for Player 1 and Player 2
        self.player1 = PlayerSelector(self.master, "Player 1", available_players, row, column)
        self.player2 = PlayerSelector(self.master, "Player 2", available_players, row, column + 1)

        self.player1.selected_player.trace_add("write", lambda *args: self.update_button_state())
        self.player2.selected_player.trace_add("write", lambda *args: self.update_button_state())

        # Add a single Confirm button
        self.confirm_button = tk.Button(
            self.master,
            text="Confirm",
            command=self.confirm_selection,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            state= "disabled"
        )
        self.confirm_button.grid(row=row, column=column + 2, columnspan=2, pady=20)

    def update_button_state(self):
        player1 = self.player1.selected_player.get()
        player2 = self.player2.selected_player.get()
        if self.is_valid_player(player1) and self.is_valid_player(player2) and player1 != player2:
            self.confirm_button.config(state="normal")
        else:
            self.confirm_button.config(state="disabled")

    def confirm_selection(self):
        """Handle confirmation for both players."""
        player1_selection = self.player1.selected_player.get()
        player2_selection = self.player2.selected_player.get()
        if (self.is_valid_player(player1_selection), self.is_valid_player(player2_selection)):
            logging.info(f"Player 1: {player1_selection}")
            logging.info(f"Player 2: {player2_selection}")

    def is_valid_player(self, playerName):
        return playerName != "No players available"

