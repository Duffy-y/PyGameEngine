from GameObject import GameObject
from Transform import Transform
from Vector2D import Vector2
from Resources import Resources
from Input import Input

import pygame
from pygame.locals import *
pygame.init()

class test:
    def __init__(self):
        GameObject.init_object(self)

        # Components definitions
        self.transform  = Transform(Vector2(0, 0, 0), Vector2(0, 0, 0), Vector2(0, 0, 0))
        self.sprite     = Resources.load("flamme.png")
        self.sprite     = pygame.transform.scale(self.sprite, (50, 50))

    def update(self):
        self.transform.translate(Vector2(1, 1, 0))
        if Input.get_key(K_SPACE):
            self.transform.translate(Vector2(0, -5, 0))
        pass
