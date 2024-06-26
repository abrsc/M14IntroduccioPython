import time
from pygame.locals import *
import pygame

AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'assets/TitleScreen.png'
WHITE = (255,255,255)
running = True
partida = False

sprite_vides = 'assets/cor1.0.png'
vides_image = pygame.image.load(sprite_vides)
sprite_energia = 'assets/energia.png'
energia_image = pygame.image.load(sprite_energia)
sprite_escut = 'assets/escut.png'
escut_image = pygame.image.load(sprite_escut)
sprite_velocitat = 'assets/velocitat.png'
velocitat_image = pygame.image.load(sprite_velocitat)
# Bala rectangular blanca:
sprite_bala = 'assets/tretnau.png'
bala_imatge = pygame.image.load(sprite_bala)
sprite_bala2 = 'assets/tretnau2.png'
bala_imatge2 = pygame.image.load(sprite_bala2)
#bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
#bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 4.5
temps_entre_bales = 1000 #1 segon
temps_invicibilitat = 3000 #2 segon (+1 d'animacions)
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2
temps_ultim_golp_jugador1 = 0
temps_ultim_golp_jugador2 = 0
temps_energia = 20000 #20 segons
temps_poder_escut = 1000 # 1 segon
temps_poder_velocitat = 3000 # 3 segons
temps_ultim_energia_jugador1 = 0
temps_ultim_energia_jugador2 = 0
temps_pause = 0
temps_partida = 300000 #5min

pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load('assets/musicadefons.mp3')
#pygame.mixer.music.play(-1, 12, 3000)
#pygame.mixer.music.set_volume(0.75)
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Vaseleyo")
background = pygame.image.load(BACKGROUND_IMAGE).convert()

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

def credits():
    animaciocreditacabat = False
    credits = True
    while credits == True:
        if animaciocreditacabat == False:
            for i in range(0,60):
                time.sleep(0.02)
                pantalla.fill((0,0,0))
                TextPantalla(pantalla,None,22, "Programa: Arno B., Xavi Sancho, Biel G.", (WHITE), (20,i))
                TextPantalla(pantalla,None,22, "Gràfics: Arno B., Kristopher G.", (WHITE), (20,i+20))
                TextPantalla(pantalla,None,22, "Música: -", (WHITE), (20,i+38))
                TextPantalla(pantalla,None,22, "Efectes de so: -", (WHITE), (20,i+56))
                pygame.display.update()
            TextPantalla(pantalla,None,17, "Premeu la barra espaiadora per continuar..", (WHITE), (40,180))
            animaciocreditacabat = True
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        credits = False
                        menuprincipal()
        pygame.display.update()

