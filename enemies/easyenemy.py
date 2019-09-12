from enemies.enemybase import EnemyBase


class EasyEnemy(EnemyBase):

    def __init__(self, screen, settings, enemy_type, imagepath, width=100,
                 height=5, color=(0, 255, 0), velocity=(20, 20)):
        """ Initialize default values"""
        super().__init__(screen, settings, enemy_type, width, height, color, velocity, imagepath)
        self.isMovingRight = True

        # Create the sprite
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.WINDOW_WIDTH/2 - (self.enemy_width / 2)
        self.rect.y = 20

    def update(self):
        """ Update the easy enemy position and logic """
        if self.isMovingRight:
            self.rect.x += self.velocity.x
        else:
            self.rect.x -= self.velocity.x
        self.check_boundaries()

    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self.rect, 5)
        self.screen.blit(self.image, self.rect)

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
