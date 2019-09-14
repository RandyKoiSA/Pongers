from custom.vector_point import Vector
from players.player_base import PlayerBase


class SidePlayer(PlayerBase):
    """ Side player bar that holds all the attribute and details of what the player has. """
    def __init__(self, screen, controller, settings, rightside, imagepath, player_type, width=5, height=100,
                 color=(0, 0, 0), velocity=Vector(20, 20)):
        """ Initialize properties """

        # Initializing super class properties
        super().__init__(screen, controller, settings, player_type, width, height, color, velocity, imagepath)

        # Checks if the player side bar will be placed on the top or bottom
        self.topside = rightside

        # Initializing rectangle for the player side bar
        self.rect = self.image.get_rect()

        # Place the player side bar on the top
        if not self.topside:
            self.rect.x = self.settings.WINDOW_WIDTH / 4
            self.rect.y = 30
        # Place the player side bar on the bottom
        else:
            self.rect.x = self.settings.WINDOW_WIDTH / 4
            self.rect.y = self.settings.WINDOW_HEIGHT - 40

    def update(self):
        """ Update the player based on controller input """
        if self.controller.MOVELEFT:
            self.rect.x -= self.velocity.x

        if self.controller.MOVERIGHT:
            self.rect.x += self.velocity.x

        self.check_boundaries()

    def draw(self):
        """ Draw the player side bar onto the given screen """
        self.screen.blit(self.image, self.rect)

    def check_boundaries(self):
        """ Check if the player has gone over given out of bound area"""
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right >= self.settings.WINDOW_WIDTH / 2:
            self.rect.right = self.settings.WINDOW_WIDTH / 2
