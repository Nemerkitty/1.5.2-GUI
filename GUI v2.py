from tkinter import *
from random import *
import tkinter as tk


class GUI:

    totalBalance = randint(100, 10000)
    # creates a random value to be used in the account balance
    shownbalance = False


    def displaylabel(self):
        if self.shownbalance == False:
            balance = tk.Label(text=self.totalBalance)
            balance.pack(side=TOP)
            self.shownbalance = True

    def __init__(self, root):
        updatebutton = tk.Button(text="Click to view account balance", command=lambda: self.displaylabel())
        # using lambda is a solution to the button running the method instantly
        # still fairly unsure about how lambda works, will need to look more into it
        quitbutton = tk.Button(text="Quit Program", command=quit, fg="light grey", bg='dark red')
        quitbutton.pack(side=BOTTOM)
        updatebutton.pack(side=TOP, fill=X)


root = Tk()
# root serves as a reference to the main window that is open in the program

root.geometry("400x300")
# .geometry allows the size of the window to be determined
root.title("1.5.2 GUI")

GUI = GUI(root)
# I am currently unsure why this fixed my program,
# but I know it works here and was taken from my previous attempt at tkinter

root.mainloop()

