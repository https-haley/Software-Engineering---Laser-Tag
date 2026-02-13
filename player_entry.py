import tkinter as tk
from tkinter import ttk

class PlayerEntry:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Entry Terminal")
        self.root.geometry("1080x720")
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
        self.create_bottom_bar()
        self.bind_function_keys()

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
    def f2_game_params(self):    print("F2 Game Parameters")
    def f3_start_game(self):     print("F3 Start Game")
    def f5_preentered(self):     print("F5 PreEntered Games")
    def f7_unused(self):         print("F7 pressed")
    def f8_view_game(self):      print("F8 View Game")
    def f10_flick_sync(self):    print("F10 Flick Sync")
    def f12_clear_game(self):
        print("F12 Clear Game")

        
        for table in (self.red_table, self.green_table):
            for item_id in table.get_children():
                slot, _name = table.item(item_id, "values")
                table.item(item_id, values=(slot, ""))

    def delete_selected_player(self):
        print("Delete selected player")
        selected = self.red_table.selection()
        table = self.red_table
        if not selected:
            selected = self.green_table.selection()
            table = self.green_table

        if selected:
            item_id = selected[0]
            slot, _name = table.item(item_id, "values")
            table.item(item_id, values=(slot, ""))

    def manual_insert_player(self):
        print("Manual insert player (Insert key)")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PlayerEntry()
    app.run()
