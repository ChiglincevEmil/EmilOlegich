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
        """ Приводит вектор к удобному для чтения формату """
        return str(self.x) + ',' + str(self.y)

    def __add__(self, other):
        """ Вычисляет вектор, являющийся суммой двух данных векторв """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Вычисляет вектор, являющийся разностью двух данных векторв """
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        """ Вычисляет вектор, являющийся обратным данному вектору """
        self.x *= (-1)
        self.y *= (-1)
        return Vector(self.x, self.y)

a = input()
b = input()
a = Vector(a)
b = Vector(b)
print('Сумма векторов = ' + '(' + str(a + b) + ')')
print('Разность веткоров = ' + '(' + str(a - b) + ')')
print('Вектор, обратный a = ' + '(' + str(a) + ')')
