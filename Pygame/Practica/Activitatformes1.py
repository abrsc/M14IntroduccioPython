import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0)
BLAU = (0,0,255)
VERD = (0,255,0)
BLANC = (255,255,255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Activitat Formes 1')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    rectangle1 = pygame.Rect(100, 100, 400, 50)
    rectangle2 = pygame.Rect(75, 75, 450, 100)
    rectangle3 = pygame.Rect(50, 50, 500, 150)
    rectangle4 = pygame.Rect(0, 0, 600, 250)
    pygame.draw.rect(pantalla, NEGRE, rectangle4, 25)
    pygame.draw.rect(pantalla, BLAU, rectangle3)
    pygame.draw.rect(pantalla, VERD, rectangle2)
    pygame.draw.rect(pantalla, VERMELL, rectangle1)
    pygame.display.update()
