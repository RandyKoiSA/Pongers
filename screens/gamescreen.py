from players.player import Player
from enemies.easyenemy import EasyEnemy
from balls.ball_type_one import BallTypeOne
from balls.ball_type_zero import BallTypeZero
from core import gamefunctions as gf
from players.side_player import SidePlayer
from custom.text import Text
from enemies.easyenemy_sidepaddle import EasyEnemySidePaddle as EnemyTypeOne
import pygame


class GameScreen:
    """ Game screen that display the actually game play of pong"""
    def __init__(self, screen, settings, gamemode, controller):
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

        # Initialize net sprite
        self.netimage = pygame.image.load('imgs/vertical-net.png')
        self.netrect = self.netimage.get_rect()
        self.netrect.x = self.settings.WINDOW_WIDTH/2 - 5

        # Initialize player score text
        self.player_score = Text(self.screen, self.settings, str(self.gamemode.player_points),
                                      text_color=(0, 0, 0), background_color=self.settings.BACKGROUND_COLOR,
                                      pos_x=self.settings.WINDOW_WIDTH/2 - 25, pos_y=self.settings.WINDOW_HEIGHT/2)

        # Initialize enemy score text
        self.enemy_score = Text(self.screen, self.settings, str(self.gamemode.enemy_points),
                                text_color=(0, 0, 0), background_color=self.settings.BACKGROUND_COLOR,
                                pos_x=self.settings.WINDOW_WIDTH/2 + 25, pos_y=self.settings.WINDOW_HEIGHT/2)

        # Background sound
        pygame.mixer.music.load('wav/backgroundmusic.wav')
        pygame.mixer.music.play(-1, 0.0)

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
        # Update the player score
        self.player_score.message = str(self.gamemode.player_points)
        self.player_score.update_message()

        self.enemy_score.message = str(self.gamemode.enemy_points)
        self.enemy_score.update_message()

        # Update all the player sprites
        for player in self.players:
            player.update()
        # Update all enemy sprites
        for enemy in self.enemies:
            if enemy.enemy_type is 0:
                enemy.update(self.balls)
            elif enemy.enemy_type is 1:
                enemy.update(self.balls)
            else:
                enemy.update()
        # Update all ball sprites
        for ball in self.balls:
            ball.update()

    def draw(self):
        """ Draw all the sprites in the game screen """
        # Draw net
        self.screen.blit(self.netimage, self.netrect)

        # Draw player score
        self.player_score.draw()

        # Draw enemy score
        self.enemy_score.draw()

        # Draw all player sprites in player group
        for player in self.players:
            player.draw()
        # Draw all enemy sprites in enemy group
        for enemy in self.enemies:
            enemy.draw()
        # Draw all ball sprites in ball group
        for ball in self.balls:
            ball.draw()

    def create_sprites(self, players, enemies, balls):
        """ Loads in all the player, enemies, and balls into the game."""
        # Create the players in the list
        self.create_players(players)
        # Create the enemies in the list
        self.create_enemies(enemies)
        # Create the balls in the list
        self.create_balls(balls)

    def create_players(self, players):
        # Add all the new players into the game's players group
        for player in players:
            print(player['width'])
            if player['player_type'] == 0:
                new_player = Player(self.screen, self.controller, self.settings, player['player_type'],
                                    player['imagepath'])
                self.players.append(new_player)
            elif player['player_type'] == 1:
                new_player = SidePlayer(self.screen, self.controller, self.settings, player['rightside'],
                                        player['imagepath'], player['player_type'])
                self.players.append(new_player)

    def create_enemies(self, enemies):
        # Add all new enemies into the game's enemy group
        for enemy in enemies:
            if enemy['enemy_type'] == 0:
                new_enemy = EasyEnemy(self.screen, self.settings, enemy['enemy_type'], enemy['imagepath'],
                                      enemy['width'], enemy['height'], enemy['color'], enemy['velocity'])
                self.enemies.append(new_enemy)
            if enemy['enemy_type'] == 1:
                new_enemy = EnemyTypeOne(self.screen, self.settings, enemy['enemy_type'], enemy['rightside'],
                                         enemy['imagepath'], enemy['width'], enemy['height'], enemy['color'],
                                         enemy['velocity'])
                self.enemies.append(new_enemy)

    def create_balls(self, balls):
        # Add all new balls into the game's ball group
        for ball in balls:
            if ball['ball_type'] == 0:
                new_ball = BallTypeZero(self.screen, self.settings, self.gamemode,
                                        ball['ball_type'], ball['color'], ball['velocity'], self.players, self.enemies,
                                        ball['isRandom'], ball['degree'], self.balls)
                self.balls.append(new_ball)
            if ball['ball_type'] == 1:
                new_ball = BallTypeOne(self.screen, self.settings, self.gamemode, ball['ball_type'], ball['color'],
                                       ball['velocity'], self.players, self.enemies, ball['isRandom'],
                                       ball['degree'], self.balls)
                self.balls.append(new_ball)
