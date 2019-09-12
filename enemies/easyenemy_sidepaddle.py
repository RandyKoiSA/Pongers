from enemies.enemybase import EnemyBase


class EasyEnemySidePaddle(EnemyBase):
    """ Easy Enemy that spawns a vertical bars """
    def __init__(self, screen, settings, enemy_type, rightside, imagepath, width=5, height=100, color=(0, 255, 0),
                 velocity=(20, 20)):
        super().__init__(screen, settings, enemy_type, width, height, color, velocity, imagepath)
        self.isMovingUp = True

        # Creating a rectangle for the enemy
        self.rect = self.image.get_rect()
        if rightside:
            self.rect.x = 15
            self.rect.y = self.settings.WINDOW_HEIGHT / 4
        else:
            self.rect.x = self.settings.WINDOW_WIDTH - 25
            self.rect.y = self.settings.WINDOW_HEIGHT / 4

    def update(self):
        """ Update the enemy movements """
        if self.isMovingUp:
            self.rect.y -= self.velocity.y
        else:
            self.rect.y += self.velocity.y

        self.check_boundaries()

    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self.rect, 5)
        self.screen.blit(self.image, self.rect)

    def check_boundaries(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.isMovingUp = False

        if self.rect.bottom >= self.settings.WINDOW_HEIGHT/2:
            self.rect.bottom = self.settings.WINDOW_HEIGHT/2
            self.isMovingUp = True
