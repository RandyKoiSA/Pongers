from custom.button import Button


class LevelButton(Button):
    """ Level Button will hold the descriptions of the level. """
    def __init__(self, screen, settings, levelName, playergroup, enemygroup, ballgroup, rules,
                 button_width=100, button_height=100, position_x=0, position_y=0, button_color=(0, 255, 0),
                 text_color=(255, 255, 255)):
        super().__init__(screen, settings, levelName, button_width, button_height, position_x, position_y, button_color,
                         text_color)
        """ Initiate properties """
        self.playerGroup = playergroup
        self.enemyGroup = enemygroup
        self.ballGroup = ballgroup
        self.rules = rules

    def gather_information(self):
        for player in self.playerGroup:
            print(player)