from enemies.enemybase import EnemyBase


class EasyEnemySidePaddle(EnemyBase):
    """ Easy Enemy that spawns a vertical bars """
    def __init__(self, screen, settings, enemy_type, rightside, imagepath, width=5, height=100, color=(0, 255, 0),
                 velocity=(20, 20)):
        """ Initializing properties """

        # Initializing super parent properties
        super().__init__(screen, settings, enemy_type, width, height, color, velocity, imagepath)

        # Checks if the enemy bar is moving up
        self.isMovingUp = True

        # Decides whether the enemy bar spawns on top or bottom
        self.topSide = rightside

        # Creating a rectangle for the enemy
        self.rect = self.image.get_rect()

        # Top enemy bar
        if self.topSide:
            self.rect.x = 3 * self.settings.WINDOW_WIDTH / 4
            self.rect.y = 30
        # Bottom Enemy bar
        else:
            self.rect.x = 3 * self.settings.WINDOW_WIDTH / 4
            self.rect.y = self.settings.WINDOW_HEIGHT - 40

    def update(self, balls):
        """ Update the enemy movements """

        # Find closest ball
        closest_ball = [self.settings.WINDOW_WIDTH/2, self.settings.WINDOW_HEIGHT/2]

        # Scan through all the list of balls to find the closest to the enemy bar
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

        # Checks if the enemy bar gone out of bound
        self.check_boundaries()

    def draw(self):
        """ Draws the enemy bar onto the given screen """
        self.screen.blit(self.image, self.rect)

    def check_boundaries(self):
        """ Checks if the enemy bar has gone out of bound """
        # Checks if the enemy bar has gone of the net
        if self.rect.left <= self.settings.WINDOW_WIDTH / 2:
            self.rect.left = self.settings.WINDOW_WIDTH / 2
            self.isMovingUp = False

        # Checks if the enemy bar has gone out of bound to the right
        if self.rect.right >= self.settings.WINDOW_WIDTH:
            self.rect.right = self.settings.WINDOW_WIDTH
            self.isMovingUp = True
