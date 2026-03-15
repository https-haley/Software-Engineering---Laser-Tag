import tkinter as tk
from tkinter import ttk
import udp


class PlayActionDisplay:
    def __init__(self, root, red_players, green_players):
        self.root = root
        self.root.title("Play Action Display")
        self.root.geometry("1000x700")
        self.root.configure(bg="black")

        self.score_labels = {} # Keep track of score labels to update later

        self.time_left = 360 # In seconds 6 min game time
        self.timer_label = tk.Label(
            self.root,
            text="Time Remaining: 06:00",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="black"
        )
        self.timer_label.place(x=15, y=15)
        self.update_timer()

        # Title
        title = tk.Label(
            self.root,
            text="PLAY ACTION DISPLAY",
            font=("Arial", 24, "bold"),
            fg="yellow",
            bg="black"
        )
        title.pack(pady=20)

        # Frame for team tables
        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack(pady=20)

        # Create team tables
        self.create_team_display(main_frame, "RED TEAM", red_players, 0, "darkred")
        self.create_team_display(main_frame, "GREEN TEAM", green_players, 1, "darkgreen")

        # Play-by play placeholder
        event_frame = tk.LabelFrame(
            self.root,
            text="PLAY BY PLAY",
            bg="black",
            fg="white",
            font=("Arial", 14, "bold"),
            padx=10,
            pady=10
        )
        event_frame.pack(pady=5, fill="both", expand=True)

        self.event_log = tk.Listbox(
            event_frame,
            width=80,
            height=20,
            bg="black",
            fg="white",
            font=("Courier", 12)
        )
        self.event_log.pack(fill="both", expand=True)

        # Placeholder text
        self.event_log.insert(tk.END, "Game events will appear here...")

    def create_team_display(self, parent, team_name, players, col, color):
        # Container to hold team frame and score label
        container = tk.Frame(parent, bg="black")
        container.grid(row=0, column=col, padx=40)

        frame = tk.LabelFrame(
            container,
            text=team_name,
            bg=color,
            fg="white",
            font=("Arial", 14, "bold"),
            padx=10,
            pady=10
        )
        frame.pack()

        table = ttk.Treeview(
            frame,
            columns=("Slot", "EquipmentID", "UserName", "Score"),
            show="headings",
            height=15
        )

        table.heading("Slot", text="#")
        table.heading("EquipmentID", text="Equip ID")
        table.heading("UserName", text="Codename")
        table.heading("Score", text="Score")

        table.column("Slot", width=40, anchor="center")
        table.column("EquipmentID", width=100, anchor="center")
        table.column("UserName", width=160, anchor="center")
        table.column("Score", width=80, anchor="center")

        table.pack()

        # Insert players
        for player in players:
            if len(player) == 3:
                table.insert("", "end", values=(player[0], player[1], player[2], 0))
            else:
                table.insert("", "end", values=player)

        score_label = tk.Label(
            container,
            text="Total Score: 0",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="black",
            pady=10
        )
        score_label.pack()

        self.score_labels[team_name] = score_label

    def update_score(self, team_name, new_score):
        if team_name in self.score_labels:
            self.score_labels[team_name].config(text=f"Score: {new_score}")

    def update_timer(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60) # Get quotient and remainder to get minutes and seconds remaining
            time_string = f"Time Remaining: {mins:02d}:{secs:02d}"

            self.timer_label.config(text=time_string)

            self.time_left -= 1
            self.root.after(1000, self.update_timer) # Wait 1 second to update timer
        else:
            self.timer_label.config(text = "Game Over", fg="red")
            udp.broadcastEndCode()
