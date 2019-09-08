import pygame.ftfont


class Button:
    """ Creation of a button for user interface """

    def __init__(self, screen, settings,
                 message='', button_width=200, button_height=50,
                 position_x=300, position_y=300,
                 button_color=(0, 255, 0), text_color=(255, 255, 255)):
        """ Initialize button attributes """
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button
        self.message = str(message)
        self.width = button_width
        self.height = button_height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(position_x, position_y, self.width, self.height)

        # The button message needs to be prepped only once
        """ Turn message into a rendered image and center on the button """
        self.msg_image = self.font.render(self.message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """ Draw on the sprites on the screen """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def update_position(self):
        self.msg_image_rect.center = self.rect.center
