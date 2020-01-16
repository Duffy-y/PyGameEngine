import math
import time
import multiprocessing as mp

class Transform:
    def __init__(self, position, rotation, angle):
        self.position   = position
        self.rotation   = rotation
        self.scale      = angle

    def SetPosition(self, position):
        self.position = position

    def Translate(self, translateVector):
        self.position += translateVector

    def LerpTranslate(self, translateVector):
        """Lerp the movement, to make it more real, use modified sigmoid function to simulate a form of acceleration.

        Parameters
        ----------
        translateVector : Vector
            A vector which represent the movement of the object

        No data are returned

        """
        def lerp(pipe):
            end_time    = time.time() + 1
            delta_time  = time.time() - end_time
            while delta_time < 1:
                pipe.send(1 / (1 + math.exp(-7 * delta_time + 4)))
                delta_time = time.time() - end_time
            pipe.send(-1)

        parentPipe, childPipe = mp.Pipe()
        lerpProcess = mp.Process(target=lerp, args=(childPipe, ))
        lerpProcess.start()

        while True:
            print(parentPipe.recv())

    def Rotate(self, rotationVector):
        self.rotation += rotationVector

    def Scale(self, scaleVector):
        self.scale = scaleVector
