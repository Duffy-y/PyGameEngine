import sys
import time as t
sys.path.append("Engine/")      # Allow import of all Engine Component

import pygame
from pygame.locals import *

pygame.init()

from Input import Input
from Engine import *

engine = Engine((500, 500), 60, "Engine under development")

while True:
    print("yeet")
