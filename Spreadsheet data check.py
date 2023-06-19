# used to access time related functions
import time
import pyautogui as pag

time.sleep(1)

# Copy from spreadsheet
pag.press("enter")
pag.hotkey("command", "c")

# Paste in Mosaic
pag.hotkey("ctrl", "tab")
pag.moveTo(121, 547)
pag.click()
time.sleep(0.5)
pag.hotkey("command", "v")
pag.press("enter")

# Check data
time.sleep(1)
pag.moveTo(127, 721)
pag.click()

# Return

"""
time.sleep(5)
pyautogui.typewrite("Geeks For Geeks!")
pyautogui.press("enter")
pyautogui.hotkey("command","v")
pyautogui.hotkey("command","a")
"""
