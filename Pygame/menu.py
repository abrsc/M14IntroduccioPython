import time
from pygame.locals import *
import pygame

AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'Assets/TitleScreen.png'
WHITE = (255,255,255)
running = True
partida = False

# Jugador 1:
player_image = pygame.image.load('assets/Nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 2

# Jugador 2:
player_image2 = pygame.image.load('assets/Nau2.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 150))
velocitat_nau2 = 2

# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 3
temps_entre_bales = 1000 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2

pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load('Assets/musicadefons.mp3')
#pygame.mixer.music.play(-1, 12, 3000)
#pygame.mixer.music.set_volume(0.75)
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Vaseleyo")
background = pygame.image.load(BACKGROUND_IMAGE).convert()

# CREAR LA SUPERFÍCIE TRANSPARENT I EL RECTANGLE SOBRE ELLA:
seccio_transparent = pygame.Surface((240,120),pygame.SRCALPHA)

# Control de FPS
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

def TextPantalla(pantalla, font, tamany, text, color, posicio):
    font = pygame.font.SysFont(font,tamany)
    img = font.render(text, True, color)
    pantalla.blit(img, posicio)

def animacioinici():
    color = 0
    for i in range(0,255):
        time.sleep(0.01)
        if i < 255:
            color += 3
            if color > 255:
                color = 255
        if i < 70:
            time.sleep(0.01)
            pantalla.fill((0,0,0))
            TextPantalla(pantalla,None,80, "Vaseleyo", (color,0,0), (40,i))
        pygame.display.update()
            

def menuprincipal():
    # Imprimeixo imatge de fons:
    pantalla.blit(background, (0,0))
    pygame.draw.rect(seccio_transparent,(0,0,0,100),(0,35,140,68))
    # DIBUIXAR LA SUPERFÍCIE TRANSPARENT A LA FINESTRA
    pantalla.blit(seccio_transparent, (40, 40))
    # Dibuixem el text
    TextPantalla(pantalla, None, 24, "1.- Crèdits", WHITE, (50,80))
    TextPantalla(pantalla, None, 24, "2.- Jugar", WHITE,(50,100))
    TextPantalla(pantalla,None, 24, "3.- Sortir", WHITE, (50,120))
    pygame.display.update()

#animacioinici()
menuprincipal()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_2:
                partida = True
            if event.key == K_3:
                running = False

    if partida == True:
       BACKGROUND_IMAGE = 'Assets/fondo.png'
       videsjugador1 = 3
       videsjugador2 = 3
       while True:
    #contador
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # controlar trets de les naus
            if event.type == KEYDOWN:
                #jugador 1
                if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time
                # jugador 2
                if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time

        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_LEFT]:
            player_rect2.x -= velocitat_nau2
        if keys[K_RIGHT]:
            player_rect2.x += velocitat_nau2



        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())

        #dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        #Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1: # bucle que recorre totes les bales
            bala.y -= velocitat_bales # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_jugador1.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                videsjugador2 -= 1
                print("Queda", videsjugador2, "vides al jugador 2!")
                bales_jugador1.remove(bala)  # eliminem la bala
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala_imatge, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                videsjugador1 -= 1
                print("Queda", videsjugador1, "vides al jugador 1!")
                bales_jugador2.remove(bala)  # eliminem la bala
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1
        if videsjugador1 == 0 or videsjugador2 == 0:
            score = True
            while score:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            score = False
                pantalla.fill((0,0,0))
                if videsjugador1 == 0:
                    TextPantalla(pantalla,None,60, "Player 2 wins", (255,0,0), (20,80))
                    TextPantalla(pantalla,None,20, "Press space to continue.", (255,255,255), (80,130))
                if videsjugador2 == 0:
                    TextPantalla(pantalla,None,60, "Player 1 wins", (255,0,0), (20,80))
                    TextPantalla(pantalla,None,20, "Press space to continue.", (255,255,255), (80,130))
                pygame.display.update()
            BACKGROUND_IMAGE = 'Assets/TitleScreen.png'
            partida = False
            menuprincipal()
            break
    



        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)

        pygame.display.update()
        clock.tick(fps)

    
            



