from time import sleep
import pyautogui
while True:
    f = open("spam.txt", "r")
    pyautogui.write(f.read())
    pyautogui.press("Enter")
    sleep(0.4)