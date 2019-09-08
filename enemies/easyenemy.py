from enemies.enemybase import EnemyBase

class EasyEnemy(EnemyBase):
    def __init__(self, screen, settings):
        """ Initialize default values"""
        super().__init__(screen, settings)

    def update(self):
        """ Update the easy enemy position and logic """
        if self.movingright:
            self.rect.x += self.velocity.x
        else:
            self.rect.x -= self.velocity.x
        self.check_boundaries()

    def check_boundaries(self):
        """ Checks if the rectangle hit the edge of the screen """
        # When the enemy bar hits the left boundary, move right
        if self.rect.left < 0:
            self.rect.left = 0
            self.movingright = True

        # When the enemy bar hits the right boundary, move left
        if self.rect.right > self.settings.WINDOW_WIDTH:
            self.rect.right = self.settings.WINDOW_WIDTH
            self.movingright = False