import pygame
import sys
from pygame.locals import *


def check_events(controller):
    """ Respond to key presses and mouse events """
    for event in pygame.event.get():
        # When the exit button is clicked
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # On Key Pressed Event
        if event.type == KEYDOWN:
            check_keydown_events(event, controller)

        # On Key Released Event
        if event.type == KEYUP:
            check_keyup_events(event, controller)


def check_keydown_events(event, controller):
    """ On keys and mouse is pressed down events """
    # When the player is moving right
    if event.key == K_RIGHT or event.key == K_d:
        # Have the controller trying to move right
        controller.MOVERIGHT = True
        controller.MOVELEFT = False

    # When the player is trying to left
    if event.key == K_LEFT or event.key == K_a:
        controller.MOVERIGHT = False
        controller.MOVELEFT = True

    # When the player is trying to move up
    if event.key == K_UP or event.key == K_w:
        controller.MOVEUP = True
        controller.MOVEDOWN = False

    # When the player is trying to move down
    if event.key == K_DOWN or event.key == K_s:
        controller.MOVEUP = False
        controller.MOVEDOWN = True

def check_keyup_events(event, controller):
    """ On keys and mouse is released events """
    # When the player wants to stop moving right
    if event.key == K_RIGHT or event.key == K_d:
        controller.MOVERIGHT = False

    # When the player wants to stop moving left
    if event.key == K_LEFT or event.key == K_a:
        controller.MOVELEFT = False

    # When the player wants to stop moving up
    if event.key == K_UP or event.key == K_w:
        controller.MOVEUP = False

    # When the player wants to stop moving down
    if event.key == K_DOWN or event.key == K_s:
        controller.MOVEDOWN = False

    # On release of the escape button will exit the program
    if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()
