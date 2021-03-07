from pyautogui import *
import pyautogui
import random
import keyboard
import win32api, win32con
import time


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

print("Program running!")

while keyboard.is_pressed('x') == False:

    if pyautogui.pixel(720, 314)[0] == 0:
        click(720, 314)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(873, 311)[0] == 0:
        click(873, 311)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(1027, 309)[0] == 0:
        click(1027, 309)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(1199, 309)[0] == 0:
        click(1199, 309)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(709, 477)[0] == 0:
        click(709, 477)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(861, 467)[0] == 0:
        click(861, 467)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(1027, 466)[0] == 0:
        click(1027, 466)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(1160, 475)[0] == 0:
        click(1160, 475)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(879, 626)[0] == 0:
        click(879, 626)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(1017, 635)[0] == 0:
        click(1017, 635)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(1169, 640)[0] == 0:
        click(1169, 640)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(724, 627)[0] == 0:
        click(724, 627)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(881, 791)[0] == 0:
        click(881, 791)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(682, 798)[0] == 0:
        click(682, 798)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(992, 792)[0] == 0:
        click(992, 792)
        time.sleep(0.01)
        print("Tile clicked!")
    if pyautogui.pixel(1191, 798)[0] == 0:
        click(1191, 798)
        time.sleep(0.01)
        print("Tile clicked!")

while keyboard.is_pressed('x'):
    print("Program stopped!")
    time.sleep(10)
