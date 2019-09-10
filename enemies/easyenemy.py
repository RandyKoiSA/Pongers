from enemies.enemybase import EnemyBase
import pygame


class EasyEnemy(EnemyBase):

    def __init__(self, screen, settings, enemy_type, width=100, height=5, color=(0, 255, 0), velocity=(20, 20)):
        """ Initialize default values"""
        super().__init__(screen, settings, enemy_type, width, height, color, velocity)
        self.isMovingRight = True

        # Creating a rectangle for the enemy
        self.rect = pygame.Rect(((self.settings.WINDOW_WIDTH/2) - (self.enemy_width / 2), 20),
                                (self.enemy_width, self.enemy_height))

    def update(self):
        """ Update the easy enemy position and logic """
        if self.isMovingRight:
            self.rect.x += self.velocity.x
        else:
            self.rect.x -= self.velocity.x
        self.check_boundaries()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 5)

    def check_boundaries(self):
        """ Checks if the rectangle hit the edge of the screen """
        # When the enemy bar hits the left boundary, move right
        if self.rect.left < 0:
            self.rect.left = 0
            self.isMovingRight = True

        # When the enemy bar hits the right boundary, move left
        if self.rect.right > self.settings.WINDOW_WIDTH:
            self.rect.right = self.settings.WINDOW_WIDTH
            self.isMovingRight = False
