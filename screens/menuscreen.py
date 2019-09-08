from custom import button
from custom import text
import pygame
import sys
from pygame.locals import *


class MainMenuScreen:
    """ Main Menu Screen, this will display buttons for the user to interact with before playing """
    def __init__(self, screen, settings, gamemode, controller, screenmanager):

        self.screen = screen

        self.settings = settings

        self.gamemode = gamemode

        self.controller = controller

        self.screenmanager = screenmanager

        self.play_button = button.Button(self.screen,
                                         self.settings,
                                         button_height=50,
                                         button_width=100,
                                         position_x=self.settings.WINDOW_WIDTH/2 - 50,
                                         position_y=self.settings.WINDOW_HEIGHT/2 - 25,
                                         message='Play',
                                         text_color=(255, 255, 255),
                                         button_color=(0, 0, 0))

        self.quit_button = button.Button(self.screen,
                                         self.settings,
                                         button_height=50,
                                         button_width=100,
                                         position_x=self.settings.WINDOW_WIDTH/2 - 50,
                                         position_y=self.settings.WINDOW_HEIGHT/2 + 50,
                                         message='Quit',
                                         text_color=(255, 255, 255),
                                         button_color=(0, 0, 0))

        self.title = text.Text(self.screen, self.settings, message='PONG BY RANDY LE',
                               pos_x=self.settings.WINDOW_WIDTH/2, pos_y=50,
                               background_color=self.settings.BACKGROUND_COLOR)

    def run(self):
        self.check_events()
        # self.update()
        self.draw()

    def check_events(self):
        """ Checks plays input and keyboard events """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.gamemode.game_active = True
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_button_collision(mouse_x, mouse_y)

    # def update(self):

    def draw(self):
        self.play_button.draw()
        self.quit_button.draw()
        self.title.draw()

    def check_button_collision(self, pos_x, pos_y):
        """ checks if any button has been clicked """
        # checks if the mouse clicked over the play button
        if self.play_button.rect.collidepoint(pos_x, pos_y):
            self.screenmanager.bMain_Screen = False
            self.screenmanager.bLevelSelect_Screen = True

        # checks if the mouse clicked over the quit button
        if self.quit_button.rect.collidepoint(pos_x, pos_y):
            pygame.quit()
            sys.exit()