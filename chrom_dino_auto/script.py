import pyautogui
from PIL import Image, ImageGrab
import time
import numpy as np

def hit(key):
    pyautogui.press(key)

def take_screenshot():
    image = ImageGrab.grab().convert('L')
    return image

def cactus():
    for i in range(300, 350):
        for j in range(650, 700):
            if data[i, j] < 50:
                return True
    return False

if __name__ == "__main__":
    time.sleep(3)
    hit('up')
    while True:
        image = take_screenshot()
        data = image.load() #image to array 600bdinoheigth 172 initial catus        
        data_arr = np.asarray(data)
        
        #if cactus():
        #    hit('up')
        print(np.asarray(data_arr))
        if 0 in data_arr[250:300, 650:700]:
            print(True)
    
    


    #image.show()