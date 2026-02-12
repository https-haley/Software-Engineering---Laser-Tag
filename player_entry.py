import tkinter as tk
from tkinter import ttk

class PlayerEntry:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Laser Tag Entry Terminal")
        self.root.geometry("900x500")
        self.root.configure(bg="black")

        title = tk.Label(
            self.root,
            text="Edit Current Game",
            font=("Arial", 18, "bold"),
            fg="deepskyblue",
            bg="black"
        )
        title.pack(pady=15)

        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack()

        self.create_red_team_table(main_frame)
        self.create_green_team_table(main_frame)

    def create_red_team_table(self, parent):
        red_frame = tk.LabelFrame(
            parent,
            text="RED TEAM",
            bg="darkred",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        red_frame.grid(row=0, column=0, padx=20)

        
        self.red_table = ttk.Treeview(
            red_frame,
            columns=("PlayerNumber", "UserName"),
            show="headings",
            height=20
        )

        self.red_table.column("PlayerNumber", width=40, anchor="center")
        self.red_table.column("UserName", width=140, anchor="center")

        self.red_table.pack()

        for i in range(20):
            self.red_table.insert("", "end", values=(i, "", ""))

    def create_green_team_table(self, parent):
        green_frame = tk.LabelFrame(
            parent,
            text="GREEN TEAM",
            bg="darkgreen",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        green_frame.grid(row=0, column=1, padx=20)

        self.green_table = ttk.Treeview(
            green_frame,
            columns=("PlayerNumber", "UserName"),
            show="headings",
            height=20
        )

        self.green_table.column("PlayerNumber", width=40, anchor="center")
        self.green_table.column("UserName", width=140, anchor="center")

        self.green_table.pack()

        for i in range(20):
            self.green_table.insert("", "end", values=(i, "", ""))


    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PlayerEntry()
    app.run()
