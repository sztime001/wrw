import pygame

def main():

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("img/cover.jpeg")
    background = pygame.image.load("img/background.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 600 x 500
    screen = pygame.display.set_mode((600,500))
    screen.blit(background, (0,0))


    # create a text box shows start game
    pygame.font.init()
    game_text = pygame.font.SysFont("Times",50)
    game_text_screen = game_text.render("Click to start game", True, (100,100,200))
    text_rect = game_text_screen.get_rect(center = (300, 250))
    screen.blit(game_text_screen, text_rect)
    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()