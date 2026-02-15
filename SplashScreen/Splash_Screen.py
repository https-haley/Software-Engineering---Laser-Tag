import tkinter as tk
from PIL import Image, ImageTk #pip install Pillow
from playerentry import PlayerEntry

SPLASH_MS = 3000 # 3 seconds
WINDOWN_SIZE_X = 400 
WINDOW_SIZE_Y = 300

class SplashScreen(tk.Toplevel):
        def __init__(self, parent, image_path: str, duration_ms: int, on_close):
            super().__init__(parent)
            self.on_close = on_close

            #splash screen
            self.overrideredirect(True) # remove title bar
            self.configure(bg="black") # background color
            self.attributes("-topmost", True) # keep on top of other windows
                
            # load, resize and display image
            image = Image.open(image_path)
            image = image.resize((600, 350), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(image) # store as self.photo to avoid garbage collection

            #size and center window to image
            w, h = image.size
            screen_w = self.winfo_screenwidth()
            screen_h = self.winfo_screenheight()
            x = (screen_w - w) // 2
            y = (screen_h - h) // 2
            self.geometry(f"{w}x{h}+{x}+{y}")

            # image on window
            tk.Label(self, image=self.photo, bg="black").pack()

            # close after SPLASH_MS
            self.after(duration_ms, self.close)

        def close(self):
            self.destroy() # close splash screen
            self.on_close()
            
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # hide window while splash screen is active
        self.withdraw()
        #window
        self.title("Photon Laser Tag")
        self.geometry(f"{WINDOW_SIZE_X}x{WINDOW_SIZE_Y}") # player entry form size

        # show splash screen, then player entry
        SplashScreen(
            parent = self,
            image_path = "logo.jpg",
            duration_ms = SPLASH_MS,
            on_close = self.show_player_entry
        )
    def show_player_entry(self):
         self.deiconify() # show main window
         PlayerEntry(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()

