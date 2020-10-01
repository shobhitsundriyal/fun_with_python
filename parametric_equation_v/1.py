import pygame
import math

win_width, win_height = 1280, 720
out = False

#Colors
white = (255,255,255)
black = (0,0,0)
gray = (150, 150, 150)
Dark_red = (150, 0, 0)

pygame.init()
background = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

def redraw():
    
    
    pygame.display.update()

#Main Loop
while not out:
    clock.tick(120)             
 
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            out = True                                   
 
    redraw()
 
pygame.quit()