# Aquest Joc és un "clon" del joc "Flappy Bird".
from pygame.locals import *
import pygame, random, time


AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/background.png'
TITLE_BACKGROUND_IMAGE = 'assets/backgroundmenu.png'
MAR = 'assets/mar.png'
WHITE = (255,255,255)
running = True
partida = False

#Carregar la tortuga que nos da pena
imatge_tortuga = pygame.image.load('assets/tortuga.png')

#Carregar el suelo
imatge_suelo = pygame.image.load('assets/suelo.png')

#Carregar obstaculos
imatge_obstaculo = pygame.image.load('assets/obstaculo.png')


#Si tenem que calcular temps, necessitem aquesta variable per evitar que hi ha coses que apparecen si les intervales no són valides.
temps_pause = 0

temps_obstaculos = 1440 # 1,4 segons entre obstacles
velocitat_obstaculos = 4

#jugador
gravitat = 0.27
velocitat_tortuga = 0
best_score = 0
#temps_entre_punts = 1440



pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Turtle Dive")
background = pygame.image.load(BACKGROUND_IMAGE).convert()
altures_obstaculos = [500,325,200]
play_image = pygame.Surface((157,45))
play_button = play_image.get_rect(topleft=(312, 250))
score_image = pygame.Surface((157,45))
score_button = score_image.get_rect(topleft=(312, 307))
credits_image = pygame.Surface((157,45))
credits_button = credits_image.get_rect(topleft=(312, 366))
exit_image = pygame.Surface((157,45))
exit_button = exit_image.get_rect(topleft=(312, 423))
so_score = pygame.mixer.Sound('assets/sound_sfx_point.wav')
so_mort = pygame.mixer.Sound('assets/sound_sfx_die.wav')
musica = pygame.mixer.Sound('assets/coral_chorus.mp3')
musica.play(loops=-1)
musica.set_volume(0.3)


#FPS
clock = pygame.time.Clock()
fps = 60

#Definició per imprimir imatge de fons:
def imprimir_pantalla_fons(image):
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

#Definició per imprimir el suelo 2 vegades (per què tiene un efecte de movimento)
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
            for i in range(0,150):
                time.sleep(0.02)
                imprimir_pantalla_fons(MAR)
                recttransparent((0,0,0,150),(175,0,450,600))
                TextPantalla(pantalla,'Comic Sans MS',22, "Programa: Arno B., Kristopher G., ", (WHITE), (200,i+20))
                TextPantalla(pantalla, 'Comic Sans MS',22,"Xavi Sancho, Clear Code, Biel G.", (WHITE),(200,i+60))
                TextPantalla(pantalla,'Comic Sans MS',22, "Gràfics: Kristopher G.", (WHITE), (200,i+100))
                TextPantalla(pantalla,'Comic Sans MS',22, "Música: Trap Music Now", (WHITE), (200,i+140))
                TextPantalla(pantalla,'Comic Sans MS',22, "Efectes de so: Clear Code", (WHITE), (200,i+180))
                pygame.display.update()
            TextPantalla(pantalla,'Comic Sans MS',17, "Premeu la barra espaiadora per continuar...", (WHITE), (225,390))
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
    imprimir_pantalla_fons(TITLE_BACKGROUND_IMAGE)
    #recttransparent((0,0,0,100),(225,110,350,380))
    #TextPantalla(pantalla, 'Comic Sans MS', 36, "1.- Crèdits", WHITE, (256.25,120+35))
    #TextPantalla(pantalla, 'Comic Sans MS', 36, "2.- Score", WHITE,(256.25,190+35))
    #TextPantalla(pantalla, 'Comic Sans MS', 36, "Q.- Sortir", WHITE, (245,260+35))
    #TextPantalla(pantalla, 'Comic Sans MS', 20, "Premeu espai per jugar.", WHITE,(290,400+35))
    pygame.display.update()



