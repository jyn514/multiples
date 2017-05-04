import pygame, sys
from pygame.locals import *
from pygame_colors import *
from time import sleep

pygame.init()

pygame.mixer.music.load('/home/joshua/Music/(disc_1)_03_-_Sleep_Away.mp3')
pygame.mixer.music.play(0, 0.0)

window = pygame.display.set_mode((400,300))
textObj = pygame.font.Font('freesansbold.ttf', 32).render('Hello, World!', True, Black, Yellow)
rectangle = textObj.get_rect()
rectangle.center = (200, 150)
window.fill(White)
window.blit(textObj, rectangle)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
