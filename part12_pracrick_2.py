import math

class Circle:
    def __init__(self):
        self.plo = 0

    def area(self, radius, pi):
        self.plo = (radius ** 2) * pi
        return self.plo
c_1 = Circle()
print(c_1.area(4, math.pi))    