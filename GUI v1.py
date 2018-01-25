from tkinter import *
import tkinter as tk


class GUI:

    def __init__(self, root):
        updatebutton = tk.Button(text="CLICK HERE",)
        quitbutton = tk.Button(text="Quit Program", command=quit, fg="light grey", bg='dark red')
        quitbutton.pack(side=BOTTOM, fill=X)
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
