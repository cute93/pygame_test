import pygame
#s,f = pygame.init()
#print(f'{s} Successes and {f} Failures..')
pygame.init()

# Game Variables...
win_size = winWidth, winHeight = 800,600
bgcolor = r, g, b = [255,255,255]
clock = pygame.time.Clock()
FPS = 20

# ScreenSetting...
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption('Color Change.. 방향키를 움직여보세요.... 클릭/우클릭!!')

running=True
while running:
    screen.fill((r,g,b))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                if r<=250:
                    r += 5
            if event.key == pygame.K_DOWN:
                if r>=5:
                    r -= 5
            if event.key == pygame.K_LEFT:
                if g<=250:
                    g += 5
            if event.key == pygame.K_RIGHT:
                if g>=5:
                    g -= 5
        if event.type == pygame.MOUSEBUTTONUP:
            print(event.button)
            if event.button == 1 :
                if b<=250:
                    b+=5
            if event.button == 3:
                if b>=5:
                    b-=5

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
