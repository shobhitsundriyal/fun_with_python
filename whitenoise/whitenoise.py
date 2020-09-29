import pygame
import math
import random
import numpy as np

out = False
win_width, win_height = 400, 300

pygame.init()
background = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

def redraw():
    #background.fill((0,0,0))
    for i in range(win_height):
        for j in range(win_width):
            b = random.randint(0, 255)
            pygame.draw.circle(background, (b,b,b), (j+1, i+1), 2)
    pygame.display.update()

#Main Loop
while not out:
    clock.tick(120)             
 
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            out = True                                   
 
    redraw()
 
pygame.quit()