import pyautogui
import threading

def setInterval(function, time):
    e = threading.Event()
    while not e.wait(time):
        function()

def getPosition():
    #pyautogui.doubleClick()
    x, y = pyautogui.position()
    currentPosition = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(currentPosition, end='')
    print('\b' * len(currentPosition), end='', flush=True)

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

print("using size (width, height): ", pyautogui.size())
print("Press Ctrl+C to force quit")

try:
    while True:
        setInterval(getPosition, 1)
except KeyboardInterrupt:
    print("\nDone")
