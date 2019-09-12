from screens import gamescreen as gs
from screens import menuscreen as ms
from screens import levelselectscreen as ls


class ScreenManager:
    """ Manages the screen that is being displayed onto the main screen.
    This will determine what screen needs to be displayed, updates the necessary stuff inside the screen and draws it
    before displaying onto the main screen. """

    def __init__(self, screen, settings, gamemode, controller):
        """ Initialize properties"""
        self.screen = screen
        self.settings = settings
        self.gamemode = gamemode
        self.controller = controller

        # Initialize all the screens here
        self.game_screen = gs.GameScreen(self.screen, self.settings, self.gamemode, self.controller)
        self.mainmenu_screen = ms.MainMenuScreen(self.screen, self.settings, self.gamemode, self.controller, self)
        self.level_select_screen = ls.LevelSelectScreen(self.screen, self.settings, self.gamemode, self)

        # To trigger certain screen
        self.bLevelSelect_Screen = False

    def run(self):
        if self.gamemode.game_over:
            self.gamemode.game_active = False
            self.gamemode.game_over = False
            self.game_screen = gs.GameScreen(self.screen, self.settings, self.gamemode, self.controller)
            self.controller.reset_controller()

        if self.gamemode.game_active:
            self.game_screen.run()
        else:
            if self.bLevelSelect_Screen:
                self.level_select_screen.run()
            else:
                self.mainmenu_screen.run()
