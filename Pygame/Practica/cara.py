import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)
TAN = (254, 231, 184)
RED = (218, 47, 71)
PINK = (255, 120, 146)
DARK_RED = (187, 26, 52)
BLUE = (66, 137, 193)
NEGRE_TRANSPARENT = (0,0,0,170)
MAROON = (101, 70, 26)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Cara')
seccio_transparent = pygame.Surface((600,600),pygame.SRCALPHA)
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    pygame.draw.circle(pantalla,BLUE,(120,165),50)
    pygame.draw.circle(pantalla,BLUE,(180,104),35)
    pygame.draw.circle(pantalla, BLUE, (600-120,165),50) 
    pygame.draw.circle(pantalla, BLUE, (600-180,104),35)
    pygame.draw.circle(pantalla, TAN, (300,300),225)
    pygame.draw.circle(pantalla,BLUE,(128,138),35)
    pygame.draw.circle(pantalla,BLUE,(130,108),45)
    pygame.draw.circle(pantalla,BLUE,(165,104),25)
    pygame.draw.circle(pantalla, BLUE, (600-128,138),35) 
    pygame.draw.circle(pantalla, BLUE, (600-130,108),45) 
    pygame.draw.circle(pantalla, BLUE, (600-165,104),25)
    pygame.draw.circle(pantalla,PINK, (175,340),50)
    pygame.draw.circle(pantalla,PINK, (425,340),50)
    pygame.draw.rect(pantalla,RED,(175,370,250,75))
    pygame.draw.rect(pantalla,TAN,(225,360,150,50))
    pygame.draw.polygon(pantalla, DARK_RED, ((300,275),(260,330),(340,330)))
    pygame.draw.line(pantalla, NEGRE, (105,185),(495,185),25)
    pygame.draw.circle(pantalla, BLUE, (117.5,185),7.5)
    pygame.draw.circle(pantalla, BLUE, (600-117.5,185),7.5)
    pygame.draw.ellipse(pantalla,BLANC,(197.5,203,70,70))
    pygame.draw.ellipse(pantalla,BLANC,(385,203,70,70))
    pygame.draw.circle(pantalla,NEGRE,(240,235),20)
    pygame.draw.circle(pantalla,NEGRE,(428,235),20)
    pygame.draw.rect(seccio_transparent,NEGRE_TRANSPARENT,(140,197.5,135,85))
    pygame.draw.rect(seccio_transparent,NEGRE_TRANSPARENT,(325,197.5,135,85))
    pygame.draw.rect(pantalla,NEGRE,(140,197.5,135,85),7)
    pygame.draw.rect(pantalla,NEGRE,(325,197.5,135,85),7)
    

    pantalla.blit(seccio_transparent,(0,0))
    pygame.display.update()