import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(5, 5)

class Input:
    KEY_LIST        = []
    EVENT_LIST      = []
    BUTTON_LIST     = []

    mouse_position  = None

    @staticmethod
    def update():
        """Set event, key, mouse button and position in Input classe.
        You should'nt use this function as it's dedicated to the engine.
        The engine call this function before every frame and object update.
        """
        Input.EVENT_LIST        = pygame.event.get()
        Input.KEY_LIST          = pygame.key.get_pressed()
        Input.BUTTON_LIST       = pygame.mouse.get_pressed()
        Input.mouse_position    = pygame.mouse.get_pos()

    @staticmethod
    def get_key(keycode):
        """Allow fast access to a keyboard key state.
        Example : Input.get_key(K_SPACE)

        Parameters
        ----------
        keycode : pygame.key
            Key constant
            Example : K_ESCAPE

        Returns
        -------
        bool
            True if the key is pressed, False otherwise

        """
        if Input.KEY_LIST[keycode]:
            return True
        else:
            return False

    @staticmethod
    def get_mouse_button(button):
        """Allow fast access to a mouse button state.

        Parameters
        ----------
        button : int
            Mouse button ID (0 : Left click | 1 : Middle click | 2 : Right click)

        Returns
        -------
        bool
            True if the button is pressed, False othwerwise

        """
        if Input.BUTTON_LIST[button]:
            return True
        else:
            return False

    @staticmethod
    def get_event(event_type):
        """Allow fast access to event list

        Parameters
        ----------
        event_type : pygame.event
            Event type you want to check.

        Returns
        -------
        bool
            True if the event exists, False otherwise.

        """
        for event in Input.EVENT_LIST:
            if event.type == event_type:
                return True
            else:
                return False
