import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((300,180))
mRect = pygame.Rect(10, 10, 10, 10)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255),mRect)    
    pygame.display.flip()



'''
size = width, height = (400,300)
bgcolor = (255,255,255)
timer = pygame.time.Clock()

r = Rect(width//2-50,height//2-50,100,100)
rectcolor = [90,20,100]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Move Rect!!')

gameFlag = True
while gameFlag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameFlag = False
        if event.type == pygame.KEYDOWN :
            if event.key == K_LEFT:
                r.move_ip(-10, 0)
            if event.key == K_RIGHT:
                r.move_ip(10, 0)
            if event.key == K_UP:
                r.move_ip(0, -10)
            if event.key == K_DOWN:
                r.move_ip(0, 10)        
    screen.fill(bgcolor)
    pygame.draw.rect(screen, rectcolor, r)
    pygame.display.update()
    timer.tick(20)
'''
pygame.quit()