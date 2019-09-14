from custom.button import Button
from custom.text import Text
import pygame
from pygame.locals import *


class GameOverScreen:
    """ Gameover screen displays if you have won or lost. """
    def __init__(self, screen, settings, gamemode, screenmanager):
        """ Initialize properties """
        self.screen = screen

        self.settings = settings

        self.gamemode = gamemode

        self.screenmanager = screenmanager

        # Initializing the title screen
        self.title = Text(self.screen, self.settings, 'GAME OVER', (0, 0, 0), self.settings.BACKGROUND_COLOR,
                          self.settings.WINDOW_WIDTH / 2, 50)

        # Initializing the level selection button
        self.level_select_button = Button(self.screen, self.settings, 'Level Select', 200, 50,
                                          self.settings.WINDOW_WIDTH/2 - 100, self.settings.WINDOW_HEIGHT/2,
                                          (0, 0, 0), (255, 255, 255))

        # Initializing the main menu button
        self.main_menu_button = Button(self.screen, self.settings, 'Main Menu', 200, 50,
                                       self.settings.WINDOW_WIDTH / 2 - 100, self.settings.WINDOW_HEIGHT / 2 + 100,
                                       (0, 0, 0), (255, 255, 255))

    def run(self):
        """ The game-loop of the screen"""
        self.check_events()
        self.draw()

    def check_events(self):
        """ Checks players input and keybaord events """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_button_collision(mouse_x, mouse_y)

    def draw(self):
        """ Draw all the sprites inside of the game over screen"""
        self.title.draw()
        self.level_select_button.draw()
        self.main_menu_button.draw()

    def check_button_collision(self, mouse_x, mouse_y):
        """ Checks if any button has been clicked. """

        # Checks if the mouse clicked onto the level select button
        if self.level_select_button.rect.collidepoint(mouse_x, mouse_y):
            self.screenmanager.reset()
            self.screenmanager.bLevelSelect_Screen = True

        # Checks if the mouse clicked onto the main menu button
        elif self.main_menu_button.rect.collidepoint(mouse_x, mouse_y):
            self.screenmanager.reset()
