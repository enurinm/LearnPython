import pygame, sys, random

from pygame.locals import*

pygame.init()
pygame.display.set_caption("rain")
screen=pygame.display.set_mode((1000,600))
clock=pygame.time.Clock()
raindrop_spawn_time=0
camerlyn_default=pygame.image.load("./img/Camerlyn_umbrella.png").convert()
camerlyn_right=pygame.image.load("./img/Camerlyn_umbrella.png").convert()
camerlyn_jump=pygame.image.load("./img/Camerlyn_umbrella.png").convert()

class Camerlyn:
    """docstring for Camerlyn."""

    def __init__(self):
        super(Camerlyn, self).__init__()
        self.x = 150
        self.y = 450

    def draw(self):
        pressed_keys=pygame.key.get_pressed()

        if pressed_keys[K_RIGHT]:
            screen.blit(camerlyn_right,(self.x, self.y))
        elif pressed_keys[K_UP]:
            screen.blit(camerlyn_jump,(self.x, self.y))
        else:
            screen.blit(camerlyn_default,(self.x, self.y))
        pass

    def hit_by(self, raindrop):
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x,raindrop.y))
        pass

    def move(self):
        pressed_keys=pygame.key.get_pressed()
        if self.y < 450:
            self.y+=10
            pass
        if pressed_keys[K_UP]:
            self.y-=20
            pass
        if pressed_keys[K_RIGHT]:
            self.x+=5
            pass
        if pressed_keys[K_LEFT]:
            self.x-=5
            pass


class Raindrop:
    """make Raindrop."""

    def __init__(self):
        super(Raindrop, self).__init__()
        self.x = random.randint(0,1000)
        self.y = -5
        self.speed=random.randint(5,18)

    def move(self):
        self.y+=self.speed
        pass

    def draw(self):
        pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x,self.y+5),1)
        pass

    def off_screen(self):
        return self.y>800
        pass

raindrops = []
camerlyn = Camerlyn()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pass
        pass

    raindrops.append(Raindrop())
    screen.fill((255,255,255))
    camerlyn.draw()
    camerlyn.move()

    i=0
    while i<len(raindrops):
        raindrops[i].move()
        raindrops[i].draw()
        if raindrops[i].off_screen() or camerlyn.hit_by(raindrops[i]):
            del raindrops[i]
            i-=1
            pass
        i+=1
        pass

    pygame.display.update()
    pass
