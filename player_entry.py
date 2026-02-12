import tkinter as tk
from tkinter import ttk, messagebox
import socket

class PlayerEntry: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Player Entry")
        self.root.geometry("520x360")
        self.root.resizable(True, True)
        self.root.configure(bg="black")
            #Main Frame
        main_frame = tk.Frame(self.root)
        main_frame.pack()

    #Title
        title = tk.Label(
            self.root,
            text="Edit Current Game",
            font=("Arial", 18, "bold"),
            fg="blue",
            bg = "black"
        )
        title.pack(pady=3)


        self.create_red_team_table(main_frame)
        self.create_green_team_table(main_frame)

    def create_red_team_table(self, parent):
        red_frame = tk.LabelFrame(
            parent,
            text="RED TEAM",
            bg="black",
            fg="white",
            font=("Arial", 12 ),
            padx=10,
            pady=10
        )
        red_frame.grid(row=0, column=0, padx=20)

        self.red_table.pack()

        for i in range(20):
            self.red_table.insert("", "end", value=(i, "", ""))

    def team_ui(self):
        self.tree = ttk.Treeview(self, columns)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PlayerEntry()
    app.run()