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

def x_pt1(t):
    result = math.sin(t/10) * 100 + math.sin(t/15) * 120 + math.sin(t/25) * 5
    return int(result) 

def y_pt1(t): #sin(freq)*amplitude
    result = math.cos(t/10) * 100
    return int(result)

def x_pt2(t):
    result = math.sin(t/10) * 200 + math.sin(t) * 2
    return int(result) 

def y_pt2(t): 
    result = math.cos(t/20) * 200 + math.cos(t/12) * 30 + math.cos(t/8) * 22
    return int(result)

def redraw():
    global t
    #if mod%20 == 0:
    background.fill(black)
    '''
    pygame.draw.circle(background, white, (x1, y1), 1) 
    pygame.draw.circle(background, white, (x2, y2), 1) 
    '''
    for i in range(20):#number of trails
        x1,y1 = translate(x_pt1(t+i), y_pt1(t+i))
        x2,y2 = translate(x_pt2(t+i), y_pt2(t+i))
        pygame.draw.line(background, white , (x1,y1),(x2, y2), 2)
    t += 1.5
    
    pygame.display.update()

#Main Loop

while not out:
    clock.tick(120)             
 
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            out = True                                   
 
    redraw()
 
pygame.quit()