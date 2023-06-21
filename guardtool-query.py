import pyautogui as pag

pag.hotkey("alt", "tab")

# Fill query
pag.write("MCMST")
pag.press("tab", presses=2)
pag.write("UGRD")
pag.press("tab", presses=2)
pag.write("50")
pag.press("tab")
pag.write("2023-06-08-23:59")
pag.press("tab")
pag.write("2023-06-09-23:59")
pag.press("tab")
pag.write("2239")
pag.press("tab", presses=2)
pag.write("2241")
pag.press("enter")
