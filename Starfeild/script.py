import random
import pygame
height = 800
width = 800
class Star():
    def __init__(self, *args):
        x = random(-width//2, width//2)
        y = random(-height//2, height//2)
        z = 0
