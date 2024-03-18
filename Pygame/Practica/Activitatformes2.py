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
pygame.display.set_caption('Activitat Formes 2')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    rectangle1 = pygame.Rect(100, 100, 400, 400)
    pygame.draw.rect(pantalla, BLAU, rectangle1)
    pygame.draw.circle(pantalla, VERMELL, (300, 300), 200)
    pygame.draw.polygon(pantalla, YELLOW, ((300,100),(130,400),(470,400)))
    pygame.display.update()
