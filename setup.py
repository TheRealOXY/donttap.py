import time
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
from tkinter.ttk import *
import os

root = tk.Tk()

def setApp():
    os.system('pip install pywin32')
    os.system('pip install keyboard')
    os.system('pip install pyautogui')
    os.system('pip install opencv-python')

def closeApp():
    print('Setup canceled')
    time.sleep(0.2)
    root.destroy()

def debugApp():
    os.system('pip uninstall pywin32')
    os.system('pip uninstall keyboard')
    os.system('pip uninstall pyautogui')
    os.system('pip uninstall opencv-python')
    time.sleep(1)
    os.system('pip install pywin32')
    os.system('pip install keyboard')
    os.system('pip install pyautogui')
    os.system('pip install opencv-python')
    os.system('ECHO Program debuged')

canvas = tk.Canvas(root, height=0, width=50, bg="#FFFFFF")
canvas.pack()

button = tk.Button(root, text="Setup", padx=50, pady=5, bg="#389474", fg="#FFFFFF", font='families 10 bold', command=setApp)
button.pack()

button2 = tk.Button(root, text="Debug", padx=47.9, pady=5, bg="#387794", fg="#FFFFFF", font='families 10 bold', command=debugApp)
button2.pack()

button3 = tk.Button(root, text="Close", padx=50.5, pady=5, bg="#943838", fg="#FFFFFF", font='families 10 bold', command=closeApp)
button3.pack()

root.mainloop()
