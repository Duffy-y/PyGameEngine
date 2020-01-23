import sys
import os
import gc
import threading
import importlib
sys.path.append(".")

import pygame
from pygame.locals import *

from Input import Input
from Resources import Resources

pygame.init()

class Engine:
    def __init__(self, size, fps, caption):
        # Game parameters
        pygame.display.set_caption(caption)
        self.ROOT               = pygame.display.set_mode(size)
        self.FPS                = fps
        self.GRAPH_PROCESS      = threading.Thread(target=self.graph_loop)
        self.GRAPH_PROCESS.setDaemon(True)

        # Preparation before starting engine
        self.clock              = pygame.time.Clock()
        self.script_classes     = self.load_script_classes()
        Resources.load_resources()

        # Start engine
        self.GRAPH_PROCESS.start()
        self.engine_loop()

    def load_script_classes(self):
        returnedArray = []
        for r, _, f in os.walk("."):
            for file in f:
                if ".py" in file and ".pyc" not in file and "s_" in file:
                    module_name = r.replace(".\\", "") + "." + file.replace(".py", "")
                    class_name  = file.replace(".py", "").replace("s_", "")
                    module      = importlib.import_module(module_name)
                    returnedArray.append(eval("module." + class_name))
        return returnedArray

    def engine_loop(self):
        while True:
            # Input handling
            Input.update()
            for event in Input.EVENT_LIST:
                if event.type == QUIT:
                    sys.exit()
                    pygame.quit()

            self.clock.tick(self.FPS)

    def graph_loop(self):
        while True:
            self.clock.tick(self.FPS)

engine = Engine((500, 500), 60, "Engine under development")
