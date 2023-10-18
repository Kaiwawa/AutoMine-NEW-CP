from random import randint
from pyautogui import leftClick, press
from time import sleep
from tkinter import *
import threading
import traceback


class Run:
    def __init__(self):
        self.running = False

    def loop(self):
        try:
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
        except Exception as e:
            traceback.print_exc()

    def on(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.loop)
            self.thread.start()

    def off(self):
        self.running = False


root = Tk()
root.title("Clube Penguin Auto Mine v0.2")
root.geometry("500x300")

root.iconbitmap("icon.ico")

label = Label(root, text="CP Auto Mine", fg="Black", font=("Arial", 32))
label.pack()

intro_label = Label(root, text="Click Start or Stop", font=("Calibri", 13) )
intro_label.pack()

app = Run()

button_frame = Frame(root)
button_frame.pack(side=TOP)

start = Button(button_frame, text="Start", command=app.on, width=15, cursor='hand2')
start.pack(side=LEFT, pady=50)

stop = Button(button_frame, text="Stop", command=app.off, width=15, cursor='hand2')
stop.pack(side=LEFT, padx=10)

label = Label(root, text="Made by Kaiwawa", fg="Black", font=("Arial", 8) )
label.pack(side=BOTTOM,padx=15,pady=15)

root.attributes("-topmost", True)

root.mainloop()

# PRINT SAVE
# print(pyautogui.position())
# print(getValueX)
# print(getValueY)

# POS SAVE 1920x1080
# Profile 1222 975
# Puffle Tricks 539 967
# Puffle Bag 534 874
# Pos 1 = 1144 881
# Pos 2 = 787 751
