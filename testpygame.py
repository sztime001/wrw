import pygame


def game_setting_loop(screen):
    running = True
    game_text = pygame.font.SysFont("Times",20)
    game_text_instruction = "game instruction:\n press corresponding key to add \
                             character in game.\n\n \
                             W: Werewolf                M: Minion\n\
                             S: Seer                    V: Villager\n\
                             R: Robber                  T: Trouble maker\n\
                             D: Drunk                   A: tAnner\n\
                             O: masOn                   I: Insomniac"
    game_text_screen = game_text.render(game_text_instruction, True, (100,100,200))
    text_rect = game_text_screen.get_rect(center = (300, 100))
    screen.blit(game_text_screen, text_rect)
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("key pressed")

    print("setting completed")
    return

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
    game_text_screen = game_text.render("Press ENTER to start game...", True, (100,100,200))
    text_rect = game_text_screen.get_rect(center = (300, 250))
    screen.blit(game_text_screen, text_rect)
    pygame.display.update()

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("key pressed")
                    game_setting_loop(screen)

        clock.tick(10)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()