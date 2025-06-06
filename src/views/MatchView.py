import tkinter as tk
from PIL import Image, ImageTk
from src.models import MatchObject
from src.models.PlayerObject import PlayerObject
import tkinter.font as tkFont

class MatchView:
    def __init__(self, master, matchObject: MatchObject, row, column):
        # Define default, hover, and clicked background colors
        self.default_bg = "#d3d3d3"  # Light gray
        self.hover_bg = "#c0c0c0"    # Slightly darker gray for hover
        self.clicked_bg = "#a9a9a9"  # Darker gray for clicked state
        self.is_clicked = False      # Flag to track if the frame is clicked

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

        # Bind hover events
        self.frame.bind("<Enter>", self.on_hover)
        self.frame.bind("<Leave>", self.on_leave)

        # Bind click and release events
        self.frame.bind("<Button-1>", self.on_click)
        self.frame.bind("<ButtonRelease-1>", self.on_release)

    def on_hover(self, event):
        """Change the background color when the mouse enters the frame."""
        if not self.is_clicked:
            self.frame.configure(bg=self.hover_bg)
            self.label_image.configure(bg=self.hover_bg)
            self.label.configure(bg=self.hover_bg)

    def on_leave(self, event):
        """Revert the background color when the mouse leaves the frame."""
        if not self.is_clicked:
            self.frame.configure(bg=self.default_bg)
            self.label_image.configure(bg=self.default_bg)
            self.label.configure(bg=self.default_bg)

    def on_click(self, event):
        """Change the background color to clicked color and call the on_click callback."""
        self.is_clicked = True
        self.frame.configure(bg=self.clicked_bg)
        self.label_image.configure(bg=self.clicked_bg)
        self.label.configure(bg=self.clicked_bg)

    def on_release(self, event):
        """Revert the background color back to default when the mouse button is released."""
        self.is_clicked = False
        self.frame.configure(bg=self.default_bg)
        self.label_image.configure(bg=self.default_bg)
        self.label.configure(bg=self.default_bg)

        
