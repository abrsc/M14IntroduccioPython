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
YELLOW = (255, 255, 0)


pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Activitat Formes 4')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    cel = pygame.Rect(0, 0, 600, 400)
    herba = pygame.Rect(0,400,600,50)
    terra = pygame.Rect(0, 450, 600, 150)
    tronc_arbre = pygame.Rect(pantalla, ())
    pygame.draw.rect(pantalla, (3,177,252), cel)
    pygame.draw.rect(pantalla, (6,148,15), herba)
    pygame.draw.rect(pantalla, (36,16,5), terra)

    # Sol
    pygame.draw.circle(pantalla, YELLOW, (400,100), 75)
    pygame.display.update()


