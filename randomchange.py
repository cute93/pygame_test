import pygame
from random import randrange

def getRandomColor():
    return randrange(256),randrange(256),randrange(256)

# init
s,f = pygame.init()
print(f'{s} Successes and {f} Failures..')


# Game Variables...
win_size = winWidth, winHeight = 800,600
backColor = getRandomColor()
clock = pygame.time.Clock()
FPS = 20

# ScreenSetting...
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption('Set Random BackGroud Color!!')

# Game Loop
endFlag=True
while endFlag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endFlag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                endFlag = False
            if event.key == pygame.K_c:
                backColor = getRandomColor()
    screen.fill(backColor)
    pygame.draw.rect(screen, (4,4,4), (10,10,20,20),1)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
