import pygame
from core import controller, gamemode, settings
from screens import screenmanager


def run_game():
    """ Initial function to run the game """

    # Initialize pygame
    pygame.init()

    # Setup settings
    pong_settings = settings.Settings()
    main_screen = pygame.display.set_mode((pong_settings.WINDOW_WIDTH, pong_settings.WINDOW_HEIGHT))
    pygame.display.set_caption("Pong by Randy Le 2019")

    # Initialize a game mode
    pong_gamemode = gamemode.Gamemode()

    # Initialize a player controller
    player_controller = controller.Controller()

    # Initialize screen manager
    screen_manager = screenmanager.ScreenManager(main_screen, pong_settings, pong_gamemode, player_controller)

    while True:
        """ Game loop, as long as this is true the game will still run."""
        main_screen.fill(pong_settings.BACKGROUND_COLOR)
        screen_manager.run()

        # Display the screen onto the window
        pygame.display.flip()
        pong_settings.main_clock.tick(30)


run_game()
