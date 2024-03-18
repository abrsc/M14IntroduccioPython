import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)
ALPHA = 50
NEGRE_TRANSPARENT = (0,0,0,ALPHA)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Text')

#FONT I TEXT de tamany 64
def TextPantalla(pantalla, font, tamany, text, color, posicio):
    font = pygame.font.SysFont(font,tamany)
    img = font.render(text, True, color)
    pantalla.blit(img, posicio)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pantalla.fill(BLANC)
    #dibuixem el text a la posició 200,200
    TextPantalla(pantalla, None, 50, "Ano baseleyo", (255, 255, 0), (100, 200))
    TextPantalla(pantalla, "freemono", 50, "Hello world", (255, 0, 0), (100, 400))

    pygame.display.update()