from random import randint
import pygame

win_height = 600
win_width = 600
white = (255,255,255)
black = (0,0,0)

out = False

pygame.init()
background = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

class Star:
    def __init__(self):
        self.x = randint(-win_width//2, win_width//2)
        self.y = randint(-win_height/2, win_height/2)
        self.z = win_width

def show(bg, x, y, r):
    x = win_width//2 + x
    y = win_height//2 + y
    pygame.draw.circle(bg, white, (x, y), r)

Stars = []
for i in range(100):
    Stars.append(Star())

while not out:
    clock.tick(120)             
 
    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            out = True 

    background.fill(black)
    for obj in Stars:
        if obj.z < win_width/4:
            r = 5
        elif obj.z < win_width/3:
            r = 4
        elif obj.z < win_width/2:
            r = 3
        elif obj.z < win_width:
            r = 2
        else:
            r = 1

        show(background, int((obj.x/obj.z)*win_width), int((obj.y/obj.z)*win_width), r)
        obj.z -= 13
        if obj.z < obj.x or obj.z<1:#first cond?
            obj.z = win_width
            obj.x = randint(-win_width//2, win_width//2)
            obj.y = randint(-win_height/2, win_height/2)
        

    pygame.display.update()