import pygame, sys
from pygame.locals import *
from pygame_colors import *

pygame.init()
window = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Catomotive")
cat = pygame.image.load('/home/joshua/Documents/Coding/pygame/cat.png')
catx = 10
caty= 10
direction = 'right'

while True:
    window.fill(White)
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    window.blit(cat, (catx, caty))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    #AFFECTS SPEED AS WELL AS REFRESH RATE
    pygame.time.Clock().tick(30)
