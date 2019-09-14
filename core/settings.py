import pygame


class Settings:
    """ Settings, stores the default value of the game configurations """
    def __init__(self):
        """ Initialize default values """

        # Window's width and heigh
        self.WINDOW_HEIGHT = 720
        self.WINDOW_WIDTH = 1280

        # Window's background color
        self.BACKGROUND_COLOR = (230, 230, 230)

        # Window's main clock
        self.main_clock = pygame.time.Clock()

        # player win point sound
        self.win_point_sound = pygame.mixer.Sound('wav/winpoint.wav')

        # enemy win point sound
        self.lose_point_sound = pygame.mixer.Sound('wav/losepoint.wav')

        # player wins game
        self.win_game_sound = pygame.mixer.Sound('wav/winsound.wav')

        # enemy wins game
        self.lose_game_sound = pygame.mixer.Sound('wav/losesound.wav')
