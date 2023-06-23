import pyautogui as pag
import time

"""
Use: Windows
"""

pag.PAUSE = 0.25
pag.FAILSAFE = True

# Start
pag.hotkey("alt", "tab")


while True:
    pag.press("down")

    # Edit photo
    pag.hotkey("shift", "f10")
    pag.press("down", presses=3)
    pag.press("enter")

    time.sleep(15)
    pag.hotkey("alt", "tab")
    time.sleep(1)
