import pyautogui as pag
import time

"""
time.sleep(5)
pag.typewrite("Geeks For Geeks!")
pag.press("enter")
pag.hotkey("command","v")
pag.hotkey("command","a")
"""

# Start
pag.hotkey("alt", "tab")

pag.press("down")

# Edit photo
pag.hotkey("shift", "f10")
pag.press("down", presses=3)
pag.press("enter")
