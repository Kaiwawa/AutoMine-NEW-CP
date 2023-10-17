from random import randint
from pyautogui import leftClick, press
from time import sleep
from tkinter import *
import threading


class Run:
    def __init__(self):
        self.running = False

    def loop(self):
        while self.running:
            leftClick(534, 970)
            sleep(0.3)
            leftClick(534, 875)

            getValueX = randint(787, 1144)
            getValueY = randint(751, 881)
            leftClick(getValueX, getValueY)
            sleep(2)
            press("d")

            sleep(120)

    def on(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.loop)
            self.thread.start()

    def off(self):
        self.running = False


root = Tk()
root.title("New CP Auto Mine")
root.geometry("500x300")

root.iconbitmap('icon.ico')

label = Label(root, text="CP Auto Mine", fg="Black", font=("Arial", 32))
label.pack()

intro_label = Label(root, text="Click Start or Stop", font=('Calibri', 13))
intro_label.pack()

app = Run()

start = Button(root, text="Start", command=app.on)
start.pack(pady=50)

stop = Button(root, text="Stop", command=app.off)
stop.pack(padx=10)

root.attributes("-topmost", True)  # Keep the window on top

root.mainloop()

# PRINT SAVE
# print(pyautogui.position())
# print(getValueX)
# print(getValueY)

# POS SAVE
# Profile 1222 975
# Puffle Tricks 539 967
# Puffle Bag 534 874
# Pos 1 = 1144 881
# Pos 2 = 787 751