menuprincipal()
while running:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_2:
                credits()
            if event.key == K_SPACE:
                partida = True
            if event.key == K_q:
                running = False
            if event.key == K_1:
                animacio_infoscore = True
                infoscore = True
                while infoscore:
                    if animacio_infoscore:
                        imprimir_pantalla_fons(MAR)
                        recttransparent((0,0,0,150),(225,110,350,350))
                        TextPantalla(pantalla,'Comic Sans MS',40,"Millor puntuació",(WHITE),(254,140))
                        if best_score < 10:
                            TextPantalla(pantalla,'Comic Sans MS',150,str(best_score),(WHITE),(350,200))
                        elif best_score < 100:
                            TextPantalla(pantalla,'Comic Sans MS',150,str(best_score),(WHITE),(318,200))
                        elif best_score < 1000:
                            TextPantalla(pantalla,'Comic Sans MS',150,str(best_score),(WHITE),(265,200))
                        else:
                            best_score = 999
                            TextPantalla(pantalla,'Comic Sans MS',150,str(best_score),(WHITE),(310,200))
                        TextPantalla(pantalla,'Comic Sans MS',16, "Premeu la barra espaiadora per continuar...", (WHITE), (242,430))    
                        pygame.display.update()
                        animacio_infoscore = False
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == KEYDOWN:
                                if event.key == K_SPACE and animacio_infoscore == False:
                                    infoscore = False
                                    menuprincipal()
                    pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if play_button.collidepoint(event.pos):
                partida = True
            if credits_button.collidepoint(event.pos):
                credits()
            if exit_button.collidepoint(event.pos):
                running = False
            if score_button.collidepoint(event.pos):
                animacio_infoscore = True
                infoscore = True
                while infoscore:
                    if animacio_infoscore:
                        imprimir_pantalla_fons(MAR)
                        recttransparent((0,0,0,150),(225,110,350,350))
                        TextPantalla(pantalla,'Comic Sans MS',40,"Millor puntuació",(WHITE),(254,140))
                        if best_score < 10:
                            TextPantalla(pantalla,'Comic Sans MS',150,str(best_score),(WHITE),(350,200))
                        elif best_score < 100:
                            TextPantalla(pantalla,'Comic Sans MS',150,str(best_score),(WHITE),(318,200))
                        elif best_score < 1000:
                            TextPantalla(pantalla,'Comic Sans MS',150,str(best_score),(WHITE),(265,200))
                        else:
                            best_score = 999
                            TextPantalla(pantalla,'Comic Sans MS',150,str(best_score),(WHITE),(310,200))
                        TextPantalla(pantalla,'Comic Sans MS',16, "Premeu la barra espaiadora per continuar...", (WHITE), (242,430))    
                        pygame.display.update()
                        animacio_infoscore = False
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == KEYDOWN:
                                if event.key == K_SPACE and animacio_infoscore == False:
                                    infoscore = False
                                    menuprincipal()



    if partida == True:
        current_time = pygame.time.get_ticks()
        player_rect = imatge_tortuga.get_rect(midbottom=(AMPLADA // 4.5, ALTURA - 270))
        game_over = False
        pause = False
        score = 0
        comptador = 0 #Per evitar que els obstacles aparacen multiples veces seguides.
        ultima_posicio = 0 #Per saber qué estava l'ultima posició dels obstacles.
        temps_ultim_obstaculo = 0 #La ultima vegada que va venir el obstaculo.
        pos_x_suelo = 0 #La posicio del suelo
        obstaculos = [] #Llista per guardar els obstaculos
        score_possible = True
        comptador_so = 0
        #temps_ultim_punt = current_time + 2500
        #if best_score > 0:
           # temps_ultim_punt = current_time + 1500 



        while partida:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        velocitat_tortuga = 0
                        velocitat_tortuga -= 6
                    #Pause
                    if event.key == K_ESCAPE:
                        pause = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        velocitat_tortuga = 0
                        velocitat_tortuga -= 6


            # Mantenir al jugador dins de la pantalla:
            player_rect.clamp_ip(pantalla.get_rect())
            imprimir_pantalla_fons(BACKGROUND_IMAGE)


            for obstaculo in obstaculos:    
                if obstaculo.right < 0:
                    obstaculos.remove(obstaculo)
                #else:
                #    pantalla.blit(imatge_obstaculo,obstaculo)
                
                if player_rect.colliderect(obstaculo):
                    so_mort.play()
                    velocitat_tortuga = 0
                    game_over = True
            
            #Per comptar el score cada vegada que el jugador està entre un obstaculo.
            if obstaculos:
                for obstaculo in obstaculos:
                    if 95 < obstaculo.centerx < 105 and score_possible:
                        score += 1
                        comptador_so += 1
                        if comptador_so == 5:
                            so_score.play()
                            comptador_so = 0
                        score_possible = False
                    if obstaculo.centerx < 0:
                        score_possible = True


            if player_rect.top < 2 or player_rect.bottom > 500:
                velocitat_tortuga = 4
                so_mort.play()
                game_over = True
            
            if current_time - temps_ultim_obstaculo >= temps_obstaculos:
                pos_aleatoria_obstaculo = random.choice(altures_obstaculos)
                obstaculo_abajo = imatge_obstaculo.get_rect(midtop = (900,pos_aleatoria_obstaculo))
                obstaculo_arriba = imatge_obstaculo.get_rect(midbottom = (900,pos_aleatoria_obstaculo-175))
                obstaculos.append(pygame.Rect(obstaculo_abajo.topleft[0],obstaculo_abajo.topleft[1],125,600))
                obstaculos.append(pygame.Rect(obstaculo_arriba.topleft[0],obstaculo_arriba.topleft[1],125,600))
                if ultima_posicio == pos_aleatoria_obstaculo:
                    comptador += 1
                if comptador == 1:
                    while ultima_posicio == pos_aleatoria_obstaculo:
                        pos_aleatoria_obstaculo = random.choice(altures_obstaculos)
                    comptador = 0
                ultima_posicio = pos_aleatoria_obstaculo
                temps_ultim_obstaculo = current_time

            #if current_time - temps_ultim_punt >= temps_entre_punts:
             #   score += 1
              #  temps_ultim_punt = current_time


            pantalla.blit(imatge_tortuga, player_rect)
            velocitat_tortuga += gravitat
            player_rect.y += velocitat_tortuga

            if pause == True:
                temps_pause = 0
                temps_pause = current_time
                imprimir_suelo()
                recttransparent((0,0,0,150),(0,0,300,600))
                TextPantalla(pantalla,None,50,"PAUSE",(WHITE),(92.5,85))
                TextPantalla(pantalla,None,35,"ESC.- Resumir",(WHITE),(20,155))
                TextPantalla(pantalla,None,35,"M.- Menù principal",(WHITE),(20,200))
                TextPantalla(pantalla,None,35,"Q.- Quitar joc",(WHITE),(20,245))
                pygame.display.update()
                while pause == True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()       
                        if event.type == KEYDOWN:      
                            if event.key == K_ESCAPE:
                                pause = False
                            if event.key == K_m:
                                pause = False
                                game_over = True
                            if event.key == K_q:
                                pause = False
                                partida = False
                                running = False
                    current_time = pygame.time.get_ticks()
                temps_ultim_obstaculo = current_time - temps_pause + temps_ultim_obstaculo
                #temps_ultim_punt = current_time - temps_pause + temps_ultim_punt

            TextPantalla(pantalla,'Comic Sans MS', 40, str(score),(0,0,0),(380,0))

            pos_x_suelo -= 4
            imprimir_suelo()
            if pos_x_suelo <= -800:
                pos_x_suelo = 0

            for obstaculo in obstaculos:
                obstaculo.x -= velocitat_obstaculos
                pantalla.blit(imatge_obstaculo,obstaculo)


            if game_over == True:
                if score > best_score:
                    best_score = score
                partida = False
                obstaculo_abajo = 0
                obstaculo_arriba = 0                    
                menuprincipal()


            pygame.display.update()
            clock.tick(fps)