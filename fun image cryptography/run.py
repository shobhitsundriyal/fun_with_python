import argparse
import random
import numpy as np
import cv2

def encoder(key):

    return

def decoder(key):

    return

key = int(input('Enter a integer key: '))
random.seed(key)
np.random.seed(key)

# for now just read image
image = cv2.imread('img.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

img_arr = np.array(image)
print(img_arr.shape)


np.random.shuffle(img_arr[:,:,0])
np.random.shuffle(img_arr[:,:,1])
np.random.shuffle(img_arr[:,:,2])

cv2.imshow('op',img_arr)
cv2.waitKey()