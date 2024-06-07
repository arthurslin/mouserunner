import pyautogui
import time
import random

def mouse_run():
    screen_width, screen_height = pyautogui.size()
    y = random.randint(0,screen_height)
    x = random.randint(0,screen_width)

    pyautogui.moveTo(x,y,duration=random.uniform(0.5,1.5))

try:
    while True:
        mouse_run()
        time.sleep(random.uniform(1,5))
except KeyboardInterrupt:
    print("Over")
