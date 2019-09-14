from balls.ballbase import BallBase
import pygame
import math


class BallTypeOne(BallBase):
    """ Ball Type One, a ball that no wall collision """

    def __init__(self, screen, settings, gamemode, ball_type, color, velocity, players, enemies, israndom, degree,
                 balls):
        """ Initialize properties """

        # Initialize the parent class
        super().__init__(screen, settings, gamemode, ball_type, color, velocity, players,
                         enemies, israndom, degree, balls)

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

        # Check if the ball hit any of the sprites
        self.check_collision()

    def draw(self):
        """ Draw the ball onto the screen """

        # Draw the ball onto the screen
        pygame.draw.ellipse(self.screen, self.color, self.rect, 0)

    def check_boundaries(self):
        """ Checks if the ball reached the edges of the program """

        # Checks if the ball passed the top or bottom screen
        if self.rect.bottom < 0 or self.rect.top > self.settings.WINDOW_HEIGHT:
            self.check_if_player_scored()
            self.gamemode.remainingBalls -= 1
            self.balls.remove(self)
            self.gamemode.check_if_over()
            if self.gamemode.game_over:
                if self.gamemode.bHasWon:
                    self.settings.win_game_sound.play()
                else:
                    self.settings.lose_game_sound.play()

            self.check_if_remaining_balls()

        # Checks if the ball passed the left or right screen
        if self.rect.right < 0 or self.rect.left > self.settings.WINDOW_WIDTH:
            self.check_if_player_scored()
            self.gamemode.remainingBalls -= 1
            self.balls.remove(self)
            self.gamemode.check_if_over()
            self.check_if_remaining_balls()

    def check_collision(self):
        """ Detects if the ball has hit the """

        # Checks if the ball collided with any of the players
        self.check_player_collision()

        # Checks if the ball has collided with any of the enemies
        for enemy in self.enemies:
            if self.rect.colliderect(enemy):
                if enemy.enemy_type == 0:
                    self.velocity_x *= -1
                if enemy.enemy_type == 1:
                    self.velocity_y *= -1

                self.ball_sound.play()

    def check_player_collision(self):
        """ Checks if the ball collides with the player"""

        # Scans through all the player
        for player in self.players:

            # Checks if the player bar is the main paddle
            if player.player_type == 0:
                # True, if the ball has collided with the player bar
                if self.rect.colliderect(player):
                    # Calculate the new angle based on the player's bar movement.
                    if self.velocity_y > 0:
                        if player.controller.MOVEUP:
                            self.degree -= self.velocity_y * 1.5 + 10
                        if player.controller.MOVEDOWN:
                            self.degree += self.velocity_y * 1.5 + 10
                        self.update_radian()
                    else:
                        if player.controller.MOVEUP:
                            self.degree -= self.velocity_y * 1.5 - 10
                        if player.controller.MOVERIGHT:
                            self.degree += self.velocity_y * 1.5 - 10
                    self.velocity_x *= -1

                    self.ball_sound.play()

            # Checks if the player bar is the side paddle
            if player.player_type == 1:
                if self.rect.colliderect(player):
                    self.velocity_y *= -1

                    self.ball_sound.play()

    def check_if_player_scored(self):
        """ Called after ball has passed the screen, checks if the player has scored. """
        if self.rect.centerx > self.settings.WINDOW_WIDTH / 2:
            self.gamemode.player_points += 1
            self.settings.win_point_sound.play()
        else:
            self.gamemode.enemy_points += 1
            self.settings.lose_point_sound.play()

    def check_if_remaining_balls(self):
        """ Checks if there is any more balls left to be spawned before ending game. """
        if self.gamemode.remainingBalls > 0 and len(self.balls) is 0:
            self.balls.append(BallTypeOne(self.screen, self.settings, self.gamemode, self.ball_type, self.color,
                                          (self.velocity_x, self.velocity_y),
                                          self.players, self.enemies, True, 0, self.balls))
