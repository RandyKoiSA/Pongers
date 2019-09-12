import pygame
from custom.vector_point import Vector


class EnemyBase:
    """ Base for enemy ai """
    def __init__(self, screen, settings, enemy_type, width, height, color, velocity):
        """ Initialize the default values of the enemy """
        # Enemy's height size
        self.enemy_height = height

        # Enemy's width size
        self.enemy_width = width

        # Enemy's color box
        self.color = color

        # Enemy's speed when moving left and right
        self.velocity = Vector(velocity[0], velocity[1])

        # Screen, to draw onto
        self.screen = screen

        # Settings, to access the size of the window to figure out boundaries
        self.settings = settings

        # Enemy Type, to determine what type of enemy it is
        self.enemy_type = enemy_type
