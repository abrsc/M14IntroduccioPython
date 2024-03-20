import pygame, time

AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'Assets/TitleScreen.png'

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

def menuprincipal():
    pantalla.blit(background, (0,0))
    pygame.draw.rect(seccio_transparent,(0,0,0,100),(0,35,140,68))
    font = pygame.font.SysFont(None,25)
    img = font.render("1.- Crèdits", True, (255,255,255))
    img2 = font.render("2.- Jugar", True, (255,255,255))
    img3= font.render("3.- Sortir", True, (255,255,255))
    pantalla.blit(seccio_transparent, (40, 40))
    pantalla.blit(img, (50, 80))
    pantalla.blit(img2, (50, 100))
    pantalla.blit(img3, (50, 120))

menuprincipal()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Imprimeixo imatge de fons:
    # DIBUIXAR LA SUPERFÍCIE TRANSPARENT A LA FINESTRA
    # dibuixem el text
    pygame.display.update()

