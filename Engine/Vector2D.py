import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalize(self):
        vector_norm = math.sqrt(self.x ** 2 + self.y ** 2)
        return vector_norm

    def __str__(self):
        return f"Vector2D : ({self.x}, {self.y})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector2(x, y)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector2(x, y)

    def __pow__(self, other):
        x = self.x ** other
        y = self.y ** other
        return Vector2(x, y)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector2(x, y)

    def __floordiv__(self, other):
        x = self.x // other
        y = self.y // other
        return Vector2(x, y)

    def __iadd__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    def __isub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector2(x, y)

    def __imul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector2(x, y)

    def __ipow__(self, other):
        x = self.x ** other
        y = self.y ** other
        return Vector2(x, y)

    def __itruediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector2(x, y)

    def __ifloordiv__(self, other):
        x = self.x // other
        y = self.y // other
        return Vector2(x, y)
