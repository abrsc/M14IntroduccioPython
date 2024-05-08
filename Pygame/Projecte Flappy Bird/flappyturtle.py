# Aquest Joc és un "clon" del joc "Flappy Bird".
from pygame.locals import *
import pygame, random, time


AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/background.png'
WHITE = (255,255,255)
running = True
partida = False

#Carregar la tortuga que nos da pena
imatge_tortuga = pygame.image.load('assets/tortuga.png')

#Carregar el suelo
imatge_suelo = pygame.image.load('assets/suelo.png')

temps_pause = 0

pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Flappy Turtle")
background = pygame.image.load(BACKGROUND_IMAGE).convert()
pos_x_suelo = 0

#FPS
clock = pygame.time.Clock()
fps = 60

#Definició per imprimir imatge de fons:
def imprimir_pantalla_fons(image):
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

def imprimir_suelo():
    pantalla.blit(imatge_suelo, (pos_x_suelo, 482))
    pantalla.blit(imatge_suelo,(pos_x_suelo + 800, 482))

#Definició per imprimir text facilment.
def TextPantalla(pantalla, font, tamany, text, color, posicio):
    font = pygame.font.SysFont(font,tamany)
    img = font.render(text, True, color)
    pantalla.blit(img, posicio)

#Definició per imprimir un rectangle transparent facilment.
def recttransparent(color, posicio):
    seccio_transparent = pygame.Surface((800,600),pygame.SRCALPHA)
    pygame.draw.rect(seccio_transparent,color,posicio)
    pantalla.blit(seccio_transparent, (0, 0))

#Definició que imprima els credits del joc a la pantalla.
def credits():
    animaciocreditacabat = False
    credits = True
    while credits == True:
        if animaciocreditacabat == False:
            for i in range(0,60):
                time.sleep(0.02)
                pantalla.blit(background, (0,0))
                recttransparent((0,0,0,150),(175,0,450,600))
                TextPantalla(pantalla,'Comic Sans MS',22, "Programa: Arno B., Kristopher G., Xavi Sancho", (WHITE), (20,i))
                TextPantalla(pantalla,'Comic Sans MS',22, "Gràfics: Kristopher G.", (WHITE), (20,i+20))
                TextPantalla(pantalla,'Comic Sans MS',22, "Música: -", (WHITE), (20,i+38))
                TextPantalla(pantalla,'Comic Sans MS',22, "Efectes de so: -", (WHITE), (20,i+56))
                pygame.display.update()
            TextPantalla(pantalla,'Comic Sans MS',17, "Premeu la barra espaiadora per continuar..", (WHITE), (40,180))
            animaciocreditacabat = True
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE and animaciocreditacabat == True:
                        credits = False
                        menuprincipal()
        pygame.display.update()

#Imprimir el menu de inici de joc.
def menuprincipal():
    pantalla.blit(background, (0,0))
    recttransparent((0,0,0,100),(225,110,350,380))
    TextPantalla(pantalla, 'Comic Sans MS', 40, "1.- Crèdits", WHITE, (256.25,120+35))
    TextPantalla(pantalla, 'Comic Sans MS', 40, "2.- Jugar", WHITE,(256.25,190+35))
    TextPantalla(pantalla, 'Comic Sans MS', 40, "3.- Score", WHITE,(256.25,260+35))
    TextPantalla(pantalla, 'Comic Sans MS', 40, "4.- Sortir", WHITE, (256.25,330+35))
    pygame.display.update()

menuprincipal()
while running:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_1:
                credits()
            if event.key == K_2:
                partida = True
            if event.key == K_4:
                running = False

    if partida == True:
        current_time = pygame.time.get_ticks()
        BACKGROUND_IMAGE = 'assets/mar.png'
        player_rect = imatge_tortuga.get_rect(midbottom=(AMPLADA // 4.5, ALTURA - 270))
        gravitat = 0.2
        velocitat_tortuga = 0

        while True:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        velocitat_tortuga = 0
                        velocitat_tortuga -= 5.5

            # Mantenir al jugador dins de la pantalla:
            player_rect.clamp_ip(pantalla.get_rect())
            imprimir_pantalla_fons(BACKGROUND_IMAGE)

            pantalla.blit(imatge_tortuga, player_rect)
            velocitat_tortuga += gravitat
            player_rect.y += velocitat_tortuga

            pos_x_suelo -= 1
            imprimir_suelo()
            if pos_x_suelo <= -800:
                pos_x_suelo = 0

            pygame.display.update()
            clock.tick(fps)