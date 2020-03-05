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
image = cv2.imread('cat.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

img_np = np.array(image)/255
print(img_np.shape)

noise = np.random.rand(img_np.shape[0], img_np.shape[1], img_np.shape[2])
img_arr = img_np #+ noise


np.random.shuffle(img_arr[:,:,0])
np.random.shuffle(img_arr[:,:,1])
np.random.shuffle(img_arr[:,:,2])


cv2.imshow('op',img_arr)
cv2.waitKey()

for i in range(key):
    np.random.shuffle(img_arr[:,:,0])
    np.random.shuffle(img_arr[:,:,1])
    np.random.shuffle(img_arr[:,:,2])
    cv2.imshow('op'+str(i),img_arr)
    cv2.waitKey()
    i += 1