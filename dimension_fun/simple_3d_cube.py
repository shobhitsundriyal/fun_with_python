import pygame
import math
import numpy as np

win_width, win_height = 800, 800
out = False

cube_points = np.empty((4,3))
cube_points[0] = [-50, -50, 0]
cube_points[1] = [50, -50, 0]
cube_points[2] = [50, 50, 0]
cube_points[3] = [-50, 50, 0]

#Colors
white = (255,255,255)
black = (0,0,0)
gray = (150, 150, 150)
Dark_red = (150, 0, 0)

pygame.init()
background = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()


ortho_mat = np.array([
        [1, 0, 0]
        [0, 1, 0]
    ])

def translate(x):
    x = x + win_width/2
    return int(x)

def redraw(): # Clean up the screen and start a new grid and new frame of pendulum with new coordinates
    background.fill(black)
    cube_points = np.matmul()
    for points in cube_points:
        x = translate(points[0])
        y = translate(points[1])
        pygame.draw.circle(background, white, (x,y), 5)

    pygame.display.update()


#Main Loop
while not out:
    clock.tick(60)             
 
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            out = True                                   
        
 
    redraw()
 
pygame.quit()