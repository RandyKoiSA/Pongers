from custom.button import Button


class LevelButton(Button):
    """ Level Button will hold the descriptions of the level. """

    def __init__(self, screen, settings, levelname, playergroup, enemygroup, ballgroup, rules,
                 button_width=100, button_height=100, position_x=0, position_y=0, button_color=(0, 0, 0),
                 text_color=(255, 255, 255)):
        """ Initializing properties """

        # Initialize parent class
        super().__init__(screen, settings, levelname, button_width, button_height, position_x, position_y, button_color,
                         text_color)

        # playerGroup, is a dictionary of all the players in the level
        self.playerGroup = playergroup

        # enemyGroup, is a dictionary of all the enemies in the level
        self.enemyGroup = enemygroup

        # ballGroup, is a dictionary of all the balls in the level
        self.ballGroup = ballgroup

        # rules, a dictionary that has all the rules to set up the game
        self.rules = rules

    def gather_information(self):
        """ Read through all the players information """
        for player in self.playerGroup:
            print(player)
