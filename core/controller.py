class Controller:
    """ Controller, stores all the inputs the owner presses """
    def __init__(self):
        # Initialize default values
        self.MOVELEFT = False
        self.MOVERIGHT = False
        self.MOVEUP = False
        self.MOVEDOWN = False

    def reset_controller(self):
        # Reset the controller before start of game
        self.MOVELEFT = False
        self.MOVERIGHT = False
        self.MOVEUP = False
        self.MOVEDOWN = False
