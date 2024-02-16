import tkinter as tk
from tkinter import ttk

class AddBookWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Add Book")
        self.geometry("400x300")

        self.create_widgets()


    def create_widgets(self):
        pass