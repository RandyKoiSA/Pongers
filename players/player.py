import pygame
from custom.vector_point import Vector
from players.player_base import Player_Base

class Player(Player_Base):
    """ Player sprite that holds all the attribute and details of what the player has """
    def __init__(self, screen, controller, settings, player_type, width=100, height=5, color=(0, 0, 0), velocity=Vector(20,5)):
        """ Initialise default values """
        super().__init__(screen, controller, settings, player_type, width, height, color, velocity)

        # Create the rectangle and position the player
        self.rect = pygame.Rect(((self.settings.WINDOW_WIDTH / 2) - (self.player_width / 2),
                                 self.settings.WINDOW_HEIGHT - self.player_height - 20),
                                (self.player_width, self.player_height))

    def update(self):
        """ Update the player based on controller inputs"""
        if self.controller.MOVELEFT:
            self.rect.x -= self.velocity.x

        if self.controller.MOVERIGHT:
            self.rect.x += self.velocity.x

        self.check_boundaries()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 5)

    def check_boundaries(self):
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > self.settings.WINDOW_WIDTH:
            self.rect.right = self.settings.WINDOW_WIDTH

