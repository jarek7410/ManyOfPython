import math


class circle:
    def __init__(self, r):
        self.r = r

    def pole(self):
        return math.pi * self.r * self.r;

    def obw(self):
        return math.pi * self.r * 2


class squer:
    def __init__(self, a):
        self.a = a

    def pole(self):
        return self.a * self.a

    def obw(self):
        return 4 * self.a


class triangle:
    def __init__(self, a, b, c):
        if a + b < c or a + c < b or c + b < a:
            raise ValueError("\"wrong sides of triangle\"")
        else:
            self.sides = [a, b, c]

    def pole(self):
        a = self.sides
        s = (a[0] + a[1] + a[2]) / 2
        return (s * (s - a[0]) * (s - a[1]) * (s - a[2])) ** 0.5

    def obw(self):
        return self.sides[0]+self.sides[1]+self.sides[2]
