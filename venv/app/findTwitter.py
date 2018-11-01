import pyautogui
import time

pyautogui.PAUSE = 0.1
time.sleep(1)

print("Finding Twitter Bookmark")
x, y, j, k = pyautogui.locateOnScreen('images/twitter.png')
print(pyautogui.locateOnScreen('images/twitter.png'))

print("\nFinding all folder bookmark icons")
print(list(pyautogui.locateAllOnScreen('images/folder.png')))

print("\nGoing to Twitter")
time.sleep(0.5)
pyautogui.moveTo((x, y))
pyautogui.click()
