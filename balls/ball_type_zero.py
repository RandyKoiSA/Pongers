from balls.ballbase import BallBase
import pygame
import math

class Ball_Type_Zero(BallBase):
    """ Ball Type Zero, will bounce wall the left and right walls. """
    def __init__(self, screen, settings, gamemode, ball_type, color, velocity, players, enemies, isRandom, degree):
        """ Initialize properties """
        super().__init__(screen, settings, gamemode, ball_type, color, velocity, players, enemies, isRandom, degree)

        # creating a rect object for the ball
        self.rect = pygame.Rect(((self.settings.WINDOW_WIDTH / 2) - (self.ball_width / 2),
                                 ((self.settings.WINDOW_HEIGHT / 2) - (self.ball_height / 2))),
                                (self.ball_width, self.ball_height))

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
        self.check_player_collision()

        # Scan if the ball collides with any of the enemies
        for enemy in self.enemies:
            if self.rect.colliderect(enemy):
                self.velocity.y *= -1

        # Checks if the ball past the top and bottom screen
        if self.rect.top < 0 or self.rect.bottom > self.settings.WINDOW_HEIGHT:
            self.gamemode.game_over = True

    def check_player_collision(self):
        """ Checks if the ball collides with the player"""
        for player in self.players:
            # Collision to main horizontal bar
            if player.player_type == 0:
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
            # Collision to player's vertical side bars
            if player.player_type == 1:
                if self.rect.colliderect(player):
                    self.velocity.x *= -1