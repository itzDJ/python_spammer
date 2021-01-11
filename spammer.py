import pyautogui
import time

time.sleep(2)
num = -1
while num != 0:
    pyautogui.typewrite("test")
    pyautogui.press("enter")
    time.sleep(0.5)
