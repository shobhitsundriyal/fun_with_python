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

cv2.imshow('op',image)
cv2.waitKey()