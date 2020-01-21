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
        Input.EVENT_LIST        = pygame.event.get()
        Input.KEY_LIST          = pygame.key.get_pressed()
        Input.BUTTON_LIST       = pygame.mouse.get_pressed()
        Input.mouse_position    = pygame.mouse.get_pos()

    @staticmethod
    def get_key(keycode):
        if Input.KEY_LIST[keycode]:
            return True
        else:
            return False

    @staticmethod
    def get_mouse_button(button):
        if Input.BUTTON_LIST[button]:
            return True
        else:
            return False

    @staticmethod
    def get_event(event_type):
        for event in Input.EVENT_LIST:
            if event.type == event_type:
                return True
            else:
                return False
