from balls.ballbase import BallBase
import pygame
import math


class BallTypeZero(BallBase):
    """ Ball Type Zero, will bounce wall the left and right walls. """
    def __init__(self, screen, settings, gamemode, ball_type, color, velocity, players, enemies, israndom, degree,
                 balls):
        """ Initialize properties """

        # Initialize parent class
        super().__init__(screen, settings, gamemode, ball_type, color,
                         velocity, players, enemies, israndom, degree, balls)

        # creating a rect object for the ball
        self.rect = pygame.Rect(((self.settings.WINDOW_WIDTH / 2) - (self.ball_width / 2),
                                 ((self.settings.WINDOW_HEIGHT / 2) - (self.ball_height / 2))),
                                (self.ball_width, self.ball_height))

    def update(self):
        """ Update the logic of the ball """

        # Calculate the amount of y position moved
        self.rect.centery += math.sin(self.radian) * self.velocity_y

        # Calculate the amount of x position moved
        self.rect.centerx += math.cos(self.radian) * self.velocity_x

        # Check if the ball hit the edges of the screen
        self.check_boundaries()

        # Check if the ball hit any of the sprites on the screen
        self.check_collision()

    def draw(self):
        """ Draws the ball onto the screen """
        pygame.draw.ellipse(self.screen, self.color, self.rect, 0)

    def check_boundaries(self):
        """ Checks if the ball has collided with the edges of the program screen. """

        # Ball has reached the top of the screen
        if self.rect.top < 0:
            self.velocity_y *= -1

        # Ball has reached the bottom of the screen
        if self.rect.bottom > self.settings.WINDOW_HEIGHT:
            self.velocity_y *= -1

        # Ball has reached the left or right side of the screen
        if self.rect.left - self.ball_width < 0 or self.rect.right + self.ball_width > self.settings.WINDOW_WIDTH:
            self.gamemode.remainingBalls -= 1
            self.balls.remove(self)
            self.gamemode.check_if_over()

    def check_collision(self):
        """ Checks if the ball has hit any of the sprites such as: players and enemies. """

        # See if it collide with player rect
        self.check_player_collision()

        # Scan if the ball collides with any of the enemies
        for enemy in self.enemies:
            if self.rect.colliderect(enemy):
                self.velocity_y *= -1

        # Checks if the ball past the top and bottom screen
        if self.rect.top < 0 or self.rect.bottom > self.settings.WINDOW_HEIGHT:
            self.gamemode.remainingBalls -= 1
            self.gamemode.check_if_over()

    def check_player_collision(self):
        """ Checks if the ball collides with the player"""

        for player in self.players:
            # Collision to main horizontal bar
            if player.player_type == 0:
                if self.rect.colliderect(player):
                    # Checks if the ball collides on top of the player bar
                    if self.velocity_x > 0:
                        if player.controller.MOVELEFT:
                            self.degree += self.velocity_x * 1.5 + 10
                        if player.controller.MOVERIGHT:
                            self.degree -= self.velocity_x * 1.5 + 10
                        self.update_radian()
                    else:
                        if player.controller.MOVELEFT:
                            self.degree += self.velocity_x * 1.5 - 10
                        if player.controller.MOVERIGHT:
                            self.degree -= self.velocity_x * 1.5 - 10
                    self.velocity_y *= -1

            # Collision to player's vertical side bars
            if player.player_type == 1:
                if self.rect.colliderect(player):
                    self.velocity_x *= -1
