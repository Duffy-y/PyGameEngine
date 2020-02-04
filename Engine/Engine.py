import os
import sys
import threading
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pygame
from pygame.locals import *

from Input import Input
from Resources import Resources
from GameObject import GameObject

pygame.init()
Resources.init()
GameObject.init()

class Engine:
    def __init__(self, size, fps, caption):
        # Game parameters
        pygame.display.set_caption(caption)
        self.ROOT               = pygame.display.set_mode(size)
        self.UPDATE_RATE        = fps

        # Preparation before starting engine
        self.clock              = pygame.time.Clock()

        # Start engine
        self.engine_loop()

    def engine_loop(self):
        while True:
            # Input handling
            Input.update()
            for event in Input.EVENT_LIST:
                if event.type == QUIT:
                    sys.exit()
                    pygame.quit()

            GameObject.update_objects()

            self.ROOT.fill((0, 0, 0))
            for obj in GameObject.scripted_objects:
                self.ROOT.blit(obj.sprite, (obj.transform.position.x - obj.sprite_rect[2] / 2, obj.transform.position.y - obj.sprite_rect[3] / 2))
            pygame.display.update()

            self.clock.tick_busy_loop(self.UPDATE_RATE)

ENGINE_OBJ = Engine((1000, 1000), 144, "Engine under development")
