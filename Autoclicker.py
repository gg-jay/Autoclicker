# import module from file system
from tkinter import *
from tkinter import ttk
import ctypes
import time

mouse = ctypes.windll.user32
state = False

def StateFalse():
    global state
    global X
    if state == True:
        state = True
        X = 0

def StateTrue():
    global state
    global X
    if state == True:
        state = True
    else:
        x = 0
        state = True

root = Tk()
root.title("Autoclicker")
root.resizable(width=False, height=False)

amount = StringVar()
speed = StringVar()

amount.set(0)
speed.set(100)
mainframe = ttk.Frame(root)
mainframe.grid(padx=5, pady=5)

amountLabel = ttk.Label(mainframe, text ="Number of Clicks\n(set to 0 for infinite)").grid(column=1, row=1, sticky=W)
speedLabel = ttk.Label(mainframe, text="Click interval\n(In milliseconds)").grid(column=1, row=2, sticky=W)
amountEntry = ttk.Entry(mainframe, textvariable=amount, width=5).grid(column=2, row=1)
speedEntry = ttk.Entry(mainframe, textvariable=speed, width=5).grid(column=2, row=2)
startButton = ttk.Button(mainframe, text="Start", width=10, command=StateTrue).grid(column=1, row=3, columnspan=2, sticky=W)
stopButton = ttk.Button(mainframe, text="Stop", width=10, command=StateFalse).grid(column=2, row=3, columnspan=2,sticky=E)

mainframe.bind("<F1>",StateTrue())
mainframe.bind("<F3>",StateFalse())

timekeeper = 0
X = 0

while True:
    timekeeper += 1
    if state == True:
        Amount = int(amount.get())
        Speed = int(speed.get())
        print(state)
        if Amount == 0:
            time.sleep(Speed / 1000)
            mouse.mouse_event(2, 0, 0, 0, 0) #left mouse button down
            mouse.mouse_event(4, 0, 0, 0, 0) #left mouse button up
            X += 1
            print("Clicked %s Times" % (X))

        elif X < Amount and state == True:
            time.sleep(Speed / 1000)
            mouse.mouse_event(2, 0, 0, 0, 0) # left mouse button down
            mouse.mouse_event(4, 0, 0, 0, 0) # left mouse button up
            X += 1
            print("Clincked %s Times" % (X))
            if X == Amount:
                state = False