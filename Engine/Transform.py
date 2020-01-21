import math
import time
import multiprocessing as mp

class Transform:
    def __init__(self, position, rotation, angle):
        self.position   = position
        self.rotation   = rotation
        self.scale      = angle

    def set_position(self, position):
        self.position = position

    def translate(self, translate_vector):
        self.position += translateVector

    def rotate(self, rotationVector):
        self.rotation += rotationVector

    def scale(self, scaleVector):
        self.scale = scaleVector
