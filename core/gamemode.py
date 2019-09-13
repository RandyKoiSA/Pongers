from balls.ball_type_one import BallTypeOne

class Gamemode:
    """ Game mode defines the rules and checks whether the player has won or lost the game. """
    def __init__(self):
        """ Initialize default values """
        self.bHasWon = False
        self.game_over = False
        self.game_active = False

        self.player_points = 0
        self.enemy_points = 0

        self.remainingBalls = 0

    def check_if_over(self):
        if self.remainingBalls == 0:
            self.check_if_won()
            # self.show_gameover_screen()
            self.game_over = True


    def check_if_won(self):
        if self.player_points > self.enemy_points:
            self.bHasWon = True
        else:
            self.bHasWon = False

    def add_gamemode_rules(self, rules):
        self.remainingBalls = rules['remainingballs']

    def reset_game(self):
        self.bHasWon = False
        self.game_over = False
        self.game_active = False
        self.player_points = 0
        self.enemy_points = 0
        self.remainingBalls = 0

