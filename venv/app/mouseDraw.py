import pyautogui
import time

print("Press Ctrl+C to force quit")

time.sleep(5)

pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.5)
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0.5)
    pyautogui.dragRel(-distance, 0, duration=0.5)
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0.5)

print("Done")
