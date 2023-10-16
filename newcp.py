from random import randint
from pyautogui import leftClick, press
from time import sleep

def PetBag():
    leftClick(534, 970),
    sleep(0.3),
    leftClick(534, 875)

def Mine():
    getValueX = randint(787, 1144)
    getValueY = randint(751, 881)
    leftClick(getValueX, getValueY)
    sleep(2)
    press("d")

sleep(3)

while True:

    Mine()
    PetBag()
    sleep(120)
    PetBag()

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