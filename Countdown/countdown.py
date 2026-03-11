import tkinter as tk
from PIL import Image, ImageTk
import os
class Countdown:
    def __init__(self, duration=30):
        self.duration = duration
        self.root = tk.Tk()
        self.root.title("Game Starting Soon")
        self.root.configure(bg="black")
        self.count = 30

        self.imafe_dir = os.path.join(os.path.dirname(__file__), "Countdown_Images")

        self.image_label = tk.Label(self.root, bg="black")
        self.image_label.pack()
        self.update_image()

    def update_image(self):
        if self.count >= 0:
            image_path = os.path.join(self.imafe_dir, f"{self.count}.tif")
            img = Image.open(image_path)
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference to prevent garbage collection
            self.count -= 1
            self.root.after(1000, self.update_image)  # Schedule next update after 1 second
        else:
            self.root.destroy()  # Close the window when countdown is finished
            if self.on_complete:
                self.on_complete()  # Call the completion callback if provided
        def run(self):
            self.root.mainloop()
if __name__ == "__main__":
    app = Countdown()
    app.run()
            