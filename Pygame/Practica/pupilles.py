import pygame, sys
from pygame.locals import *

AMPLE = 800
ALT = 600
TAMANY = (AMPLE,ALT)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
VIOLET = (149, 53, 83)
GREY = (128, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
CYAN = (0,255,255)
PINK = (255, 192, 203)
MAGENTA = (255, 0, 255)
TAN = (210, 180, 140)
TEAL = (0, 128, 128)
WHITE = (255,255,255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Cercle')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(PINK)
    pygame.draw.circle(pantalla, WHITE, (200, 200),100)
    pygame.draw.circle(pantalla, WHITE, (600, 200), 100)
    pygame.draw.circle(pantalla, BLACK, (200, 200), 40)
    pygame.draw.circle(pantalla, BLACK, (600, 200), 40)
    pygame.draw.circle(pantalla, BLACK, (600, 200), 130, 15)
    pygame.draw.circle(pantalla, BLACK, (200, 200), 130, 15)
    pygame.draw.line(pantalla, BLACK, (330, 200), (470,200),20)
    pygame.draw.line(pantalla, BLACK, (700, 400), (650,500),15)
    pygame.draw.ellipse(pantalla, WHITE, (300, 400, 200, 100))
    pygame.draw.ellipse(pantalla, BLACK, (300, 400, 200, 100), 5)
    pygame.draw.polygon(pantalla, BLACK, ((400, 300),(350,350),(450,350)),5)
    pygame.display.update()