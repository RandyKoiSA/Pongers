import json
import pygame
import sys
from pygame.locals import *
from custom import text
from custom.level_button import LevelButton


class LevelSelectScreen:
    """ Level Select Screen display the levels that can be played by the player """
    def __init__(self, screen, settings, gamemode, screenmanager):
        """ Initialize properties """
        self.screen = screen
        self.settings = settings
        self.gamemode = gamemode
        self.screenmanager = screenmanager

        # Initializing the title text of the screen
        self.title = text.Text(self.screen, self.settings, 'Level Select', pos_x=settings.WINDOW_WIDTH/2, pos_y=50,
                               background_color=settings.BACKGROUND_COLOR)

        # Initializing a list that stores all the existing levels
        self.levels = []

        # Grabs all the levels in the JSON file: 'levels_file.json'
        self.obtain_levels()

        # Arrange the level buttons in a orderly fashion
        self.arrange_level()
        print(self.levels)

    def run(self):
        """ Screen's game-loop method"""
        self.check_events()
        # self.update()
        self.draw()

    def check_events(self):
        """ Checks for any player's input"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_button_collision(mouse_x, mouse_y)

    def draw(self):
        """ Draws all the sprites in the level selection screen """
        self.title.draw()

        # Draw all the level in the levels list
        for level in self.levels:
            level.draw()

    def obtain_levels(self):
        """ Extracts all the information from the JSON file and send them to the appropriate parameter"""
        filename = 'levels_file.json'
        with open(filename, 'r') as read_file:
            data = json.load(read_file)
            for x in data:
                self.levels.append(LevelButton(self.screen, self.screen, data[x]['levelName'],
                                               data[x]["playerGroup"], data[x]["enemyGroup"], data[x]["ballGroup"],
                                               data[x]["gamemode"]))

    def arrange_level(self):
        """ Arranges all the levels found in an orderly fashion """
        counter = 0
        column = 0
        print(str(len(self.levels)) + ' level(s)')
        for level in self.levels:
            level.rect.x = counter * 120 + 10
            level.rect.y = column * 150 + 150
            level.update_position()
            counter += 1
            if counter % 4 == 0:
                column += 1
                counter = 0

    def check_button_collision(self, mouse_x, mouse_y):
        """ Checks if the mouse has clicked onto any of the level buttons """
        for level in self.levels:
            if level.rect.collidepoint(mouse_x, mouse_y):
                self.gamemode.reset_game()
                self.gamemode.game_active = True
                self.screenmanager.bLevelSelect_Screen = False
                self.gamemode.add_gamemode_rules(rules=level.rules)
                self.screenmanager.game_screen.create_sprites(level.playerGroup, level.enemyGroup, level.ballGroup)
