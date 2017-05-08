import pygame
from pygame.locals import *
from pygame_colors import *

pygame.init()
window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")
window.fill(White)
pygame.draw.polygon(window, Green,
                    ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(window, Blue, (60, 60), (120, 60), 4)
pygame.draw.line(window, Blue, (120, 60), (60, 120))
pygame.draw.line(window, Blue, (60, 120), (120, 120), 4)
pygame.draw.circle(window, Blue, (300, 50), 20, 0)
pygame.draw.ellipse(window, Red, (300, 250, 40, 80), 1)
pygame.draw.rect(window, Red, (200, 150, 100, 50))

pixObj = pygame.PixelArray(window)
pixObj[480][380] = Black
pixObj[482][383] = Black
pixObj[484][384] = Black
pixObj[486][386] = Black
pixObj[488][388] = Black
del pixObj

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()
