#refecrence - https://www.youtube.com/watch?v=LaarVR1AOvs
import pygame
import math

win_width, win_height = 720, 720
out = False

#Colors
white = (255,255,255)
black = (0,0,0)
gray = (150, 150, 150)
Dark_red = (150, 0, 0)

pygame.init()
background = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

t = 0

def translate(x,y):
    return x+(win_width//2), y+(win_height//2)
def x_pt(t):
    return int(math.sin(t/10) * 100) 

def y_pt(t):
    return int(math.cos(t/10) * 100) #sin(freq)*amplitude

def redraw():
    global t
    #background.fill(black)
    x,y = translate(x_pt(t), y_pt(t))
    pygame.draw.circle(background, white, (x, y), 1) 
    t += 1
    
    pygame.display.update()

#Main Loop
while not out:
    clock.tick(120)             
 
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            out = True                                   
 
    redraw()
 
pygame.quit()