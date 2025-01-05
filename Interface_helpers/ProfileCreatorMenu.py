import tkinter as tk
from PIL import Image, ImageTk
import os
import functools
import math

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
    def __init__(self, organizer, master, image_path, row, column):
        self.organizer = organizer
        self.master = master
        self.image_path = image_path
        self.profile_selector = None
        self.images = get_image_filenames(self.image_path)
        self.index = 0

        # Load and resize the image
        image = Image.open(self.images[self.index])
        image = image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(image)  # Store the reference to prevent garbage collection

        # Create a button
        self.button = tk.Button(master, image=self.photo, command=self.select_profile_image)
        self.button.grid(row=row, column=column, padx=5, pady=10)

        self.player_label = tk.Label(master, text="Player Name:")
        self.player_label.grid(row=row, column=column + 1)

        self.player_entry = tk.Entry(master)
        self.player_entry.grid(row=row, column=column + 2)

        self.add_player_button = tk.Button(master, text="Add Player", command=self.add_player)
        self.add_player_button.grid(row=row, column=column + 3)

        self.player_feedback = tk.Label(master, text="")
        self.player_feedback.grid(row=row, column=column + 4)

    def select_profile_image(self):
        if self.profile_selector is None:
            self.profile_selector = ProfileImageSelector(self, self.images, 0, 0)

    def add_player(self):
        player_name = self.player_entry.get()

        if player_name:
            feedback = self.organizer.add_player(player_name, self.images[self.index])
            if (feedback == True):
                self.player_feedback.config(text="Player '{}' successfully added".format(player_name), fg="green")
            else:
                self.player_feedback.config(text="Player '{}' already exist".format(player_name), fg="red")

            # Clear the entry after adding the player
            self.player_entry.delete(0, tk.END)
            # Reset the feedback after N seconds
            self.master.after(5000, self.reset_feedback)

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


class ProfileImageSelector:
    def __init__(self, profile_controller, images, x, y):
        self.profile_controller = profile_controller
        self.master = tk.Toplevel()
        self.master.title("profile selection")
        self.images = images
        self.buttons = []  # List to store Button widgets

        # Bind the close_window() function to the WM_DELETE_WINDOW event
        self.master.protocol("WM_DELETE_WINDOW", self.close_window)

        column = 3
        row = math.ceil(len(images) / column)

        for i in range(row):
            for j in range(column):
                self.create_profile_button(i * column + j, i + x, j + y)

    def create_profile_button(self, index, row, column):
        image = self.images[index]
        # Load and resize the image
        image = Image.open(image)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)

        # Create a button with the image
        button = tk.Button(self.master, image=photo, command=functools.partial(self.button_click, index))
        button.photo = photo  # Store the PhotoImage object as an attribute of the button
        button.grid(row=row * 2, column=column, padx=5, pady=10)  # Add vertical space between buttons

        # Store the button to prevent it from being garbage collected
        self.buttons.append(button)

    def button_click(self, index):
        self.profile_controller.select_profile(index)
        self.close_window()

    def close_window(self):
        self.profile_controller.close_window()

    def destroy(self):
        self.master.destroy()
