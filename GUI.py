# Uses the installer class to check for and install missing modules
import installer

install = installer.Installer()
install.install_required_modules()

import tkinter as tk
import mouse
import time
from sys import maxsize
import ExitSplash as ES

# The main housing for both the GUI and the entire program
class GUI(tk.Frame):
    # Contains all instance variables used throughout the GUI
    def __init__(self, master=None):
        super().__init__(master)

        # The x cooridnate for the Desired Position
        self.x = tk.IntVar()
        self.x.set(0)

        # The y cooridnate for the Desired Position
        self.y = tk.IntVar()
        self.y.set(0)

        # Used to determine if the user wants the clicker to run indefinitely
        self.infinite = tk.IntVar()
        self.infinite.set(0)

        # Used to determine if the user wants to clicker to double click with every click the clicker does
        self.doubleVar = tk.IntVar()
        self.doubleVar.set(0)

        # Used to determine the length of time in seconds the user wants to run the clicker if they do not select infinite
        self.lengthVar = tk.IntVar()
        self.lengthVar.set(0)

        # Used to determine the amount of delay in milliseconds between clicks the user wants
        self.delayVar = tk.IntVar()
        self.delayVar.set(0)

        # Used for displaying the current position of the mouse on a label
        self.mousePosVar = tk.StringVar()
        self.mousePosVar.set("Current Mouse Position "+str(mouse.get_position()))

        # Used to determine which button the mouse uses when the clicker runs
        self.mouseButtonVar = tk.StringVar()
        self.mouseButtonVar.set("Left")

        # The options for buttons on the mouse the user has
        self.mouseButtonOptions = ["Left", "Middle", "Right"]

        # Used for emergency stops when the clicker is running
        self.stopClickingVar = False

        # Used to update the timer label
        self.timerVar = tk.StringVar()
        self.timerVar.set("Time left: " + str(0.0))

        self.master = master
        self.pack()
        self.create_widgets()
        self.displayCurrentMousePos()
    
    # Used as a button command to send the mouse to the Desired Location
    def sendMouse(self):
        mouse.move(self.x.get(), self.y.get())
    
    # Used as to call the mouse.move function and begin the loop that clicks the mouse with the desired settings, it also handles the timer and displaying the timer
    def startSendClicking(self, start, firstRun=True):
        # Used as a local variable used to make sure that the IntVar that affects the length entry isn't touched so that infinite can run without displaying the sys.maxsize
        trueLength = self.lengthVar.get()
        # Used to store the condition of whether the user chose the clicker to run idefinitely or not
        infinite = bool(self.infinite.get())
        # Used to assign the mouse type for clicking
        mouse_type = mouse.LEFT
        # Used to determine whether normal or double clicks are used
        click_type = bool(self.doubleVar.get())
        # The current time
        current = time.time()
        # The time that has passed since the loop started
        elapsed = current - start

        # Uses the param to send the mouse to the desired location when the loop runs for the first time, this is done to keep the mouse unlocked
        if firstRun:
            self.sendMouse() 
        
        # Allows the loop to run indefinitely but with an escape determine by the user
        if infinite and not self.stopClickingVar:
            trueLength = maxsize
        else:
            trueLength = self.lengthVar.get()
            self.stopClickingVar = False
        
        # Sets which mouse button is used in the auto clicker class function
        if self.mouseButtonVar.get() == "Left":
            mouse_type = mouse.LEFT
        elif self.mouseButtonVar.get() == "Middle":
            mouse_type = mouse.MIDDLE
        else:
            mouse_type = mouse.RIGHT
        
        # A call to the autoclicker class function
        if click_type:
            mouse.double_click(mouse_type)
        else:
            mouse.click(mouse_type)
        
        # The recursive part of the loop, it contains a failsafe so that if the user moves the mouse by at least ten pixels in any direction the clicker stops
        if elapsed <= trueLength and not ((mouse.get_position()[0] > (self.x.get() + 10) or mouse.get_position()[0] < (self.x.get() - 10)) and (mouse.get_position()[1] > (self.y.get() - 10) or mouse.get_position()[1] < (self.y.get() + 10))):
            if self.delayVar.get() > 0:
                self.timerVar.set("Time left: " + str(round(self.lengthVar.get() - elapsed, 1)))
                self.after(self.delayVar.get(), self.startSendClicking, start, False)
            else:
                self.after_idle(self.startSendClicking, start, False)
        else:
            self.timerVar.set("Time left: " + str(0.0))
    
    # Sets the current mouse position to the desired one
    def getCurrentMousePos(self, event=' '):
        self.x.set(mouse.get_position()[0])
        self.y.set(mouse.get_position()[1])
    
    # Recursively displays the current mouse position
    def displayCurrentMousePos(self):
        self.mousePosVar.set("Current Mouse Position "+str(mouse.get_position()))
        self.after(1, self.displayCurrentMousePos)

    # Forces the clicker to stop with a keyboard button press
    def stopClicking(self, event=' '):
        self.stopClickingVar = True
        self.lengthVar.set(0)
    
    # The emergency quit for the clicker, skips the exit splash
    def quitClicker(self, event=' '):
        quit()
    
    # Creates all of the widgets used in the GUI
    def create_widgets(self):
        # A label to mark the purpose of the associated entries below for the user
        self.setPosLabel = tk.Label(self, text="Desired Position(X,Y)")
        self.setPosLabel.grid(row=0, column=0, sticky=tk.N, padx=5, pady=5)

        # An entry for the user to set the x coordinate for the desired position
        self.setXEntry = tk.Entry(self, textvariable=self.x, justify=tk.RIGHT)
        self.setXEntry.grid(row=0, column=1, sticky=tk.N, padx=5, pady=5)

        # An entry for the user to set the y coordinate for the desired position
        self.setYEntry = tk.Entry(self, textvariable=self.y, justify=tk.RIGHT)
        self.setYEntry.grid(row=0, column=2, sticky=tk.N, padx=5, pady=5)

        # A button for the user to test mouse coordinates by sending the mouse to the coordinates
        self.sendMouseButton = tk.Button(self, text="Send Mouse", command=self.sendMouse)
        self.sendMouseButton.grid(row=0, column=3, sticky=tk.N, padx=5, pady=5)

        # The checkbox that allows the user to make the clicker run indefinitely
        self.infiniteCheckButton = tk.Checkbutton(self, text="Infinite", variable=self.infinite, onvalue=1, offvalue=0)
        self.infiniteCheckButton.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        # The checkbox that allows the user to select whether the clicks the clicker does is normal or double
        self.doubeCheckButton = tk.Checkbutton(self, text="Double", variable=self.doubleVar, onvalue=1, offvalue=0)
        self.doubeCheckButton.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # A label to mark the purpose of the following entry for the user
        self.lengthLabel = tk.Label(self, text="Length(s)")
        self.lengthLabel.grid(row=2, column=0, sticky=tk.S, padx=5, pady=5)

        # An entry for the user to set the length the program runs for
        self.lengthEntry = tk.Entry(self, textvariable=self.lengthVar, justify=tk.RIGHT)
        self.lengthEntry.grid(row=2, column=1, sticky=tk.S, padx=5, pady=5)

        # A label that displays the current timer length
        self.timerLabel = tk.Label(self, textvariable=self.timerVar)
        self.timerLabel.grid(row=2, column=2, sticky=tk.S, padx=5, pady=5)

        # A label to mark the purpose of the following entry for the user
        self.delayLabel = tk.Label(self, text="Delay(ms)")
        self.delayLabel.grid(row=3, column=0, sticky=tk.S, padx=5, pady=5)

        # An entry for the user to set the delay for the clicker to use inbetween clicks
        self.delayEntry = tk.Entry(self, textvariable=self.delayVar, justify=tk.RIGHT)
        self.delayEntry.grid(row=3, column=1, sticky=tk.S, padx=5, pady=5)

        # A drop down menu for the user to select which mouse button is used in the clicker
        self.mouseButtonOptionMenu = tk.OptionMenu(self, self.mouseButtonVar, *self.mouseButtonOptions)
        self.mouseButtonOptionMenu.grid(row=4, column=2, sticky=tk.E, padx=5, pady=5)

        # A button for the user to begin the clicker
        self.sendStartButton = tk.Button(self, text="Send & Start Clicking", command=lambda: self.startSendClicking(time.time()))
        self.sendStartButton.grid(row=4, column=3, sticky=tk.E, padx=5, pady=5)

        # A label that tells the user what the current position of their mouse is
        self.currentPosLabel = tk.Label(self, textvariable=self.mousePosVar)
        self.currentPosLabel.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)

        # A button that, while it works, exists only to tell the user that the control key is used to set the current mouse position as the desired one
        self.getCurrentPosButton = tk.Button(self, text="Set Desired Postion as Current Position(Press CTRL)", command=self.getCurrentMousePos)
        self.getCurrentPosButton.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)

# The run code for the GUI, it changes the window title, icon, and binds all keyboard controls as well as starting the display updating loop
root = tk.Tk()
gui = GUI(master=root)
gui.master.title("AutoClicker")
gui.master.iconbitmap("icon.ico")
gui.master.bind('<Control_L>', gui.getCurrentMousePos)
gui.master.bind('<Escape>', gui.stopClicking)
gui.master.bind('<Shift-Escape>', gui.quitClicker)
gui.master.bind('<Return>', gui.startSendClicking)
gui.master.lift()
gui.master.attributes("-topmost", True)
gui.mainloop()

# The run code for the exit splash, it changes the window title, icon, and sets the splash to stay for 3 seconds
exitroot = tk.Tk()
exitsplash = ES.ExitSplash(master=exitroot)
exitsplash.master.title("Exit Splash")
exitsplash.master.iconbitmap("icon.ico")
exitsplash.after(3000, exitroot.destroy)
exitsplash.mainloop()
