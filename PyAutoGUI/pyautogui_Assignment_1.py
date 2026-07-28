import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = True  # Enable failsafe to stop the script by moving the mouse to the corner
pyautogui.PAUSE = 1  # Set a pause duration between actions

print("1. Opening Chrome Browser...")
pyautogui.hotkey('win', 'r')  # Open the Run dialog
pyautogui.typewrite('chrome\n')  # Type 'chrome' and press Enter to open Chrome
pyautogui.press('enter')  # Press Enter to ensure Chrome is focused

print("2. Navigating to the website & Maximize the screen...")
pyautogui.typewrite('https://www.nseindia.com/static/invest/first-time-investor-stamp-duty-charges-taxes\n') # Type the website URL and press Enter
time.sleep(1)  # Wait for the website to load
pyautogui.press('enter')  # Press Enter to ensure the website is loaded
pyautogui.hotkey('alt','space') # Maximize the window
time.sleep(0.5)  # Wait for the website to fully load 
pyautogui.press('x') # Press Enter to ensure the website is loaded
# time.sleep(1)  # Wait for the website to fully load

print("3. Copy the data from the website...")
pyautogui.moveTo(595,650) # Starting position of the data to be copied
pyautogui.mouseDown() # Hold down the left mouse button to start selecting the data
time.sleep(2)  # Wait for the selection to complete
pyautogui.dragTo(2200, 1000, duration=2) # Drag to Bottom of the page to select the data
pyautogui.mouseUp() # Release the left mouse button to Excel complete the selection
time.sleep(1)  # Wait for the selection to complete

pyautogui.hotkey('ctrl', 'c')  # Copy the selected content
time.sleep(2)  # Wait for the copy action to complete
pyautogui.hotkey('alt','space') # close the Excel window
time.sleep(1)  # Wait for the window to close
pyautogui.press('c') # Press Enter to ensure the window is closed
time.sleep(2)  # Wait for the window to close

print("4. Open > Paste the copied data > Save > Close Excel")
pyautogui.hotkey('win')  # Open the Run dialog again
time.sleep(2)  # Wait for the Run dialog to open
pyautogui.write('Excel\n')  # Type 'notepad' and press Enter to open Notepad
time.sleep(2)  # Wait for Notepad to open
pyautogui.press('enter', presses=3, interval=3)  # Press Enter to ensure Notepad is focused
time.sleep(1)  # Wait for Excel to be ready
pyautogui.hotkey('ctrl', 'v')  # Paste the copied content into Notepad
time.sleep(2)  # Wait for the paste action to complete
pyautogui.hotkey('ctrl', 's')  # Save the file
pyautogui.write('NSE_Data_' + time.strftime('%Y-%m-%d')) # Write the file name and path
pyautogui.press('tab',presses=2, interval=2)  # Press Tab to navigate to the Save button
pyautogui.press('enter')  # Press Enter to save the file
pyautogui.write('Downloads') # Write the file name and path
pyautogui.press('enter')  # Press Tab to navigate to the Save button
pyautogui.press('tab',presses=2,interval=2)  # Press Enter to save the file
pyautogui.press('enter')  # Press Enter to save the file
time.sleep(2)  # Wait for the save action to complete
pyautogui.press('tab') # SAve As window is open, press tab to navigate to the Save button
pyautogui.press('enter')  # Press Enter to save the file
time.sleep(2)  # Wait for the save action to complete

pyautogui.hotkey('alt','space') # close the Excel window
time.sleep(1)  # Wait for the window to close
pyautogui.press('c') # Press Enter to ensure the window is closed
time.sleep(2)  # Wait for the window to close
