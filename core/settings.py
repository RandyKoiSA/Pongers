import pygame


class Settings:
    """ Settings, stores the default value of the game configurations """
    def __init__(self):
        """ Initialize default values """
        # Window's width and heigh
        self.WINDOW_HEIGHT = 720
        self.WINDOW_WIDTH = 1280
        self.BACKGROUND_COLOR = (230, 230, 230)
        self.main_clock = pygame.time.Clock()

        self.anchor_topleft = (0, 0)
        self.anchor_topmid = (self.WINDOW_WIDTH/2, 0)
        self.anchor_topright = (self.WINDOW_WIDTH, 0)
        self.anchor_midleft = (0, self.WINDOW_HEIGHT/2)
        self.anchor_middle = (self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/2)
        self.anchor_midright = (self.WINDOW_WIDTH, self.WINDOW_HEIGHT/2)
        self.anchor_midleft = (0, self.WINDOW_HEIGHT)
        self.anchor_middle = (self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT)
        self.anchor_midright = (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        # player win point sound
        self.win_point_sound = pygame.mixer.Sound('wav/winpoint.wav')
        # enemy win point sound
        self.lose_point_sound = pygame.mixer.Sound('wav/losepoint.wav')
        # player wins game
        self.win_game_sound = pygame.mixer.Sound('wav/winsound.wav')
        # enemy wins game
        self.lose_game_sound = pygame.mixer.Sound('wav/losesound.wav')
