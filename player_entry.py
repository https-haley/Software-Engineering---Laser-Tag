import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import udp
import db

class PlayerEntry:
    def __init__(self, root):
        self.root = root
        self.root.title("Entry Terminal")
        self.root.geometry("1080x720")
        self.root.configure(bg="black")
        self.active_team = "RED"  

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
        self.red_table.bind("<Button-1>", lambda e: self.set_active_team("RED"), add="+")
        self.green_table.bind("<Button-1>", lambda e: self.set_active_team("GREEN"), add="+")
        self.create_bottom_bar()
        self.bind_function_keys()
        self.conn = db.get_connection()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        udp.startUDP()

    def on_close(self):
        self.conn.close()
        self.root.destroy()
        
    def set_active_team(self, team):
        self.active_team = team
        self.red_table.selection_remove(self.red_table.selection())
        self.green_table.selection_remove(self.green_table.selection())
        
    def get_next_empty_row(self, table):
        for row in table.get_children():
            slot, equip, name = table.item(row, "values")
            if str(equip) == "" and str(name) == "":
                return row, slot
        return None, None

    def create_red_team_table(self, parent):
        self.red_frame = tk.LabelFrame(
            parent,
            text="RED TEAM",
            bg="darkred",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        self.red_frame.grid(row=0, column=0, padx=20)

        
        self.red_table = ttk.Treeview(
            self.red_frame,
            columns=("Slot", "EquipmentID", "UserName"),
            show="headings",
            height=20,
            selectmode="browse"
        )

        self.red_table.column("Slot", width=40, anchor="center")
        self.red_table.column("EquipmentID", width=100, anchor="center")
        self.red_table.column("UserName", width=140, anchor="center")

        self.red_table.heading("Slot", text="#")
        self.red_table.heading("EquipmentID", text="Equip ID")
        self.red_table.heading("UserName", text="Codename")

        self.red_table.pack()

        for i in range(20):
            self.red_table.insert("", "end", values=(i, "", ""))

    def create_green_team_table(self, parent):
        self.green_frame = tk.LabelFrame(
            parent,
            text="GREEN TEAM",
            bg="darkgreen",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        self.green_frame.grid(row=0, column=1, padx=20)

        self.green_table = ttk.Treeview(
            self.green_frame,
            columns=("Slot", "EquipmentID", "UserName"),
            show="headings",
            height=20,
            selectmode="browse"
        )

        self.green_table.column("Slot", width=40, anchor="center")
        self.green_table.column("EquipmentID", width=100, anchor="center")
        self.green_table.column("UserName", width=140, anchor="center")

        self.green_table.heading("Slot", text="#")
        self.green_table.heading("EquipmentID", text="Equip ID")
        self.green_table.heading("UserName", text="Codename")

        self.green_table.pack()

        for i in range(20):
            self.green_table.insert("", "end", values=(i, "", ""))

    # Bottom Bar
    def create_bottom_bar(self):
        bar = tk.Frame(self.root, bg="black")
        bar.pack(side="bottom", fill="x")

        btn_row = tk.Frame(bar, bg="black")
        btn_row.pack(fill="x", padx=10, pady=(8, 4))

        def make_btn(text, command):
            return tk.Button(
                btn_row,
                text=text,
                command=command,
                bg="black",
                fg="lime",
                activebackground="gray20",
                activeforeground="lime",
                font=("Arial", 11, "bold"),
                bd=2,
                relief="solid",
                padx=18,
                pady=10
            )

    #Buttons
        make_btn("F1\nEdit\nGame", self.f1_edit_game).pack(side="left", padx=10)
        make_btn("F2\nGame\nParameters", self.f2_game_params).pack(side="left", padx=10)
        make_btn("F3\nStart\nGame", self.f3_start_game).pack(side="left", padx=10)
        make_btn("F5\nPreEntered\nGames", self.f5_preentered).pack(side="left", padx=40)
        make_btn("F7", self.f7_unused).pack(side="left", padx=10)
        make_btn("F8\nView\nGame", self.f8_view_game).pack(side="left", padx=10)
        make_btn("F10\nFlick\nSync", self.f10_flick_sync).pack(side="left", padx=40)
        make_btn("F12\nClear\nGame", self.f12_clear_game).pack(side="left", padx=10)

        hint = tk.Label(
            bar,
            text="<Del> to Delete Player, <Ins> to Manually Insert, or edit codename",
            bg="lightgray",
            fg="black",
            font=("Arial", 11)
        )
        hint.pack(fill="x")


    #Keybinds
    def bind_function_keys(self):
        self.root.bind("<F1>",  lambda e: self.f1_edit_game())
        self.root.bind("<F2>",  lambda e: self.f2_game_params())
        self.root.bind("<F3>",  lambda e: self.f3_start_game())
        self.root.bind("<F5>",  lambda e: self.f5_preentered())
        self.root.bind("<F7>",  lambda e: self.f7_unused())
        self.root.bind("<F8>",  lambda e: self.f8_view_game())
        self.root.bind("<F10>", lambda e: self.f10_flick_sync())
        self.root.bind("<F12>", lambda e: self.f12_clear_game())

        self.root.bind("<Delete>", lambda e: self.delete_selected_player())
        self.root.bind("<Insert>", lambda e: self.manual_insert_player())

    #Button Functions
    def f1_edit_game(self):      print("F1 Edit Game")
    def f2_game_params(self):    
        print("F2 Game Parameters")
        win = tk.Toplevel(self.root)
        win.title("Change Network Address")
        win.configure(bg="black")
        win.grab_set()
    
        tk.Label(win, text="Enter new network address:",
                 fg="deepskyblue", bg="black",
                 font=("Arial", 12, "bold")).pack(pady=10)
    
        entry = tk.Entry(win, width=30)
        entry.pack(padx=15, pady=10)
        entry.insert(0, udp.networkAddress)
        entry.focus_set()
    
        def apply():
            new_addr = entry.get().strip()
            if new_addr != "":
                udp.setNetworkAddress(new_addr)
            win.destroy()
    
        tk.Button(win, text="Apply", command=apply,
                  bg="black", fg="lime", bd=2,
                  relief="solid", padx=16, pady=6).pack(pady=10)
    
        win.bind("<Return>", lambda e: apply())
    def f3_start_game(self):     print("F3 Start Game")
    def f5_preentered(self):     print("F5 PreEntered Games")
    def f7_unused(self):         print("F7 pressed")
    def f8_view_game(self):      print("F8 View Game")
    def f10_flick_sync(self):    print("F10 Flick Sync")
    def f12_clear_game(self):    
        print("F12 Clear Game")

        for table in (self.red_table, self.green_table):
            for item_id in table.get_children():
                slot, _equip, _name = table.item(item_id, "values")
                table.item(item_id, values=(slot, "", ""))

    def delete_selected_player(self):
        print("Delete selected player")
        selected = self.red_table.selection()
        table = self.red_table
        if not selected:
            selected = self.green_table.selection()
            table = self.green_table

        if selected:
            item_id = selected[0]
            slot, _equip, _name = table.item(item_id, "values")
            table.item(item_id, values=(slot, "", ""))

    def manual_insert_player(self):
           
        table = self.red_table if self.active_team == "RED" else self.green_table
        team = self.active_team

        item_id, slot = self.get_next_empty_row(table)
        if item_id is None:
            messagebox.showerror("Team Full", f"{team} team already has 20 players.")
            return

        # Popup for Player ID
        win = tk.Toplevel(self.root)
        win.title("Add Player")
        win.configure(bg="black")
        win.grab_set()

        tk.Label(win, text=f"{team} TEAM - Slot {slot}", fg="deepskyblue",
                 bg="black", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Label(win, text="Player ID:", fg="white", bg="black").pack()
        id_entry = tk.Entry(win)
        id_entry.pack(pady=5)
        id_entry.focus_set()

        tk.Label(win, text="Codename (only needed if new):", fg="white", bg="black").pack()
        name_entry = tk.Entry(win)
        name_entry.pack(pady=5)

        tk.Label(win, text="Equipment ID:", fg="white", bg="black").pack()
        equip_entry = tk.Entry(win)
        equip_entry.pack(pady=5)

        def save():

            pid_text = id_entry.get().strip()
            if not pid_text.isdigit():
                messagebox.showerror("Invalid", "Player ID must be an integer.")
                win.lift()
                win.focus_force()
                return

            player_id = int(pid_text)

            equip_text = equip_entry.get().strip()
            if not equip_text.isdigit():
                messagebox.showerror("Invalid", "Equipment ID must be an integer.")
                win.lift()
                win.focus_force()
                return
            equipment_id = int(equip_text)
            
            for table_check in (self.red_table, self.green_table):
                for row in table_check.get_children():
                    vals = table_check.item(row, "values")
                    if str(vals[1]) == str(equipment_id):
                        messagebox.showerror("Duplicate Equipment ID",
                        f"Equipment ID {equipment_id} already exists.")
                        win.lift()
                        win.focus_force()
                        return
                        
            for table_check in (self.red_table, self.green_table):
                for row in table_check.get_children():
                    slot_val, equip_val, name_val = table_check.item(row, "values")

                    if name_val == "":
                        continue  

                    existing_pid = db.get_player_id(self.conn, name_val)  
                    if existing_pid == player_id:
                        messagebox.showerror("Duplicate Player",
                                            f"Player ID {player_id} is already in the game.")
                        win.lift()
                        win.focus_force()
                        return

            # Query DB for existing codename
            existing_name = db.get_codename(self.conn, player_id)

            if existing_name:
                codename = existing_name
            else:
                codename = name_entry.get().strip()
                if codename == "":
                    messagebox.showerror("Invalid", "New player requires a codename.")
                    return
                # Insert into DB if not found
                db.insert_player(self.conn, player_id, codename)

            # Update GUI table with codename
            table.item(item_id, values=(slot, equipment_id, codename))
            udp.broadcastEquipmentID(equipment_id)
            win.destroy()

        tk.Button(win, text="Save", command=save, bg="black", fg="lime",
                  bd=2, relief="solid", padx=16, pady=6).pack(pady=10)

        win.bind("<Return>", lambda e: save())
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    PlayerEntry(root)
    root.mainloop()
