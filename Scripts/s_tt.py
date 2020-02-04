from GameObject import GameObject
from Transform import Transform
from Vector2D import Vector2
from Resources import Resources

import pygame
pygame.init()

class tt:
    def __init__(self):
        GameObject.init_object(self)

        # Components definitions
        self.transform  = Transform(Vector2(100, 100, 1), Vector2(0, 0, 0), Vector2(0, 0, 0))
        self.sprite     = Resources.load("pompier.png")
        self.sprite     = pygame.transform.scale(self.sprite, (100, 100))

    def update(self):
        pass
