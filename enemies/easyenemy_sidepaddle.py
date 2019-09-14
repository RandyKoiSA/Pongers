from enemies.enemybase import EnemyBase


class EasyEnemySidePaddle(EnemyBase):
    """ Easy Enemy that spawns a vertical bars """
    def __init__(self, screen, settings, enemy_type, rightside, imagepath, width=5, height=100, color=(0, 255, 0),
                 velocity=(20, 20)):
        super().__init__(screen, settings, enemy_type, width, height, color, velocity, imagepath)
        self.isMovingUp = True
        self.topSide = rightside
        # Creating a rectangle for the enemy
        self.rect = self.image.get_rect()
        # Top enemy bar
        if self.topSide:
            self.rect.x = 3 * self.settings.WINDOW_WIDTH / 4
            self.rect.y = 10
        # Bottom Enemy bar
        else:
            self.rect.x = 3 * self.settings.WINDOW_WIDTH / 4
            self.rect.y = self.settings.WINDOW_HEIGHT - 20

    def update(self, balls):
        """ Update the enemy movements """
        # Find closest ball
        closest_ball = [self.settings.WINDOW_WIDTH/2, self.settings.WINDOW_HEIGHT/2]
        for ball in balls:
            if self.topSide:
                if ball.rect.y < closest_ball[1]:
                    closest_ball = ball.rect
            elif not self.topSide:
                if ball.rect.y > closest_ball[1]:
                    closest_ball = ball.rect

        # Calculation for if the bar is on top
        if self.rect.centerx >= closest_ball[0]:
            self.rect.x -= self.velocity.x
        elif self.rect.centerx <= closest_ball[0]:
            self.rect.x += self.velocity.x

        self.check_boundaries()

    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self.rect, 5)
        self.screen.blit(self.image, self.rect)

    def check_boundaries(self):
        if self.rect.left <= self.settings.WINDOW_WIDTH / 2:
            self.rect.left = self.settings.WINDOW_WIDTH / 2
            self.isMovingUp = False

        if self.rect.right >= self.settings.WINDOW_WIDTH:
            self.rect.right = self.settings.WINDOW_WIDTH
            self.isMovingUp = True
