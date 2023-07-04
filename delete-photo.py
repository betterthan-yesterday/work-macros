import pyautogui as pag
import time

"""
Use: 16:9 fullscreen browser
"""

pag.PAUSE = 1
pag.FAILSAFE = True

pag.hotkey("alt", "tab")

while True:
    # Get and paste student number into query
    pag.hotkey("ctrl", "c")
    pag.hotkey("ctrl", "tab")
    pag.hotkey("ctrl", "a")
    pag.hotkey("ctrl", "v")
    pag.press("enter")

    # Delete
    time.sleep(4)

    # Return
    pag.hotkey("alt", "2")
    pag.hotkey("ctrl", "shift", "tab")

    # Record
    pag.hotkey("ctrl", "right")
    pag.press("right")
    pag.write("yes")
    pag.press("enter")
    pag.press("left")
    pag.hotkey("ctrl", "left")
    pag.hotkey("ctrl", "left")
