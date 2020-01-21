import os
import sys
sys.path.append(".")

import pygame
from pygame.locals import *

pygame.init()

IMAGE_FORMAT_SUPPORTED  = [".png", ".jpg", ".bmp", ".pcx", ".tga", ".tif", ".lbm", ".pbm", ".xpm"]
SOUND_FORMAT_SUPPORTED   = [".ogg", ".wav"]

class Resources:
    LOADED_FILE = {}

    @staticmethod
    def load_resources():
        """ You should not use this function as it's a function dedicated to the engine.
            Use this function only if it's your last choice.
        """
        for r, _, f in os.walk("Resources/"):
            for file in f:
                key = file
                if any(str in file for str in IMAGE_FORMAT_SUPPORTED):
                    value = pygame.image.load(r.replace(".\\", "") + key)
                    Resources.LOADED_FILE[key] = value
                if any(str in file for str in SOUND_FORMAT_SUPPORTED):
                    value = pygame.mixer.load(r.replace(".\\", "") + key)
                    Resources.LOADED_FILE[key] = value

    @staticmethod
    def load(file_name):
        """ Return the pygame object of the corresponding file in "Resources" directory.

        Parameters
        ----------
        file_name : string
            Name of the file, without directory

        Returns
        -------
        Pygame object (image, mixer ...)
            The loaded pygame object, ready to be used in your game.

        """
        if file_name in Resources.LOADED_FILE:
            return Resources.LOADED_FILE[file_name]
        else:
            raise Exception(f"Error : {file_name} does not exists in Resources folder.")
            return None

    @staticmethod
    def unload():
        """ Unload all loaded file from "Resources" directory to save memory.
            Use this function only if you don't use Resources.
        """
        Resources.LOADED_FILE = None
