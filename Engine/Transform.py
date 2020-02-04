from Vector2D import Vector2
class Transform:
    def __init__(self, position, rotation, angle):
        self.position   = position
        self.rotation   = rotation
        self.scale      = angle

    def __str__(self):
        return f"x : {self.position.x}, y : {self.position.y}, z : {self.position.z}"

    def set_position(self, position):
        self.position = position

    def translate(self, translate_vector):
        self.position += translate_vector

    def rotate(self, rotationVector):
        self.rotation += rotationVector

    def scale(self, scaleVector):
        self.scale = scaleVector
