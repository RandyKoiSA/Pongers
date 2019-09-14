from enemies.enemybase import EnemyBase


class EasyEnemy(EnemyBase):

    def __init__(self, screen, settings, enemy_type, imagepath, width=100,
                 height=5, color=(0, 255, 0), velocity=(20, 20)):
        """ Initialize default values"""

        # Initialize super parent
        super().__init__(screen, settings, enemy_type, width, height, color, velocity, imagepath)

        # Create the sprite
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.WINDOW_WIDTH - 20
        self.rect.y = self.settings.WINDOW_HEIGHT - 20

    def update(self, balls):
        """ Update the easy enemy position and logic """

        # Find closest ball near the bar
        closest_ball = [self.settings.WINDOW_WIDTH/2, 0]

        # Find the closest ball
        for ball in balls:
            if ball.rect.x > int(closest_ball[0]):
                closest_ball = ball.rect

        # Checks if the ball is on the enemy side
        if closest_ball[0] > self.settings.WINDOW_WIDTH/2:
            #
            if self.rect.top > closest_ball[1]:
                self.rect.y -= self.velocity.y
            elif self.rect.bottom < closest_ball[1]:
                self.rect.y += self.velocity.y

        self.check_boundaries()

    def draw(self):
        """ Draw the enemy bar onto the given screen. """
        self.screen.blit(self.image, self.rect)

    def check_boundaries(self):
        """ Checks if the rectangle hit the edge of the screen """
        # When the enemy bar hits the left boundary, move right
        if self.rect.top < 0:
            self.rect.top = 0

        # When the enemy bar hits the right boundary, move left
        if self.rect.bottom > self.settings.WINDOW_HEIGHT:
            self.rect.bottom = self.settings.WINDOW_HEIGHT
