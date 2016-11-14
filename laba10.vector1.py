class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        if y == 0:
            if type(x) == str:
                self.x, self.y = list(map(int, self.x.split(',')))
            else:
                pass

    def __str__(self):
        return str(self.x) + ',' + str(self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        self.x *= (-1)
        self.y *= (-1)
        return Vector(self.x, self.y)

m = input()
n = input()
m = Vector(m)
n = Vector(n)
print(str(m + n))
print(str(m - n))
print(str(m))
