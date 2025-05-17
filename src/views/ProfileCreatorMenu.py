import tkinter as tk
from PIL import Image, ImageTk
import os

from src.views.ProfileImageSelector import ProfileImageSelector

# image_path = "resources/images/"


def get_image_filenames(directory):
    image_extensions = ['.jpg', '.jpeg', '.png']  # Add more extensions if needed
    image_filenames = []

    for filename in os.listdir(directory):
        # Check if the file has one of the image extensions
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            image_filenames.append(directory + "/" + filename)

    return image_filenames


class ProfileCreatorMenu:
    def __init__(self, controller, tab, image_path, row, column):
        self.controller = controller
        self.tab = tab
        self.image_path = image_path
        self.profile_selector = None
        self.images = get_image_filenames(self.image_path)
        self.index = 0

        # Load and resize the image
        image = Image.open(self.images[self.index])
        image = image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(image)  # Store the reference to prevent garbage collection

        # Create a button
        self.button = tk.Button(tab, image=self.photo, command=self.select_profile_image)
        self.button.grid(row=row, column=column, padx=5, pady=10)

        self.player_label = tk.Label(tab, text="Player Name:")
        self.player_label.grid(row=row, column=column + 1)

        self.player_entry = tk.Entry(tab)
        self.player_entry.grid(row=row, column=column + 2)

        self.add_player_button = tk.Button(tab, text="Add Player", command=self.add_player)
        self.add_player_button.grid(row=row, column=column + 3)

        self.player_feedback = tk.Label(tab, text="")
        self.player_feedback.grid(row=row, column=column + 4)

    def select_profile_image(self):
        if self.profile_selector is None:
            self.profile_selector = ProfileImageSelector(self, self.images, 0, 0)

    def add_player(self):
        player_name = self.player_entry.get()

        if player_name:
            feedback = self.controller.add_player(player_name, self.images[self.index])
            if (feedback == True):
                self.player_feedback.config(text="Player '{}' successfully added".format(player_name), fg="green")
            else:
                self.player_feedback.config(text="Player '{}' already exist".format(player_name), fg="red")

            # Clear the entry after adding the player
            self.player_entry.delete(0, tk.END)
            # Reset the feedback after N seconds
            self.tab.after(5000, self.reset_feedback)

    def reset_feedback(self):
        self.player_feedback.config(text="", fg="black")

    def select_profile(self, index):
        self.index = index
        # reload image
        # Get the new image filename
        new_image_filename = self.images[self.index]

        # Load and resize the new image
        new_image = Image.open(new_image_filename)
        new_image = new_image.resize((100, 100))
        new_photo = ImageTk.PhotoImage(new_image)

        # Update the button to display the new image
        self.button.config(image=new_photo)
        self.button.photo = new_photo  # Store the reference to prevent garbage collection

    def close_profile_selector(self):
        if self.profile_selector is not None:
            self.profile_selector.destroy()
            self.profile_selector = None

    def close_window(self):
        self.profile_selector.destroy()
        self.profile_selector = None

