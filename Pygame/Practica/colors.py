import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
VIOLET = (149, 53, 83)
GREY = (128, 128, 128)
MAROON = (128, 0, 0)
BLACK = (0, 0, 0)
OLIVE = (128, 128, 0)
CYAN = (0,255,255)
PINK = (255, 192, 203)
MAGENTA = (255, 0, 255)
TAN = (210, 180, 140)
TEAL = (0, 128, 128)

    # while True:
    # color = input("""Que color vols?:
    # RED, GREEN, BLUE, INDIGO, ORANGE, YELLOW, VIOLET,
    # GREY, MAROON, BLACK, OLIVE, CYAN, PINK, MAGENTA, TAN, TEAL:
    # """)
    # if color == "RED":
    #     color = RED
    #     break
    # elif color == "GREEN":
    #     color = GREEN
    #     break
    # elif color == "BLUE":
    #     color = BLUE
    #     break
    # elif color == "INDIGO":
    #     color = INDIGO
    #     break
    # elif color == "ORANGE":
    #     color = ORANGE
    #     break
    # elif color == "YELLOW":
    #     color = YELLOW
    #     break
    # elif color == "VIOLET":
    #     color = VIOLET
    #     break
    # elif color == "GREY":
    #     color = GREY
    #     break
    # elif color == "MAROON":
    #     color = MAROON
    #     break
    # elif color == "BLACK":
    #     color = BLACK
    #     break
    # elif color == "OLIVE":
    #     color = OLIVE
    #     break
    # elif color == "CYAN":
    #     color = CYAN
    #     break
    # elif color == "MAGENTA":
    #     color = MAGENTA
    #     break
    # elif color == "TAN":
    #     color = TAN
    #     break
    # elif color == "TEAL":
    #     color = TEAL
    #     break
    # else:
    #     print("ERROR! S'HA DE SER EN MAJUSCULA!")

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Color de fons')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((255, 255, 255))
    rectangle1 = pygame.Rect(0, 0, 150, 600)
    rectangle2 = pygame.Rect(0, 0, 600, 75)
    rectangle3 = pygame.Rect(450, 0, 150, 600)
    rectangle4 = pygame.Rect(0, 250, 600, 75)
    pygame.draw.rect(pantalla, RED, rectangle1)
    pygame.draw.rect(pantalla, RED, rectangle2)
    pygame.draw.rect(pantalla, RED, rectangle3)
    pygame.draw.rect(pantalla, RED, rectangle4)
    pygame.display.update()