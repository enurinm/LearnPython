import pygame, sys, random

from pygame.locals import*

pygame.init()
pygame.display.set_caption("rain")
screen=pygame.display.set_mode((1000,600))
clock=pygame.time.Clock()
raindrop_spawn_time=0

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

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pass
        pass

    raindrops.append(Raindrop())
    screen.fill((255,255,255))

    i=0
    while i<len(raindrops):
        raindrops[i].move()
        raindrops[i].draw()
        if raindrops[i].off_screen():
            del raindrops[i]
            i-=1
            pass
        i+=1
        pass

    pygame.display.update()
    pass
