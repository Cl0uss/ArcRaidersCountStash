import tkinter as tk
from tkinter import simpledialog
import pyautogui as p
import keyboard
import time
from collections import deque


def ask_monitor():
    root = tk.Tk()
    root.title("Select monitor")
    result = None

    def choose(val):
        nonlocal result
        result = val
        root.destroy()

    tk.Label(root, text="On which monitor you got game opened?").pack(pady=10)
    tk.Button(root, text="Left", width=10, command=lambda: choose("left")).pack(side="left", padx=20, pady=10)
    tk.Button(root, text="Right", width=10, command=lambda: choose("right")).pack(side="right", padx=20, pady=10)

    root.mainloop()
    return result


def ask_items():
    root = tk.Tk()
    root.withdraw()

    number = simpledialog.askinteger(
        "Items in stash",
        "Write how many items you have in stash right now:"
    )

    root.destroy()
    return number


def show_popup():
    root = tk.Tk()
    root.title("Instructions")

    msg = ("After pressing 'Okay' your game should be opened on stash\n"
           "To start program press 'S'\n"
           "To stop program press 'X' for 1 second")
    tk.Label(root, text=msg, padx=15, pady=15).pack()

    tk.Button(root, text="Okay", width=12, command=root.destroy).pack(pady=10)

    root.mainloop()


# --- START ---

monitor = ask_monitor()

if monitor == 'left':
    xStart, yStart, xNext = 196, 315, 586
elif monitor == 'right':
    xStart, yStart, xNext = 2116, 315, 2504
else:
    raise SystemExit("No monitor selected")
print(f'Game on {monitor} monitor')
itemsCount = ask_items()

if itemsCount is None:
    raise SystemExit("No number entered")

print("Items in stash:", itemsCount)

show_popup()
stopped = False
print("Waiting for S...")
while not keyboard.is_pressed('s'):
        if keyboard.is_pressed('x'):
            stopped = True
            print("Stopped by user!")
            break


itemsInRow = 1
xCurr = xStart
yCurr = yStart
yNext = deque([372, 426, 481, 536, 590, 645, 699, 754, 809, 863, 893])
if not stopped:
    print("Starting...")
    p.keyDown('ctrl')
    for i in range (1,itemsCount+1):
        if keyboard.is_pressed('x'):
            print("Stopped by user!")
            break
        if i % 24 == 1 and i != 1:
            p.moveTo(xNext,yNext.popleft())
            p.click()
            time.sleep(0.8)
            xCurr, yCurr, itemsInRow = xStart, yStart, 
        if itemsInRow > 4:
            xCurr = xStart
            yCurr += 100
            itemsInRow = 1
        p.moveTo(xCurr,yCurr) 
        p.click()
        xCurr += 100
        itemsInRow +=1
    p.keyUp('ctrl')
