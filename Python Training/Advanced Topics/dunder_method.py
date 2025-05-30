class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x+ other.x, self.y+other.y)
    
    def __repr__(self):
        return f'({self.x},{self.y})'

    def __len__(self):
        self.x + self.y

v1 = Vector(19, 20)
v2 = Vector(30, 60)
v3 = v1 + v2

