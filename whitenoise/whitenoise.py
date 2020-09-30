import pygame
import math
import random
import numpy as np
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument("-c", action='store_true') 
args = parser.parse_args() 
colored = args.c

out = False
win_width, win_height = 800, 600

pygame.init()
background = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

def redraw():
    im = np.random.randint(255, size=(win_width,win_height,3))
    if not colored:
        im[:,:,1] = im[:,:,0]
        im[:,:,2] = im[:,:,0]
    surf = pygame.surfarray.make_surface(im)
    background.blit(surf, (0, 0))
    pygame.display.update()

#Main Loop
while not out:
    clock.tick(120)             
 
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            out = True                                   
 
    redraw()
 
pygame.quit()