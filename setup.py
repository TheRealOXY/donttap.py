import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
from tkinter.ttk import *
import os

root = tk.Tk()

def setApp():
    os.system('codesetup.bat')

canvas = tk.Canvas(root, height=7, width=52, bg="#FFFFFF")
canvas.pack()

button = tk.Button(root, text="Setup", padx=50, pady=5, bg="#389474", fg="#FFFFFF", font='families 10 bold', command=setApp)

button.pack()

root.mainloop()
