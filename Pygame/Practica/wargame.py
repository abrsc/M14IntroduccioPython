# import the pygame module, so you can use it
import pygame, sys
BACKGROUND_IMAGE = 'assets/war.webp'
WIDTH = 800
HIGH = 600
LOGO_IMAGE = "assets/tank.png"
CAPTION_TEXT = "War BRESCIA"
# create a surface on screen that has the size of 640 x 480
screen = pygame.display.set_mode((WIDTH, HIGH))

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
    # load bg image
    background = pygame.image.load(BACKGROUND_IMAGE).convert()
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # background set to image
        screen.blit(background, (0,0))
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