from tkinter import *
import tkinter as tk


class GUI:

    updatedVariable = 0

    def __init__(self, root):
        updatebutton = tk.Button(text=self.updatedVariable, command=self.increment)
        quitbutton = tk.Button(text="Quit Program", command=quit, fg="light grey", bg='dark red')
        quitbutton.pack(side=BOTTOM, fill=X)
        updatebutton.pack(side=TOP, fill=X)

    def increment(self):
        self.updatedVariable += 1
        print(self.updatedVariable)
        # Prints just for debugging purposes
        self.updatebutton.config(text=self.updatedVariable)


root = Tk()
# root serves as a reference to the main window that is open in the program

root.geometry("400x300")
# .geometry allows the size of the window to be determined
root.title("1.5.2 GUI")

GUI = GUI(root)
# I am currently unsure why this fixed my program,
# but I know it works here and was taken from my previous attempt at tkinter
root.mainloop()
