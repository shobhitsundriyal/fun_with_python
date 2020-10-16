import pygame
import math

win_width, win_height = 1280, 720

out = False
acceleration = False
length, angle, vel, Aacc = 0,0,0,0

#Colors
white = (255,255,255)
black = (0,0,0)
gray = (150, 150, 150)
Dark_red = (150, 0, 0)

pygame.init()
background = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

def redraw(): # Clean up the screen and start a new grid and new frame of pendulum with new coordinates
    background.fill(black)
    pendulum.draw(background)
    pygame.display.update()


#Main Loop
while not out:
    clock.tick(60)             
 
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            out = True                                   
        
 
    redraw()
 
pygame.quit()