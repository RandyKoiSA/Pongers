import pygame


class PlayerBase:
    """ Player base that other players will inherits this class. """
    def __init__(self, screen, controller, settings, player_type, width, height, color, velocity, imagepath):
        """ Initialize default values. """
        # Reference to the screen to draw on
        self.screen = screen

        # Controller, to retrieve player's keyboard and mouse input
        self.controller = controller

        # Settings, to retrieve windows settings
        self.settings = settings

        # Player Type, to find out what type of player it is
        self.player_type = player_type

        # Width, get width of the player's bar
        self.player_width = width

        # Height, get height of the player's bar
        self.player_height = height

        # Color, the color of the player's bar
        self.color = color

        # Velocity, the x and y velocity of player's bar speed
        self.velocity = velocity

        # Image path to load
        self.image = pygame.image.load(imagepath)
