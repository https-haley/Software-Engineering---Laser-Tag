import tkinter as tk
from tkinter import ttk, messagebox
import socket

class PlayerEntry: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Player Entry")
        self.root.geometry("520x360")
        self.root.resizable(True, True)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PlayerEntry()
    app.run()