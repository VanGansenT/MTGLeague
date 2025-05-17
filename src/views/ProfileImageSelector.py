import tkinter as tk
from PIL import Image, ImageTk
import os
import functools
import math

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