def menuprincipal():
    # Imprimeixo imatge de fons:
    pantalla.blit(background, (0,0))
    # CREAR LA SUPERFÍCIE TRANSPARENT I EL RECTANGLE SOBRE ELLA:
    seccio_transparent = pygame.Surface((320,200),pygame.SRCALPHA)
    pygame.draw.rect(seccio_transparent,(0,0,0,100),(0,35,140,68))
    # DIBUIXAR LA SUPERFÍCIE TRANSPARENT A LA FINESTRA
    pantalla.blit(seccio_transparent, (40, 40))
    # Dibuixem el text
    TextPantalla(pantalla, None, 24, "1.- Crèdits", WHITE, (50,80))
    TextPantalla(pantalla, None, 24, "2.- Jugar", WHITE,(50,100))
    TextPantalla(pantalla,None, 24, "3.- Sortir", WHITE, (50,120))
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
            if event.key == K_3:
                running = False

    if partida == True:
       current_time = pygame.time.get_ticks()
       BACKGROUND_IMAGE = 'assets/fondo.png'
       pause = False
       videsjugador1 = 3
       videsjugador2 = 3
       energiajugador1 = 1
       energiajugador2 = 1
       invulnerabilitatjugador1 = False
       invulnerabilitatjugador2 = False
       boostvelocitatjugador1 = False
       boostvelocitatjugador2 = False
       bales_total_utilitzades_jugador1 = 0
       bales_total_utilitzades_jugador2 = 0
       precisio_jugador1 = 0
       precisio_jugador2 = 0
       temps_inici_partida = current_time
       draw = False
       # Jugador 1:
       sprite_player1 = 'assets/Nau.png'
       player_image = pygame.image.load(sprite_player1)
       player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 15))
       velocitat_nau = 2

       # Jugador 2:
       sprite_player2 = 'assets/Nau2.png'
       player_image2 = pygame.image.load(sprite_player2)
       player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 155))
       velocitat_nau2 = 2
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
                    bales_jugador1.append(pygame.Rect(player_rect.centerx-6, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time
                if event.key == K_e and energiajugador1 > 0:
                    invulnerabilitatjugador1 = True
                    energiajugador1 -= 1      
                    temps_ultim_energia_jugador1 = current_time
                if event.key == K_r and energiajugador1 > 0:
                    boostvelocitatjugador1 = True
                    energiajugador1 -= 1      
                    temps_ultim_energia_jugador1 = current_time                 
                # jugador 2
                if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx-6, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time
                if event.key == K_KP_0 and energiajugador2 > 0:
                    invulnerabilitatjugador2 = True
                    energiajugador2 -= 1
                    temps_ultim_energia_jugador2 = current_time
                if event.key == K_RSHIFT and energiajugador2 > 0:
                    boostvelocitatjugador2 = True
                    energiajugador2 -= 1      
                    temps_ultim_energia_jugador2 = current_time   
                #Pause
                if event.key == K_ESCAPE:
                    pause = True


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
            bala.y -= velocitat_bales+0.5 # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_total_utilitzades_jugador1 += 1
                bales_jugador1.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                if current_time - temps_ultim_golp_jugador2 >= temps_invicibilitat and invulnerabilitatjugador2 == False:
                    videsjugador2 -= 1
                    bales_total_utilitzades_jugador1 += 1
                    precisio_jugador1 += 1
                    print("Queda", videsjugador2, "vides al jugador 2!")
                    sprite_player2 = 'assets/explosió.png'
                    player_image2 = pygame.image.load(sprite_player2)
                    BACKGROUND_IMAGE = 'assets/fondo.png'
                    background = pygame.image.load(BACKGROUND_IMAGE).convert()
                    pantalla.blit(background, (0, 0))
                    pantalla.blit(player_image, player_rect)
                    pantalla.blit(player_image2, player_rect2)
                    if videsjugador1 > 2:
                        pantalla.blit(vides_image, (304,184))
                        pantalla.blit(vides_image, (304-16,184))
                        pantalla.blit(vides_image, (304-32,184))
                    elif videsjugador1 > 1:
                        pantalla.blit(vides_image, (304,184))
                        pantalla.blit(vides_image, (304-16,184))
                    elif videsjugador1 > 0:
                        pantalla.blit(vides_image, (304,184))

                    if videsjugador2 > 2:
                        pantalla.blit(vides_image, (0,0))
                        pantalla.blit(vides_image, (16,0))
                        pantalla.blit(vides_image, (32,0))
                    elif videsjugador2 > 1:
                        pantalla.blit(vides_image, (0,0))
                        pantalla.blit(vides_image, (16,0))
                    elif videsjugador2 > 0:
                        pantalla.blit(vides_image, (0,0))
                    pygame.display.update()
                    temps_ultima_bala_jugador1 += 1000
                    temps_ultima_bala_jugador2 +=1000
                    time.sleep(1)
                    sprite_player2 = 'assets/Nau2.png'
                    player_image2 = pygame.image.load(sprite_player2)
                    pantalla.blit(background, (0, 0))
                    pantalla.blit(player_image, player_rect)
                    pantalla.blit(player_image2, player_rect2)
                    pygame.display.update()
                    temps_ultim_golp_jugador2 = current_time
                bales_jugador1.remove(bala)  # eliminem la bala
                try:
                    for bala in bales_jugador2:
                        bales_jugador2.remove(bala)
                    bales_total_utilitzades_jugador2 += 1
                except:
                    continue
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_total_utilitzades_jugador2 += 1
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala_imatge2, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                if current_time - temps_ultim_golp_jugador1 >= temps_invicibilitat and invulnerabilitatjugador1 == False:
                    videsjugador1 -= 1
                    bales_total_utilitzades_jugador2 += 1
                    precisio_jugador2 += 1
                    print("Queda", videsjugador1, "vides al jugador 1!")
                    sprite_player1 = 'assets/explosió.png'
                    player_image = pygame.image.load(sprite_player1)
                    BACKGROUND_IMAGE = 'assets/fondo.png'
                    background = pygame.image.load(BACKGROUND_IMAGE).convert()
                    pantalla.blit(background, (0, 0))
                    pantalla.blit(player_image, player_rect)
                    pantalla.blit(player_image2, player_rect2)
                    if videsjugador1 > 2:
                        pantalla.blit(vides_image, (304,184))
                        pantalla.blit(vides_image, (304-16,184))
                        pantalla.blit(vides_image, (304-32,184))
                    elif videsjugador1 > 1:
                        pantalla.blit(vides_image, (304,184))
                        pantalla.blit(vides_image, (304-16,184))
                    elif videsjugador1 > 0:
                        pantalla.blit(vides_image, (304,184))

                    if videsjugador2 > 2:
                        pantalla.blit(vides_image, (0,0))
                        pantalla.blit(vides_image, (16,0))
                        pantalla.blit(vides_image, (32,0))
                    elif videsjugador2 > 1:
                        pantalla.blit(vides_image, (0,0))
                        pantalla.blit(vides_image, (16,0))
                    elif videsjugador2 > 0:
                        pantalla.blit(vides_image, (0,0))
                    pygame.display.update()
                    temps_ultima_bala_jugador1 += 1000
                    temps_ultima_bala_jugador2 +=1000
                    time.sleep(1)
                    sprite_player1 = 'assets/Nau.png'
                    player_image = pygame.image.load(sprite_player1)
                    pantalla.blit(background, (0, 0))
                    pantalla.blit(player_image, player_rect)
                    pantalla.blit(player_image2, player_rect2)
                    pygame.display.update()
                    temps_ultim_golp_jugador1 = current_time
                bales_jugador2.remove(bala)  # eliminem la bala
                try:
                    for bala in bales_jugador1:
                        bales_jugador1.remove(bala)
                    bales_total_utilitzades_jugador1 += 1
                except:
                    continue

        if videsjugador1 > 2:
            pantalla.blit(vides_image, (304,184))
            pantalla.blit(vides_image, (304-16,184))
            pantalla.blit(vides_image, (304-32,184))
        elif videsjugador1 > 1:
            pantalla.blit(vides_image, (304,184))
            pantalla.blit(vides_image, (304-16,184))
        elif videsjugador1 > 0:
            pantalla.blit(vides_image, (304,184))

        if videsjugador2 > 2:
            pantalla.blit(vides_image, (0,0))
            pantalla.blit(vides_image, (16,0))
            pantalla.blit(vides_image, (32,0))
        elif videsjugador2 > 1:
            pantalla.blit(vides_image, (0,0))
            pantalla.blit(vides_image, (16,0))
        elif videsjugador2 > 0:
            pantalla.blit(vides_image, (0,0))
        
        if energiajugador1 > 0:
            pantalla.blit(energia_image,(304-48,184))
        if energiajugador2 > 0:
            pantalla.blit(energia_image,(48,0))
        
        if energiajugador1 < 1 and current_time - temps_ultim_energia_jugador1 >= temps_energia:
            energiajugador1 += 1
        if energiajugador2 < 1 and current_time - temps_ultim_energia_jugador2 >= temps_energia:
            energiajugador2 += 1

        if invulnerabilitatjugador1 == True:
            pantalla.blit(escut_image, (304-48,184))
        if invulnerabilitatjugador2 == True:
            pantalla.blit(escut_image,(48,0))
        if invulnerabilitatjugador1 == True and current_time - temps_ultim_energia_jugador1 >= temps_poder_escut:
            invulnerabilitatjugador1 = False
        if invulnerabilitatjugador2 == True and current_time - temps_ultim_energia_jugador2 >= temps_poder_escut:
            invulnerabilitatjugador2 = False

                
        if boostvelocitatjugador1 == True and current_time - temps_ultim_energia_jugador1 >= temps_poder_velocitat:
            boostvelocitatjugador1 = False
            velocitat_nau = 2
        if boostvelocitatjugador2 == True and current_time - temps_ultim_energia_jugador2 >= temps_poder_velocitat:
            boostvelocitatjugador2 = False
            velocitat_nau2 = 2
        if boostvelocitatjugador1 == True:
            velocitat_nau = 4
            pantalla.blit(velocitat_image, (304-48,184))
            
        if boostvelocitatjugador2 == True:
            velocitat_nau2 = 4
            pantalla.blit(velocitat_image,(48,0))

        timer = int((temps_partida - (current_time - temps_inici_partida))/1000)
        if timer < 10:
            TextPantalla(pantalla,None,20,str(timer),(WHITE), (310,5))
        elif timer < 100:
            TextPantalla(pantalla,None,20,str(timer),(WHITE), (300,5))
        elif timer > 99:
            TextPantalla(pantalla,None,20,str(timer),(WHITE), (290,5))

        if pause == True:
            temps_pause = 0
            temps_pause = current_time
            seccio_transparent = pygame.Surface((320,200),pygame.SRCALPHA)
            pygame.draw.rect(seccio_transparent,(0,0,0,150),(0,0,320,200))
            pantalla.blit(seccio_transparent, (0, 0))
            TextPantalla(pantalla,None,50,"PAUSE",(WHITE),(100,85))
            pygame.display.update()
            while pause == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()       
                    if event.type == KEYDOWN:      
                        if event.key == K_ESCAPE:
                            pause = False
                current_time = pygame.time.get_ticks()
            pantalla.blit(background, (0, 0))
            pantalla.blit(player_image, player_rect)
            pantalla.blit(player_image2, player_rect2)
            if videsjugador1 > 2:
                pantalla.blit(vides_image, (304,184))
                pantalla.blit(vides_image, (304-16,184))
                pantalla.blit(vides_image, (304-32,184))
            elif videsjugador1 > 1:
                pantalla.blit(vides_image, (304,184))
                pantalla.blit(vides_image, (304-16,184))
            elif videsjugador1 > 0:
                pantalla.blit(vides_image, (304,184))

            if videsjugador2 > 2:
                pantalla.blit(vides_image, (0,0))
                pantalla.blit(vides_image, (16,0))
                pantalla.blit(vides_image, (32,0))
            elif videsjugador2 > 1:
                pantalla.blit(vides_image, (0,0))
                pantalla.blit(vides_image, (16,0))
            elif videsjugador2 > 0:
                pantalla.blit(vides_image, (0,0))
            temps_ultim_golp_jugador1 = current_time - temps_pause + temps_ultim_golp_jugador1
            temps_ultim_golp_jugador2 = current_time - temps_pause + temps_ultim_golp_jugador2 
            temps_ultima_bala_jugador1 = current_time - temps_pause + temps_ultima_bala_jugador1
            temps_ultima_bala_jugador2 = current_time - temps_pause + temps_ultima_bala_jugador2
            temps_ultim_energia_jugador1 = current_time - temps_pause + temps_ultim_energia_jugador1
            temps_ultim_energia_jugador2 = current_time - temps_pause + temps_ultim_energia_jugador2
            temps_inici_partida = current_time - temps_pause + temps_inici_partida
            pygame.display.update()


        if videsjugador1 == 0 or videsjugador2 == 0 or current_time - temps_inici_partida >= temps_partida:
            score = True
            animacio = True
            try:
                resultat_precisio_jugador1 = int((precisio_jugador1/bales_total_utilitzades_jugador1)*100)
            except:
                resultat_precisio_jugador1 = 0
            try:
                resultat_precisio_jugador2 = int((precisio_jugador2/bales_total_utilitzades_jugador2)*100)
            except:
                resultat_precisio_jugador2 = 0
            if current_time - temps_inici_partida >= temps_partida:
                if videsjugador1 > videsjugador2 and videsjugador1 != videsjugador2:
                    videsjugador2 = 0
                elif videsjugador2 > videsjugador1 and videsjugador2 != videsjugador1:
                    videsjugador1 = 0
                elif videsjugador1 == videsjugador2:
                    if resultat_precisio_jugador1 > resultat_precisio_jugador2 and resultat_precisio_jugador1 != resultat_precisio_jugador2:
                        videsjugador2 = 0
                    elif resultat_precisio_jugador2 > resultat_precisio_jugador1 and resultat_precisio_jugador1 != resultat_precisio_jugador2:
                        videsjugador1 = 0
                    elif resultat_precisio_jugador1 == resultat_precisio_jugador2:
                        draw = True
            while score:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            score = False
                if videsjugador1 == 0:
                    if animacio == True:
                        sprite_player1 = 'assets/explosió.png'
                        player_image = pygame.image.load(sprite_player1)
                        BACKGROUND_IMAGE = 'assets/fondo.png'
                        background = pygame.image.load(BACKGROUND_IMAGE).convert()
                        pantalla.blit(background, (0, 0))
                        pantalla.blit(player_image, player_rect)
                        pantalla.blit(player_image2, player_rect2)
                        pygame.display.update()
                        time.sleep(2)
                        pantalla.blit(background, (0, 0))
                        pantalla.blit(player_image2, player_rect2)
                        pygame.display.update()
                        time.sleep(1)
                        animacio = False
                    pantalla.fill((0,0,0))
                    TextPantalla(pantalla,None,60, "Player 2 wins", (255,0,0), (27,70))
                    TextPantalla(pantalla,None,20, "Press space to continue.", (255,255,255), (80,130))
                    TextPantalla(pantalla,None,17,"Precisió jugador 1: "+ str(resultat_precisio_jugador1) + "%", WHITE, (0,170))
                    TextPantalla(pantalla,None,17,"Precisió jugador 2: "+ str(resultat_precisio_jugador2) + "%", WHITE, (0,185))
                if videsjugador2 == 0:
                    if animacio == True:
                        sprite_player2 = 'assets/explosió.png'
                        player_image2 = pygame.image.load(sprite_player2)
                        BACKGROUND_IMAGE = 'assets/fondo.png'
                        background = pygame.image.load(BACKGROUND_IMAGE).convert()
                        pantalla.blit(background, (0, 0))
                        pantalla.blit(player_image, player_rect)
                        pantalla.blit(player_image2, player_rect2)
                        pygame.display.update()
                        time.sleep(2)
                        pantalla.blit(background, (0, 0))
                        pantalla.blit(player_image, player_rect)
                        pygame.display.update()
                        time.sleep(1)
                        animacio = False
                    pantalla.fill((0,0,0))
                    TextPantalla(pantalla,None,60, "Player 1 wins", (255,0,0), (27,70))
                    TextPantalla(pantalla,None,20, "Press space to continue.", (255,255,255), (80,130))
                    TextPantalla(pantalla,None,17,"Precisió jugador 1: "+ str(resultat_precisio_jugador1) + "%", WHITE, (0,170))
                    TextPantalla(pantalla,None,17,"Precisió jugador 2: "+ str(resultat_precisio_jugador2) + "%", WHITE, (0,185))
                if draw == True:
                    if animacio == True:
                        sprite_player1 = 'assets/explosió.png'
                        player_image = pygame.image.load(sprite_player1)
                        sprite_player2 = 'assets/explosió.png'
                        player_image2 = pygame.image.load(sprite_player2)
                        BACKGROUND_IMAGE = 'assets/fondo.png'
                        background = pygame.image.load(BACKGROUND_IMAGE).convert()
                        pantalla.blit(background, (0, 0))
                        pantalla.blit(player_image, player_rect)
                        pantalla.blit(player_image2, player_rect2)
                        pygame.display.update()
                        time.sleep(2)
                        pantalla.blit(background, (0, 0))
                        pygame.display.update()
                        time.sleep(1)
                        animacio = False
                    pantalla.fill((0,0,0))
                    TextPantalla(pantalla,None,60, "It's a draw!", (255,0,0), (52,70))
                    TextPantalla(pantalla,None,20, "Press space to continue.", (255,255,255), (80,130))
                    TextPantalla(pantalla,None,17,"Precisió jugador 1: "+ str(resultat_precisio_jugador1) + "%", WHITE, (0,170))
                    TextPantalla(pantalla,None,17,"Precisió jugador 2: "+ str(resultat_precisio_jugador2) + "%", WHITE, (0,185))                    
                pygame.display.update()
            
            BACKGROUND_IMAGE = 'assets/TitleScreen.png'
            background = pygame.image.load(BACKGROUND_IMAGE).convert()
            partida = False
            sprite_player1 = 'assets/Nau.png'
            sprite_player2 = 'assets/Nau2.png'
            player_image = pygame.image.load(sprite_player1)
            player_image2 = pygame.image.load(sprite_player2)
            try:
                for bala in bales_jugador1:
                    bales_jugador1.remove(bala)
                for bala in bales_jugador2:
                    bales_jugador2.remove(bala)
            except:
                menuprincipal()
            menuprincipal()
            break
    

        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)
        pygame.display.update()
        clock.tick(fps)