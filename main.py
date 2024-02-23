import tkinter.messagebox
from tkinter import *
from random import shuffle, randint, choice
import json

# TODO : 1- UI SETUP
window = Tk()
window.title("lear spanish with flash cards")
window.config(padx=50, pady=50)
canvas = Canvas(window, width=200, height=200)
canvas.pack()
window.mainloop()