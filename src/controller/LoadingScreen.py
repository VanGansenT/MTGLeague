import tkinter as tk
import os
from PIL import Image, ImageTk

from src.controller.EventOrganizer import EventOrganizer

image_path = "resources/images/"


class LoadingScreen:
    def __init__(self, master):
        print(os.path.exists(image_path + "LoadingScreenMTG.jpg"))
        self.master = master
        self.master.title("Loading...")

        self.loading_width = 600
        self.loading_height = 600

        # Load your image for the loading screen
        self.loading_image = Image.open(image_path + "LoadingScreenMTG.jpg")
        self.loading_image = self.loading_image.resize((self.loading_width, self.loading_height))
        self.loading_photo = ImageTk.PhotoImage(self.loading_image)

        # Display the loading image
        self.loading_label = tk.Label(self.master, image=self.loading_photo)
        self.loading_label.pack()

        # After a certain delay, destroy the loading screen and start the main application
        self.master.after(1500, self.load_main_app)

    def load_main_app(self):
        self.loading_x = self.master.winfo_x()
        self.loading_y = self.master.winfo_y()

        self.loading_width = self.master.winfo_width()
        self.loading_height = self.master.winfo_height()

        self.master.destroy()
        self.root = tk.Tk()
        self.root.geometry(f"{self.loading_width}x{self.loading_height}+{self.loading_x}+{self.loading_y}")
        event_organizer = EventOrganizer(self.root)
