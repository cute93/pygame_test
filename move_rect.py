import pygame
from pygame.locals import *
from random import randrange

def getRandomColor():
    return randrange(256),randrange(256),randrange(256)

# init
s,f = pygame.init()
print(f'{s} Successes and {f} Failures..')


# Game Variables...
win_size = winWidth, winHeight = 800,600
GameColor = WHITE, BLACK = [(250, 250, 250), (5,5,5)]
msize = 32,32
clock = pygame.time.Clock()
FPS = 20

# ScreenSetting...
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption('Move Rectangle!! press c and arrow!!')


# Rect Setting...
master = pygame.Surface(msize)
m_rect = master.get_rect()
master.fill(BLACK)


# Game Loop
gameFlag=True
while gameFlag:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameFlag = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gameFlag = False
            if event.key == K_c:
                master.fill(getRandomColor())
            if event.key == K_UP:
                if m_rect.top > 0:
                    m_rect.move_ip(0,-2)
            if event.key == K_DOWN:
                if m_rect.bottom > winHeight:
                    m_rect.move_ip(0,2)
            if event.key == K_LEFT:
                if m_rect.left>0:
                    m_rect.move_ip(-2,0)
            if event.key == K_RIGHT:
                if m_rect.right<winWidth:
                    m_rect.move_ip(2,0)

    keys = pygame.key.get_pressed()
    if keys[K_w]:
        if m_rect.top > 0:
            m_rect.move_ip(0,-2)
    if keys[K_s]:
        if m_rect.bottom < winHeight:
            m_rect.move_ip(0,2)
    if keys[K_a]:
        if m_rect.left > 0:
            m_rect.move_ip(-2,0)
    if keys[K_d]:
        if m_rect.right < winWidth:
            m_rect.move_ip(2,0)
    screen.fill(WHITE)
    screen.blit(master, m_rect)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
