import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import udp


class PlayActionDisplay:
    def __init__(self, root, red_players, green_players, music):
        self.root = root
        self.root.title("Play Action Display")
        self.root.geometry("1000x700")
        self.root.configure(bg="black")
        self.last_attacker = None
        self.players_with_base = set()
        self.team_tables = {}
        self.player_map = {}
        self.red_ids = [x[1] for x in red_players]
        self.green_ids = [x[1] for x in green_players]
        self.music = music

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

        # Load base icon image
        img = Image.open("baseicon.jpg")  
        img = img.resize((20, 20))
        self.base_icon = ImageTk.PhotoImage(img)

        udp.setMessageHandler(self.handle_udp_message)
        udp.startUDP()

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
            show="tree headings",
            height=15
        )

        table.heading("Slot", text="#")
        table.heading("EquipmentID", text="Equip ID")
        table.heading("UserName", text="Codename")
        table.heading("Score", text="Score")
        table.heading("#0", text="")
        
        table.column("#0", width=30, anchor="center")
        table.column("Slot", width=40, anchor="center")
        table.column("EquipmentID", width=100, anchor="center")
        table.column("UserName", width=160, anchor="center")
        table.column("Score", width=80, anchor="center")

        table.pack()
        self.team_tables[team_name] = table

        # Insert players
        for player in players:
            if len(player) == 3:
                item = table.insert("", "end", text="", values=(player[0], player[1], player[2], 0))
                equipment_id = player[1]
            else:
                item = table.insert("", "end", text="", values=player)
                equipment_id = player[1]

            self.player_map[equipment_id] = (team_name, item)

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

    def change_player_score(self, equipment_id, amount):
        if equipment_id not in self.player_map:
            return

        team_name, item = self.player_map[equipment_id]
        table = self.team_tables[team_name]

        values = list(table.item(item, "values"))
        current_score = int(values[3])
        new_score = current_score + amount
        values[3] = new_score

        table.item(item, values=values)

        self.update_team_score(team_name)
        self.sort_team_table(team_name)

    def update_team_score(self, team_name):
        table = self.team_tables[team_name]
        total = 0

        for item in table.get_children():
            values = table.item(item, "values")
            total += int(values[3])

        if team_name in self.score_labels:
            self.score_labels[team_name].config(text=f"Total Score: {total}")
            
    def sort_team_table(self, team_name):
        table = self.team_tables[team_name]

        rows = []
        for item in table.get_children():
            values = table.item(item, "values")
            score = int(values[3])
            rows.append((score, item, values, table.item(item, "text")))

        rows.sort(key=lambda x: x[0], reverse=True)

        for index, (_score, item, _values, _text) in enumerate(rows):
            table.move(item, "", index)

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

    def log_event(self, message):
        self.event_log.insert(tk.END, message)
        self.event_log.yview(tk.END)
        
    def give_base_icon(self, equipment_id):
        if equipment_id in self.player_map:
            team_name, item = self.player_map[equipment_id]
            table = self.team_tables[team_name]

            if equipment_id not in self.players_with_base:
                 table.item(item, image=self.base_icon)
                 self.players_with_base.add(equipment_id)

    def assign_base_to_last_attacker(self, scoring_team):
        if self.last_attacker is None:
            return

        if self.last_attacker in self.player_map:
            team_name, item = self.player_map[self.last_attacker]

            if team_name == f"{scoring_team.upper()} TEAM" and self.last_attacker not in self.players_with_base:

                # Give icon
                self.give_base_icon(self.last_attacker)

                # Add 100 points
                table = self.team_tables[team_name]
                values = list(table.item(item, "values"))

                score = int(values[3])
                score += 100
                values[3] = score

                table.item(item, values=values)
                name = self.get_player_name(self.last_attacker)
                self.log_event(f"{name} captured the base (+100)")
                self.update_team_score(team_name)

    def get_player_name(self, equipment_id):
        if equipment_id in self.player_map:
            team_name, item = self.player_map[equipment_id]
            table = self.team_tables[team_name]
            values = table.item(item, "values")
            return values[2]  
        return f"Player {equipment_id}"

    def handle_udp_message(self, msg):
        try:
            if ":" in msg:
                attacker, target = msg.split(":")
                attacker = int(attacker)

                self.last_attacker = attacker
                attacker_name = self.get_player_name(attacker)

                if target == "43":
                    self.log_event(f"{attacker_name} captured the Green Base")
                    self.assign_base_to_last_attacker("red")
                    return

                if target == "53":
                    self.log_event(f"{attacker_name} captured the Red Base")
                    self.assign_base_to_last_attacker("green")
                    return

                target = int(target)
                target_name = self.get_player_name(target)

                self.log_event(f"{attacker_name} tagged {target_name}")

                both_red = (attacker in self.red_ids) and (target in self.red_ids)
                both_green = (attacker in self.green_ids) and (target in self.green_ids)

                if both_red or both_green:
                    # Friendly fire
                    udp.broadcastEquipmentID(attacker)
                    udp.broadcastEquipmentID(target)
                else:
                    # Normal hit
                    udp.broadcastEquipmentID(target)

        except Exception as e:
            print("Error:", e)
