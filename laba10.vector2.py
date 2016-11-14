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

    def length(self):
        return (abs(self.x)**2+abs(self.y**2))**0.5

v = Vector()
lmax = 0
l = 0
max = 0
n = int(input())
for i in range(n):
    vec = input()
    vec = Vector(vec)
    l = vec.length()
    if l > lmax:
        max = vec
        lmax = l
print(str(max))

