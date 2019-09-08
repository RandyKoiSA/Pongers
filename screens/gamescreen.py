from player import Player
from enemies.easyenemy import EasyEnemy
from ballbase import BallBase
from core import gamefunctions as gf
from pygame.sprite import Group


class GameScreen:
    """ Game screen that display the actually game play of pong"""
    def __init__(self, screen, settings, gamemode, controller, screenmanager):
        """ Initialize properties """
        self.screen = screen
        self.settings = settings
        self.controller = controller
        self.gamemode = gamemode

        # Initialize the player sprite
        self.players = []

        # Initialize the enemy sprite
        self.enemies = []

        # Initialize the ball sprite
        self.balls = []

    def run(self):
        """ Run all the function needed to update and display the screen """
        self.check_events()
        self.update()
        self.draw()

    def check_events(self):
        """ use general event, this can be changed if we want to have different event for each screen """
        gf.check_events(self.controller)

    def update(self):
        """ Update all the sprites in the game screen """
        for player in self.players:
            player.update()
        for enemy in self.enemies:
            enemy.update()
        for ball in self.balls:
            ball.update()

    def draw(self):
        """ Draw all the sprites in the game screen """
        for player in self.players:
            player.draw()
        for enemy in self.enemies:
            enemy.draw()
        for ball in self.balls:
            ball.draw()

    def reset_game(self):
        """ Temporarily in place, but this resets the ball before the game starts"""
        self.ball = BallBase(self.screen, self.settings, self.gamemode, self.players, self.enemies)

    def create_sprites(self, players, enemies, balls):
        for player in players:
            new_player = Player(self.screen, self.controller, self.settings,
                                player[0], player[1], player[2], player[3])
            self.players.append(new_player)
        for enemy in enemies:
            new_enemy = EasyEnemy(self.screen, self.settings)
            self.enemies.append(new_enemy)
        for ball in balls:
            new_ball = BallBase(self.screen, self.settings, self.gamemode, self.players, self.enemies)
            self.balls.append(new_ball)