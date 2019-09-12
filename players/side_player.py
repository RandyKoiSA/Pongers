import pygame
from custom.vector_point import Vector
from players.player_base import Player_Base

class SidePlayer(Player_Base):
    """ Side player bar that holds all the attribute and details of what the player has. """
    def __init__(self, screen, controller, settings, bRightSide, player_type, width=5, height=100,
                 color=(0, 0, 0), velocity=Vector(20,20)):
        """ Initialize properties """
        super().__init__(screen, controller, settings, player_type, width, height, color, velocity)
        self.bRightSide = bRightSide

        if not bRightSide:
            self.rect = pygame.Rect((self.settings.WINDOW_WIDTH - self.player_width - 15,
                                     self.settings.WINDOW_HEIGHT / 2 + self.player_height),
                                    (self.player_width, self.player_height))
        else:
            self.rect = pygame.Rect((15,
                                     (self.settings.WINDOW_HEIGHT / 2 + self.player_height)),
                                    (self.player_width, self.player_height))

    def update(self):
        """ Update the player based on controller input """
        if self.controller.MOVEUP:
            self.rect.y -= self.velocity.y

        if self.controller.MOVEDOWN:
            self.rect.y += self.velocity.y

        self.check_boundaries()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 5)

    def check_boundaries(self):
        if self.rect.top <= self.settings.WINDOW_HEIGHT / 2:
            self.rect.top = self.settings.WINDOW_HEIGHT / 2

        if self.rect.bottom >= self.settings.WINDOW_HEIGHT:
            self.rect.bottom = self.settings.WINDOW_HEIGHT