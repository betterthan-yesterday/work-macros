import pyautogui as pag

"""
Use: 16:9 fullscreen browser
"""

pag.hotkey("alt", "tab")

# Get and paste student number into query
pag.hotkey("ctrl", "c")
pag.hotkey("ctrl", "tab")
pag.hotkey("ctrl", "a")
pag.hotkey("ctrl", "v")
pag.press("enter")

pag.mo
