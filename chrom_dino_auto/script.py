import pyautogui
from PIL import Image, ImageGrab
import numpy as np
import time

def hit(key):
    pyautogui.press(key)

def take_screenshot():
    image = ImageGrab.grab().convert('L')
    return image

def cactus():
    for i in range(250, 550):
        for j in range(650, 700):
            if data[i, j] in [5, 172]:
                return True
            #data[i,j] = 0
    return False

def bird():
    for i in range(250, 550):
        for j in range(520, 600):
            if data[i, j] in [5, 172]:
                return True
            #data[i,j] = 0
    return False    


if __name__ == "__main__":
    time.sleep(3)
    hit('up')
    while True:
        image = take_screenshot()
        data = image.load() #image to array 600bdinoheigth 172 initial catus        
        data_arr = np.asarray(data)
        
        if cactus():
            hit('up')
        
        if bird():
            hit('down')
        
   
    


    #image.show()