import pygame
class Box:
    def __init__(self, size=(32,32), color=(0,0,0)):
        self.box = pygame.Surface(size)
        self.rect = self.box.get_rect()
        self.box.fill(color)
        
class MainBar(Box):
    def setPos(self, pos):
        self.rect.center = pos
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 1
        if keys[pygame.K_a]:
            self.rect.x -= 1
        if keys[pygame.K_s]:
            self.rect.y += 1
        if keys[pygame.K_d]:
            self.rect.x += 1
            
class BasicGame:
    def __init__(self, title='Default', fps=20):
        pygame.init()
        self.winSize = self.Width, self.Height = 400,300
        self.RED, self.BLACK, self.WHITE, self.GREEN, self.BLUE = (255,0,0),(0,0,0), (255,255,255),(0,255,0),(0,0,255)
        self.screen = pygame.display.set_mode(self.winSize)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.FPS = fps
        self.mainBar = MainBar((64,16))        

    def run(self):
        onGame = True
        while onGame:
            self.screen.fill(self.WHITE)
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quit")
                    onGame = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        onGame = False
            self.mainBar.update()
            self.screen.blit(self.mainBar.box, self.mainBar.rect)
            pygame.display.update()
                                
        self.quit()
        
    def quit(self):
        pygame.quit()
    

if __name__=='__main__':
    b = BasicGame()
    b.run()
    print(b.BLACK)
    
