import pygame
import sys
from pygame.locals import *
pygame.init()

# sets size of window
DISPLAYSURF = pygame.display.set_mode((200, 200))
# caption is displayed at top of window
pygame.display.set_caption("Hello, World!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
