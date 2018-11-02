import pyautogui
import threading
import time
import math
from PIL import Image

#Setup for pyautogui operations
pyautogui.PAUSE = 0.25 #This is the number in seconds pyautogui pauses between operations
pyautogui.FAILSAFE = True #Moving mouse to upper-left kills the operation

#Object to track cursor movement/functions
class Cursor:
    def __init__(self):
        self.quadrant = 3
        self.increment = 0
        self.totalIncrement = 6
        #Set these manually
        self.marginTop = 60
        self.marginBottom = 300
        self.marginLeft = 60
        self.marginRight = 60
        #Fetches screen dimensions (only primary display)
        self.screenWidth = pyautogui.size()[0]
        self.screenHeight = pyautogui.size()[1]
        self.incrementWidth = (self.screenWidth-self.marginLeft-self.marginRight)/self.totalIncrement
        self.incrementHeight = (self.screenHeight-self.marginTop-self.marginBottom)/self.totalIncrement
        self.im1 = Image.open('images/starter1.png')
        self.im2 = Image.open('images/starter2.png')

    def findItems(self):
        print("findItems()")
        items = []
        for i in range(1, 3):
            try:
                x, y, j, k = pyautogui.locateOnScreen('images/TEST/TEST'+str(i)+'.png')
                coord = [x, y]
                items.append(coord)
            except TypeError:
                print('images/TEST/TEST'+str(i)+'.png not found within the screen region')

        if len(items) < 1:
            return self.moveCharacter()

        try:
            return self.closestPickup(items)
        except IndexError:
            print("TypeError in findItems() due to no items found (\"NoneType Object\" returned)")
            return self.findItems()

    def moveCharacter(self):
        print("Moving Character")
        self.im1 = pyautogui.screenshot()
        self.im1.save('images/image1.png')
        if self.quadrant == 1:
            print("Checking Q1. . .")
            x = self.marginLeft+(self.increment*self.incrementWidth)
            y = self.marginTop+(self.increment*self.incrementHeight)
        if self.quadrant == 2:
            print("Checking Q2. . .")
            x = self.screenWidth-self.marginRight-(self.increment*self.incrementWidth)
            y = self.marginTop+(self.increment*self.incrementHeight)
        if self.quadrant == 3:
            print("Checking Q3. . .")
            x = self.screenWidth-self.marginRight-(self.increment*self.incrementWidth)
            y = self.screenHeight-self.marginBottom-(self.increment*self.incrementHeight)+(self.incrementHeight*0.75)
        if self.quadrant == 4:
            print("Checking Q4. . .")
            x = self.marginLeft+(self.increment*self.incrementWidth)
            y = self.screenHeight-self.marginBottom-(self.increment*self.incrementHeight)+(self.incrementHeight*0.75)

        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()

        self.im2 = pyautogui.screenshot()
        self.im2.save('images/image2.png')

        if self.compareImages() == True:
            self.increment += 1
            if self.increment == 4:
                self.increment = 0
                self.quadrant += 1
                if self.quadrant == 5:
                    self.quadrant = 1
            print("self.compareImages returned TRUE, returning self.moveCharacter()")
            return self.moveCharacter()
        elif self.compareImages() == False:
            print("self.compareImages() returned FALSE, returning self.findItems()")
            return self.findItems()

    def compareImages(self):
        if (open("images/image1.png", "rb").read() == open("images/image2.png", "rb").read()):
            return True
        else:
            return False

    def closestPickup(self, list):
        print("closestPickup(list)")
        x = 960
        y = 540
        euc_dist = []
        i = 1
        for p in list:
            #print(math.hypot((x-int(p[0])), (y-int(p[1])))," Index: ",i)
            euc_dist.append(math.hypot((x-int(p[0])), (y-int(p[1]))))
            i += 1
        closest = self.sort(euc_dist)
        print("closest: ",closest,sep='')
        return self.pickupItem(list[closest])

    def pickupItem(self, list):
        print("pickupItem(list)")
        pyautogui.moveTo(list[0], list[1])
        pyautogui.doubleClick(interval=0.5)
        print("Waiting for character to move to item position")
        time.sleep(5)
        return self.findItems()



    def sort(self, list):
        print("sort(list)")
        print("list: ",list, sep='')
        lowest = list[0]
        index = 0
        for i in range(0, len(list)):
            if list[i] < lowest:
                index = i
                lowest = list[i]
        return index

#Program Execution
time.sleep(3)
myCursor = Cursor()
myCursor.findItems()
