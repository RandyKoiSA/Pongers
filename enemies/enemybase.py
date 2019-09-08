import pygame
from custom.vector_point import Vector


class EnemyBase:
    """ Base for enemy ai """
    def __init__(self, screen, settings):
        """ Initialize the default values of the enemy """
        # Enemy's height size
        self.enemy_height = 5

        # Enemy's width size
        self.enemy_width = 100

        # Enemy's color box
        self.color = (255, 0, 0)

        # Enemy's speed when moving left and right
        self.velocity = Vector(20, 0)

        # Screen, to draw onto
        self.screen = screen

        # Settings, to access the size of the window to figure out boundaries
        self.settings = settings

        # Creating a rectangle for the enemy
        self.rect = pygame.Rect(((self.settings.WINDOW_WIDTH/2) - (self.enemy_width / 2), 20),
                                (self.enemy_width, self.enemy_height))

        self.movingright = False

    def update(self):
        print('This is a base update in enemybase.py')

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 5)
