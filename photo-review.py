import pyautogui as pag
import time

"""
Use: Anywhere
"""

# Start
pag.hotkey("alt", "tab")

pag.press("down")

# Edit photo
pag.hotkey("shift", "f10")
pag.press("down", presses=3)
pag.press("enter")
