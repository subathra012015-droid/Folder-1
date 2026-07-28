import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = True  # Enable failsafe to stop the script by moving the mouse to the corner
pyautogui.PAUSE = 1  # Set a pause duration between actions

print("1. Opening Chrome Browser...")
# time.sleep(2)  # Wait for 2 seconds before starting the automation

pyautogui.hotkey('win', 'r')  # Open the Run dialog
# time.sleep(1)  # Wait for the Run dialog to open    
pyautogui.typewrite('chrome\n')  # Type 'chrome' and press Enter to open Chrome
# time.sleep(1)  # Wait for Chrome to open
pyautogui.press('enter')  # Press Enter to ensure Chrome is focused
# time.sleep(2)  # Wait for Chrome to be ready

print("2. Navigating to the website...")
pyautogui.hotkey('ctrl','t')  # Open a new tab in Chrome
# time.sleep(1)  # Wait for the new tab to open
pyautogui.typewrite('https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671\n') # Type the website URL and press Enter
# time.sleep(1)  # Wait for the website to load
pyautogui.press('enter')  # Press Enter to ensure the website is loaded
# time.sleep(1)  # Wait for the website to fully load

print("3. Copy the data from the website...")
pyautogui.hotkey('ctrl', 'a')  # Select all content on the page
# time.sleep(1)  # Wait for the selection to complete
pyautogui.hotkey('ctrl', 'c')  # Copy the selected content
# time.sleep(1)  # Wait for the copy action to complete

print("4. Opening Notepad...")
pyautogui.hotkey('win', 'r')  # Open the Run dialog again
time.sleep(1)  # Wait for the Run dialog to open
pyautogui.typewrite('Notepad\n')  # Type 'notepad' and press Enter to open Notepad
time.sleep(1)  # Wait for Notepad to open
pyautogui.press('enter')  # Press Enter to ensure Notepad is focused
time.sleep(1)  # Wait for Notepad to be ready
pyautogui.hotkey('ctrl','t')  # Open a new tab in Chrome
time.sleep(1)  # Wait for the new tab to open 
pyautogui.hotkey('ctrl', 'v')  # Paste the copied content into Notepad
time.sleep(1)  # Wait for the paste action to complete
