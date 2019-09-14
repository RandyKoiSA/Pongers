

class Gamemode:
    """ Game mode defines the rules and checks whether the player has won or lost the game. """
    def __init__(self):
        """ Initialize default values """
        # Checks if the player wins in the end
        self.bHasWon = False

        # Checks if the game is over to trigger the gameover screen
        self.game_over = False

        # Checks if the game is active to trigger the main menu / level selection screen
        self.game_active = False

        # Stores the amount of points the player has gained during the game
        self.player_points = 0

        # Stores the amount of points the enemy has gained during the game
        self.enemy_points = 0

        # Stores the amount of balls left that should be played during the game.
        self.remainingBalls = 0

    def check_if_over(self):
        """ Checks if the game has finished, leading to the game over screen"""
        if self.remainingBalls == 0:
            self.check_if_won()
            self.game_over = True

    def check_if_won(self):
        """ Checks if the player has won based on the points acquired """
        if self.player_points > self.enemy_points:
            self.bHasWon = True
        else:
            self.bHasWon = False

    def add_gamemode_rules(self, rules):
        """ Set the game rule before the game starts """
        self.remainingBalls = rules['remainingballs']

    def reset_game(self):
        """ Resets the game after the game over screen """
        self.bHasWon = False
        self.game_over = False
        self.game_active = False
        self.player_points = 0
        self.enemy_points = 0
        self.remainingBalls = 0
