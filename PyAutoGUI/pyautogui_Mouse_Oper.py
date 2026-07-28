import pyautogui
import time

# Mouse Operations
pyautogui.moveTo(200, 200, duration=1.0)  # Move the mouse to (100, 100) over 1 second
pyautogui.click(100 , 100 , duration=0.5)  # Click at (100, 100) with a duration of 0.5 seconds
pyautogui.rightClick(100, 100)  # Right-click at (200, 200)
pyautogui.doubleClick(100, 100, interval=0.25)  # Double-click at (400, 400) with an interval of 0.25 seconds
pyautogui.leftClick(100,100)

time.sleep(3)
pyautogui.dragTo(100,100, duration=1.0)  # Drag the mouse to (500, 500) over 1 second

time.sleep(3)
pyautogui.leftClick(700,700)
pyautogui.scroll(-700)  # Scroll down 500 units

time.sleep(3)
pyautogui.scroll(700)  # Scroll up 500 units