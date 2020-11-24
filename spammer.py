import pyautogui
import time

y = 0
time.sleep(1)
order = input("The time has come...\n")
if order == "Execute order 66...":
    time.sleep(2)
    while y != -1:
        y += 1
        pyautogui.typewrite("legit")
        pyautogui.press("enter")
        print(y)
        time.sleep(0.5)
else:
    print("Wrong order...")
