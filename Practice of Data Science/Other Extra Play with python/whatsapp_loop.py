import pyautogui as gui
import time

message = input('Enter The Message')
number = input("Enter The number of time to send Message")
time.sleep(5)
for i in range(int(number)):
    gui.typewrite(message)
    gui.press('Enter')   