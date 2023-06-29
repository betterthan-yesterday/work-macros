import pyautogui as pag

"""
Use: Anywhere
"""

pag.hotkey("alt", "tab")

# Fill query
pag.write("MCMST")
pag.press("tab", presses=2)
pag.write("UGRD")
pag.press("tab", presses=2)

pag.hotkey("ctrl", "shift", "tab")
pag.hotkey("ctrl", "c")
pag.hotkey("ctrl", "tab")
pag.hotkey("ctrl", "v")
pag.press("tab")

for i in range(2):
    pag.hotkey("ctrl", "shift", "tab")
    pag.press("right")
    pag.hotkey("ctrl", "c")
    pag.hotkey("ctrl", "tab")
    pag.hotkey("ctrl", "v")
    pag.press("tab")

pag.write("2239")
pag.press("tab", presses=2)
pag.write("2241")
