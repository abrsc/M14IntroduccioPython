# Aquest Joc és un "clon" del joc "Flappy Bird".
from pygame.locals import *
import pygame, random, time


AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/background.png'
WHITE = (255,255,255)
running = True
partida = False

imatge_tortuga = pygame.image.load('assets/tortuga.png')
temps_pause = 0

pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Flappy Turtle")
background = pygame.image.load(BACKGROUND_IMAGE).convert()

#FPS
clock = pygame.time.Clock()
fps = 60

#Definició per imprimir text facilment.
def TextPantalla(pantalla, font, tamany, text, color, posicio):
    font = pygame.font.SysFont(font,tamany)
    img = font.render(text, True, color)
    pantalla.blit(img, posicio)

#Imprimir el menu de inici de joc.
def menuprincipal():
    pantalla.blit(background, (0,0))
    seccio_transparent = pygame.Surface((320,200),pygame.SRCALPHA)
    pygame.draw.rect(seccio_transparent,(0,0,0,100),(0,35,140,68))
    pantalla.blit(seccio_transparent, (40, 40))
    TextPantalla(pantalla, None, 24, "1.- Crèdits", WHITE, (50,80))
    TextPantalla(pantalla, None, 24, "2.- Jugar", WHITE,(50,100))
    TextPantalla(pantalla,None, 24, "3.- Sortir", WHITE, (50,120))
    pygame.display.update()

while running:
     
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()