import pygame, time

AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'Assets/TitleScreen.png'
WHITE = (255,255,255)

pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load('Assets/musicadefons.mp3')
#pygame.mixer.music.play(-1, 12, 3000)
#pygame.mixer.music.set_volume(0.75)
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")
background = pygame.image.load(BACKGROUND_IMAGE).convert()

# CREAR LA SUPERFÍCIE TRANSPARENT I EL RECTANGLE SOBRE ELLA:
seccio_transparent = pygame.Surface((240,120),pygame.SRCALPHA)

def TextPantalla(pantalla, font, tamany, text, color, posicio):
    font = pygame.font.SysFont(font,tamany)
    img = font.render(text, True, color)
    pantalla.blit(img, posicio)

def menuprincipal():
    pantalla.blit(background, (0,0))
    pygame.draw.rect(seccio_transparent,(0,0,0,100),(0,35,140,68))
    pantalla.blit(seccio_transparent, (40, 40))
    TextPantalla(pantalla, None, 24, "1.- Crèdits", WHITE, (50,80))
    TextPantalla(pantalla, None, 24, "2.- Jugar", WHITE,(50,100))
    TextPantalla(pantalla,None, 24, "3.- Sortir", WHITE, (50,120))

menuprincipal()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Imprimeixo imatge de fons:
    # DIBUIXAR LA SUPERFÍCIE TRANSPARENT A LA FINESTRA
    # dibuixem el text
    pygame.display.update()

