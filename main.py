import ctypes
import tkinter as tk
from tkinter import ttk
from itertools import combinations
from PIL import Image, ImageTk
import os

from src.controller.LoadingScreen import LoadingScreen


if __name__ == "__main__":
    root_loading = tk.Tk()
    loading_screen = LoadingScreen(root_loading)
    root_loading.mainloop()
