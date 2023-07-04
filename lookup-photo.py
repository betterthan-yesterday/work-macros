from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import time

pag.PAUSE = 0.5

while True:

    filename = input("File name: ")

    # Get info from MCM_PHOTOLOOKUP
    chrome = webdriver.Chrome()
    chrome.get('https://csprd.mcmaster.ca/psc/prcsprd_3/EMPLOYEE/SA/q/?ICAction=ICQryNameURL=PUBLIC.MCM_PHOTO_LOOKUP')

    pag.write("polw")
    pag.press("tab")
    pag.write("Baconator4000")
    pag.press("enter")

    time.sleep(2)

    pag.write(filename)
    pag.press("enter")

    data = chrome.find_elements(By.CLASS_NAME, "PSQRYRESULTSODDROW")
    text = []
    for dat in data[1:-1]:
        if dat.text == " ":
            text.append("0")
        else:
            text.append(dat.text)

    # Input into spreadsheet
    chrome.close()
    pag.hotkey("alt", "tab")
    for tex in text:
        pag.write(tex)
        pag.press("right")

    # Repeat
    pag.press("down")
    pag.hotkey("ctrl", "c")
    pag.hotkey("ctrl", "left")
    pag.hotkey("alt", "tab")
    pag.hotkey("ctrl", "v")
    pag.press("enter")

