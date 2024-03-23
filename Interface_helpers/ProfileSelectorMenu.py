import tkinter as tk
from PIL import Image, ImageTk

image_path = "resources/images/"


class ProfileSelectorMenu:
    def __init__(self, master, images, row, column):
        self.master = master
        self.images = images
        self.profileSelector = None

        # Load and resize the image
        image = Image.open(
            image_path + "LoadingScreenMTG.jpg")  # Assuming "LoadingScreenMTG.jpg" is in the current directory
        image = image.resize((50, 50))
        self.photo = ImageTk.PhotoImage(image)  # Store the reference to prevent garbage collection

        # Create a button
        button = tk.Button(master, image=self.photo, command=self.button_click)
        button.grid(row=row, column=column)

    def button_click(self):
        print("fuck you too")
        if (self.profileSelector is None):
            self.profileSelector = tk.Tk()
            # Bind the destroy event to the close_window function
            self.profileSelector.protocol("WM_DELETE_WINDOW", self.close_window)
        pass

    def close_window(self):
        self.profileSelector.destroy()
        self.profileSelector = None
