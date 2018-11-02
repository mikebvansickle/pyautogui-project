import pyautogui

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

print("using size (width, height): ", pyautogui.size())

for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
