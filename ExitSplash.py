import tkinter as tk
from PIL import ImageTk, Image

# A splash that shows when the program exits via the window exit button
class ExitSplash(tk.Frame):
    # Declares necessary instance variables
    def __init__(self, master=None):
        super().__init__(master)

        # The image object for Linus Tech Priest
        self.img = ImageTk.PhotoImage(Image.open("Linus Tech Priest.png"))

        self.master = master
        self.pack()
        self.create_widgets()
    
    # Creates the widgets for the exit splash
    def create_widgets(self):
        # The top label of the splash
        self.topLabel = tk.Label(self, text="He is in the machine.", font=('Times New Roman Bold', 24))
        self.topLabel.pack()

        # The image of Linus Tech Priest
        self.canvas = tk.Canvas(self, width=593, height=713)
        self.canvas.pack()
        self.canvas.create_image(593/2, 713/2, image=self.img)

        # The bottom label of the splash
        self.bottomLabel = tk.Label(self, text="He will save us all.", font=('Times New Roman Bold', 24))
        self.bottomLabel.pack()