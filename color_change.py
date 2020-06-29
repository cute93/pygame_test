import pygame
from pygame.locals import *

size = width, height = (400,300)
bgcolor = [255,255,255]
timer = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('change background')

EndFlag = True
while EndFlag:
    for event in pygame.event.get():
        if event.type == QUIT:
            EndFlag = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if bgcolor[0] < 235:
                    bgcolor[0] += 20
            if event.key == K_DOWN:
                if bgcolor[0] > 20:
                    bgcolor[0] -= 20
            if event.key == K_RIGHT:
                if bgcolor[1] < 235:
                    bgcolor[1] += 20
            if event.key == K_LEFT:
                if bgcolor[1] > 20:
                    bgcolor[1] -= 20
        if event.type == MOUSEBUTTONUP:
            if event.button == 1 :
                if bgcolor[2] < 235:
                    bgcolor[2] += 20
            if event.button == 3:
                if bgcolor[2] > 20:
                    bgcolor[2] -= 20

        screen.fill(bgcolor)
        pygame.display.flip()
        timer.tick(20)        
pygame.quit()