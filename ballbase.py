import pygame
import math
import random
from custom.vector_point import Vector


class BallBase:
    """ Ball Base that has basic/general attribute for what a ball requires"""
    def __init__(self, screen, settings, gamemode, players, enemies):
        """ Initialize the default values of a ball """
        # define the value of PI
        self.PI = 3.14

        # reference to screen, used to display the ball
        self.screen = screen

        # reference to settings, used to retrieve the screen size
        self.settings = settings

        # reference to gamemode, used to see if the game is over
        self.gamemode = gamemode

        # reference to player, used to interaction with the player
        self.players = players

        # reference to enemy, used to interact with the enemy
        self.enemies = enemies

        # ball's width size : EDITABLE
        self.ball_width = 25

        # ball's height size : EDITABLE
        self.ball_height = 25

        # ball's velocity speed : EDITABLE
        self.velocity = Vector(15, 15)

        # ball's color : EDITABLE
        self.color = (125, 125, 125)

        # ball's direction angle by degree : EDITABLE
        self.degree = 10

        # spawn ball at random direction : EDITABLE
        self.bRandomDirection = True

        if self.bRandomDirection:
            self.degree = random.randint(0, 360)

        # creating a rect object for the ball
        self.rect = pygame.Rect(((self.settings.WINDOW_WIDTH / 2) - (self.ball_width / 2),
                                 ((self.settings.WINDOW_HEIGHT / 2) - (self.ball_height / 2))),
                                (self.ball_width, self.ball_height))

        # radian to find the angle the ball will go. Formula radian = degree * (3.14/180)
        self.radian = self.degree * (self.PI/180) * -1

    def update(self):
        self.rect.centery += math.sin(self.radian) * self.velocity.y
        self.rect.centerx += math.cos(self.radian) * self.velocity.x
        self.check_boundaries()
        self.check_collision()

    def draw(self):
        pygame.draw.ellipse(self.screen, self.color, self.rect, 0)

    def check_boundaries(self):
        if self.rect.left < 0:
            self.velocity.x *= -1

        if self.rect.right > self.settings.WINDOW_WIDTH:
            self.velocity.x *= -1

    def check_collision(self):
        """ Detects if the ball has hit the """
        # See if it collide with player rect
        for player in self.players:
            if self.rect.colliderect(player):
                # Checks if the ball collides on top of the player bar
                if self.velocity.x > 0:
                    if player.controller.MOVELEFT:
                        self.degree += self.velocity.x * 1.5 + 10
                    if player.controller.MOVERIGHT:
                        self.degree -= self.velocity.x * 1.5 + 10
                    self.update_radian()
                else:
                    if player.controller.MOVELEFT:
                        self.degree += self.velocity.x * 1.5 - 10
                    if player.controller.MOVERIGHT:
                        self.degree -= self.velocity.x * 1.5 - 10
                self.velocity.y *= -1

        # See if the ball collides with the enemy var
        for enemy in self.enemies:
            if self.rect.colliderect(enemy):
                self.velocity.y *= -1

        if self.rect.top < 0 or self.rect.bottom > self.settings.WINDOW_HEIGHT:
            self.gamemode.game_over = True

    def update_radian(self):
        self.radian = self.degree * (self.PI/180) * -1
