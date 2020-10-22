import pygame
from math import sin, cos, radians
import numpy as np
from numpy import transpose as T
from random import choice

win_width, win_height = 800, 800
out = False

cube_points = np.empty((8,3))
cube_points[0] = [-1, -1, -1]
cube_points[1] = [1, -1, -1]
cube_points[2] = [1, 1, -1]
cube_points[3] = [-1, 1, -1]
cube_points[4] = [-1, -1, 1]
cube_points[5] = [1, -1, 1]
cube_points[6] = [1, 1, 1]
cube_points[7] = [-1, 1, 1]

scale = 70

cube_points *= scale

angle = radians(1.3)
angle_plus = radians(5)

#Colors
white = (255,255,255)
black = (0,0,0)
gray = (150, 150, 150)
Dark_red = (150, 0, 0)

pygame.init()
background = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()


ortho_mat = np.array([
        [1, 0, 0],
        [0, 1, 0]
    ])

rotateZ = np.array([
    [cos(angle), -sin(angle), 0],
    [sin(angle), cos(angle), 0 ],
    [0, 0, 1]
])

rotateX = np.array([
    [1, 0, 0],
    [0, cos(angle), -sin(angle)],
    [0, sin(angle), cos(angle)],
])

rotateY = np.array([
    [cos(angle), 0, -sin(angle)],
    [0, 1, 0],
    [sin(angle), 0, cos(angle)],
])

def translate(x):
    x = x + win_width/2
    return int(x)

def connect(p1, p2, projected_points):
    global background
    pygame.draw.line(background, white, projected_points[p1], projected_points[p2], 2)

def redraw(): # Clean up the screen and start a new grid and new frame of pendulum with new coordinates
    background.fill(black)
    global cube_points

    #cube_points = T(np.matmul(rotateZ, T(cube_points)))
    cube_points = T(np.matmul(rotateY, T(cube_points)))
    #cube_points = T(np.matmul(rotateZ, T(cube_points)))
    #cube_points = T(np.matmul(rotateX, T(cube_points)))

    # projection at last
    #perspective
    distance = 5*scale
    z = distance + cube_points[:, 2]# - np.mean(cube_points[:, 2]))
    z = distance/z

    projected_points = T(np.matmul(ortho_mat, T(cube_points)))
    projected_points[:, 0] *= z
    projected_points[:, 1] *= z
    projected_points += win_width/2
    for i, points in enumerate(projected_points):
        x = int(points[0])  
        y = int(points[1])
        pygame.draw.circle(background, white, (x,y), 5)

    for i in range(4):
        connect(i, (i+1)%4, projected_points)
        connect(i, i+4, projected_points)
        connect(i+4, ((i+1)%4)+4, projected_points)

    pygame.display.update()


#Main Loop
while not out:
    clock.tick(60)             
 
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            out = True                                   
        
 
    redraw()
 
pygame.quit()