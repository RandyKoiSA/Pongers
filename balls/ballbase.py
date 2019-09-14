import random
import pygame


class BallBase:
    """ Ball Base that has basic/general attribute for what a ball requires"""
    def __init__(self, screen, settings, gamemode, ball_type, color, velocity,
                 players, enemies, israndom, degree, balls):
        """ Initialize the default values of a ball """
        # ball type, the type of ball it is
        self.ball_type = ball_type

        # define the value of PI
        self.PI = 3.14

        # reference to screen, used to display the ball
        self.screen = screen

        # reference to settings, used to retrieve the screen size
        self.settings = settings

        # reference to gamemode, used to see if the game is over
        self.gamemode = gamemode

        # reference to player, used to interaction with the player
        self.players = players

        # reference to enemy, used to interact with the enemy
        self.enemies = enemies

        # ball's width size : EDITABLE
        self.ball_width = 25

        # ball's height size : EDITABLE
        self.ball_height = 25

        # ball's velocity speed : EDITABLE
        self.velocity_x = velocity[0]
        self.velocity_y = velocity[1]

        # ball's color : EDITABLE
        self.color = color

        # ball's direction angle by degree : EDITABLE
        self.degree = degree

        # spawn ball at random direction : EDITABLE
        self.bRandomDirection = israndom

        # get the list of balls that are currently in play
        self.balls = balls

        # ball sound
        self.ball_sound = pygame.mixer.Sound('wav/ballsound.wav')

        if self.bRandomDirection:
            self.degree = random.randint(0, 360)
            value_speed = random.randint(10, 20)
            self.velocity_x = value_speed
            self.velocity_y = value_speed

        # radian to find the angle the ball will go. Formula radian = degree * (3.14/180)
        self.radian = self.degree * (self.PI/180) * -1

    def update_radian(self):
        self.radian = self.degree * (self.PI/180) * -1
