import pyautogui
import time
import threading

def setInterval(function, time):
    e = threading.Event()
    while not e.wait(time):
        function()

def newMove(x, y):
    x, y = pyautogui.position()
    im1 = pyautogui.screenshot()
    im1.save('images/first.png')
    x += 278
    y += 162
    pyautogui.moveTo(x, y)
    im2 = pyautogui.screenshot()
    im2.save('images/second.png')
    return x, y

def newMoveTwo(x, y):
    x, y = pyautogui.position()
    im1 = pyautogui.screenshot()
    im1.save('images/first.png')
    x += 278
    y -= 162
    pyautogui.moveTo(x, y)
    im2 = pyautogui.screenshot()
    im2.save('images/second.png')
    return x, y

def tryMove(x, y):
    x, y, j, k = pyautogui.locateOnScreen('images/currency2.png')
    pyautogui.moveTo((x, y))
    pyautogui.keyDown('Alt')
    pyautogui.click()
    pyautogui.keyUp('Alt')
    print("Picking up item")
    time.sleep(5)
    im1 = pyautogui.screenshot()
    im1.save('images/first.png')
    x = 125
    y = 125
    pyautogui.moveTo(x, y)
    im2 = pyautogui.screenshot()
    im2.save('images/second.png')
    if (open("images/first.png", "rb").read() == open("images/second.png","rb").read()):
        if (x < 960 and y < 450):
            while (x < 960 and y < 450):
                print("Images the same; topleft to mid")
                newMove(x, y)
        if (x >= 960):
            while (x >= 960 and y < 450):
                print("Images the same; mid to topright")
                newMoveTwo(x, y)

pyautogui.PAUSE = 0.5
time.sleep(1)

try:
    while True:
        setInterval(tryMove(x, y), 2)
except KeyboardInterrupt:
    print("Done")
