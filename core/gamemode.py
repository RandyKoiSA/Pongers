class Gamemode:
    """ Game mode defines the rules and checks whether the player has won or lost the game. """
    def __init__(self):
        """ Initialize default values """
        self.bHasWon = False
        self.game_over = False
        self.game_active = False

        self.remainingBalls = 0


