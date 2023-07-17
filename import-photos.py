import pyautogui as pag
import time

"""
Uses: On GuardTool Importer
"""

pag.PAUSE = 0.1
pag.hotkey("alt", "tab")

# Window 1
pag.press("space")
pag.press("enter")

# Window 2
pag.press("down")
pag.press("tab")
pag.press("p")
pag.press("tab", presses=2)
pag.press("space")
pag.press("tab", presses=3)
pag.press("enter")

# Window 3
pag.press("tab", presses=3)
pag.press("p")
pag.press("tab")
pag.press("p")
pag.keyDown('shift')
pag.press("tab", presses=3)
pag.keyUp("shift")
pag.press("space")

pag.press("tab", presses=2)
pag.press("c")
pag.press("tab", presses=1)
pag.press("c", presses=2)
pag.keyDown('shift')
pag.press("tab", presses=3)
pag.keyUp("shift")
pag.press("space")

pag.press("tab", presses=5)
pag.press("space")

# Window 4
pag.press("p", presses=2)
pag.press("tab", presses=1)
pag.press("p", presses=1)
pag.press("tab", presses=2)
pag.press("space")
pag.press("tab", presses=3)
pag.press("space")

# Window 5
pag.write("Y:\CSPRD")
pag.press("tab", presses=3)
pag.press("space")
pag.press("tab", presses=3)
pag.press("space")

# Window 6
