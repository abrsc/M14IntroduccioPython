# import the pygame module, so you can use it
import pygame, sys
while True:
    WIDTH = input("Que amplada de finestra vols (px)?: ")
    HIGH = input("Que alçada de finestra vols (px)?: ")
    try:
        int(WIDTH)
        int(HIGH)
        break
    except:
        print("Error, solament nùmeros són acceptats")
        continue
while True:
    icon = (input("""
    Que vols com icona?
    1. Gat
    2. Peix
    3. Planeta
    4. Tanc
    Insereu el nùmero corresponant:
    """))
    if icon == "1":
        LOGO_IMAGE = "assets/gat.png"
        break
    elif icon == "2":
        LOGO_IMAGE = "assets/peix.png"
        break
    elif icon == "3":
        LOGO_IMAGE = "assets/planeta.png"
        break
    elif icon == "4":
        LOGO_IMAGE = "assets/tank.png"
        break
    else:
        print("Error s'ha de sel·leccionar un numero entre 1 i 4.")
CAPTION_TEXT = input("Si us plau sel·lecciona un nom de joc: ")
# create a surface on screen that has the size of 640 x 480
while True:
    backgroundchoice = input("Vols que el font de joc sea un imatge o un color? (1 = imatge, 2 = color): ")
    if backgroundchoice == "1":
        background_choice_image = input("""
        Que vols com font?
        1. Lleó
        2. Ocean
        3. Espai
        4. Tanc
        Insereu el nùmero corresponant:
        """)
        if background_choice_image == "1":
            BACKGROUND_IMAGE = "assets/zoo.jpeg"
            break
        elif background_choice_image == "2":
            BACKGROUND_IMAGE = "assets/oceanback.jpg"
            break
        elif background_choice_image == "3":
            BACKGROUND_IMAGE = "assets/space.jpg"
            break
        elif background_choice_image == "4":
            BACKGROUND_IMAGE = "assets/war.webp"
            break
        else:
            print("Error. S'ha de sel·leccionar entre 1 i 4")
    elif backgroundchoice == "2":
        while True:
            red = (input("Quantitat de vermell que vols: "))
            green = (input("Quantitat de verd que vols: "))
            blue = (input("Quantitat de blau que vols: "))
            if int(red) <= 255 and int(green) <= 255 and int(blue) <= 255 and int(red) >= 0 and int(green) >= 0 and int(blue) >= 0:
                colors_valid = 1
                break
            else:
                print("El valor s'ha de ser entre 0 i 255 per cada color")
        if colors_valid == 1:
            break
    else:
        print("Error. S'ha de sel·leccionar entre 1 i 2.")
while True:
    pantalla = (input("Pantalla sencera? (1 = si, 2 = no): "))
    if pantalla == "1":
        screen = pygame.display.set_mode((int(WIDTH), int(HIGH)), pygame.FULLSCREEN)
        break
    elif pantalla == "2":
        screen = pygame.display.set_mode((int(WIDTH), int(HIGH)))
        break
    else:
        print("Error numero invalid.")
# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(LOGO_IMAGE)
    # set the logo of the screen
    pygame.display.set_icon(logo)
    # set the caption of the screen
    pygame.display.set_caption(CAPTION_TEXT)
    # load bg image if needed
    if backgroundchoice == "1":
        background = pygame.image.load(BACKGROUND_IMAGE).convert()
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # background set to BLACK
        if int(backgroundchoice) == 2:
            screen.fill((int(red), int(green), int(blue)))
        elif int(backgroundchoice) == 1:
            screen.blit(background, (0, 0))
        else:
            print("Error.")
            break
        # draw the screen
        pygame.display.flip()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()