import os
import sys
sys.path.append(".")

import pygame
from pygame.locals import *

IMAGE_FORMAT_SUPPORTED  = [".png", ".jpg", ".bmp", ".pcx", ".tga", ".tif", ".lbm", ".pbm", ".xpm"]
SOUND_FORMAT_SUPPORTED   = [".ogg", ".wav"]

class Resources:
    LOADED_FILE = {}

    @staticmethod
    def load_resources():
        for r, _, f in os.walk("."):
            for file in f:
                if any(str in file for str in IMAGE_FORMAT_SUPPORTED):


    # @staticmethod
    # def load(file_name):


    # @staticmethod
    # def unload(file_name):


l = Resources()
