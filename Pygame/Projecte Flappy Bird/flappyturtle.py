# Aquest Joc és un "clon" del joc "Flappy Bird".
from pygame.locals import *
import pygame, random, time


AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/background.png'
WHITE = (255,255,255)
running = True
partida = False

#La tortuga que nos da pena
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
    seccio_transparent = pygame.Surface((800,600),pygame.SRCALPHA)
    pygame.draw.rect(seccio_transparent,(0,0,0,100),(225,110,350,380))
    pantalla.blit(seccio_transparent, (0, 0))
    TextPantalla(pantalla, 'Comic Sans MS', 40, "1.- Crèdits", WHITE, (256.25,120))
    TextPantalla(pantalla, 'Comic Sans MS', 40, "2.- Jugar", WHITE,(256.25,190))
    TextPantalla(pantalla, 'Comic Sans MS', 40, "3.- Score", WHITE,(256.25,260))
    TextPantalla(pantalla, 'Comic Sans MS', 40, "4.- Sortir", WHITE, (256.25,330))
    pygame.display.update()

menuprincipal()
while running:
     
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()