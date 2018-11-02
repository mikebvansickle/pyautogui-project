import pyautogui
import time
from PIL import Image
import math

def findItems():
    print("findItems()")
    items = []
    for i in range(1, 7):
        try:
            x, y, j, k = pyautogui.locateOnScreen('images/TEST/TEST'+str(i)+'.png')
            coord = [x, y]
            items.append(coord)
        except TypeError:
            print('images/TEST/TEST'+str(i)+'.png not found within the screen region')

    try:
        return closestPickup(items)
    except IndexError:
        print("TypeError in findItems() due to no items found (\"NoneType Object\" returned)")
        return findItems()

def pickupItem(list):
    print("pickupItem(list)")
    pyautogui.moveTo(list[0], list[1])
    pyautogui.doubleClick(interval=0.5)
    print("Waiting for character to move to item position")
    time.sleep(5)
    return findItems()


def sort(list):
    print("sort(list)")
    print("list: ",list, sep='')
    lowest = list[0]
    index = 0
    for i in range(0, len(list)):
        if list[i] < lowest:
            index = i
            lowest = list[i]
    return index

def closestPickup(list):
    print("closestPickup(list)")
    x = 960
    y = 540
    euc_dist = []
    i = 1
    for p in list:
        #print(math.hypot((x-int(p[0])), (y-int(p[1])))," Index: ",i)
        euc_dist.append(math.hypot((x-int(p[0])), (y-int(p[1]))))
        i += 1

    print(euc_dist)
    closest = sort(euc_dist)
    print(closest)
    return pickupItem(list[closest])

pyautogui.FAILSAFE = True

time.sleep(2)

findItems()

#imagePos = pyautogui.locateOnScreen('images/TEST1.png')


#list(pyautogui.locateAllOnScreen('images/sixsocket.png'))
#print(list)
