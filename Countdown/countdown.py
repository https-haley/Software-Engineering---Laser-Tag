import tkinter as tk
from PIL import Image, ImageTk
import os
class Countdown:
    def __init__(self, root, duration=30, on_complete=None):
        self.duration = duration
        self.root = root
        self.root.title("Game Starting Soon")
        self.root.configure(bg="black")
        self.count = duration
        self.on_complete = on_complete

        # Clear previous screen
        for widget in self.root.winfo_children():
            widget.destroy()

        self.image_dir = os.path.join(os.path.dirname(__file__), "Countdown_Images")

        self.image_label = tk.Label(self.root, bg="black")
        self.image_label.pack()
        self.update_image()

    def update_image(self):
        if self.count >= 0:
            image_path = os.path.join(self.image_dir, f"{self.count}.tif")
            img = Image.open(image_path)
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference to prevent garbage collection
            self.count -= 1
            self.root.after(1000, self.update_image)  # Schedule next update after 1 second
        else:
            if self.on_complete:
                self.on_complete()  # Call the completion callback if provided

            
