import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
VIOLET = (98, 19, 158)
GREY = (128, 128, 128)
MAROON = (128, 0, 0)
BLACK = (0, 0, 0)
OLIVE = (128, 128, 0)
CYAN = (0,255,255)
PINK = (255, 192, 203)
MAGENTA = (255, 0, 255)
TAN = (210, 180, 140)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Rectangle')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(WHITE)
    rectangle1 = pygame.Rect(0, 0, 85, 85)
    rectangle2 = pygame.Rect(0, 85, 170, 85)
    rectangle3 = pygame.Rect(0, 170, 255, 85)
    rectangle4 = pygame.Rect(0, 255, 340, 85)
    rectangle5 = pygame.Rect(0, 340, 425, 85)
    rectangle6 = pygame.Rect(0, 425, 510, 85)
    rectangle7 = pygame.Rect(0, 510, 595, 85)
    pygame.draw.rect(pantalla, RED, rectangle1)
    pygame.draw.rect(pantalla, ORANGE, rectangle2)
    pygame.draw.rect(pantalla, YELLOW, rectangle3)
    pygame.draw.rect(pantalla, GREEN, rectangle4)
    pygame.draw.rect(pantalla, BLUE, rectangle5)
    pygame.draw.rect(pantalla, VIOLET, rectangle6)
    pygame.draw.rect(pantalla, MAGENTA, rectangle7)
    pygame.display.update()