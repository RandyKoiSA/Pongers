from custom.button import Button
from custom.text import Text
import pygame
from pygame.locals import *

class GameOverScreen():
    """ Gameover screen displays if you have won or lost. """
    def __init__(self, screen, settings, gamemode, controller, screenmanager):
        """ Initialize properties """
        self.screen = screen

        self.settings = settings

        self.gamemode = gamemode

        self.screenmanager = screenmanager

        self.title = Text(self.screen, self.settings, 'GAME OVER', (0, 0, 0), self.settings.BACKGROUND_COLOR,
                          self.settings.WINDOW_WIDTH / 2, 50)

        self.level_select_button = Button(self.screen, self.settings, 'Level Select', 200, 50,
                                          self.settings.WINDOW_WIDTH/2 - 100, self.settings.WINDOW_HEIGHT/2,
                                          (0, 0, 0), (255, 255, 255))

        self.main_menu_button = Button(self.screen, self.settings, 'Main Menu', 200, 50,
                                       self.settings.WINDOW_WIDTH / 2 - 100, self.settings.WINDOW_HEIGHT / 2 + 100,
                                       (0, 0, 0), (255, 255, 255))

    def run(self):
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
        self.title.draw()
        self.level_select_button.draw()
        self.main_menu_button.draw()

    def check_button_collision(self, mouse_x, mouse_y):
        """ Checks if any button has been clicked. """
        print('mouse event pressed down')
        if self.level_select_button.rect.collidepoint(mouse_x, mouse_y):
            self.screenmanager.reset()
            self.screenmanager.bLevelSelect_Screen = True
        if self.main_menu_button.rect.collidepoint(mouse_x, mouse_y):
            self.screenmanager.reset()
