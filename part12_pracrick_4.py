class Hexagon:
    def __init__(self):
        self.per = 0
    def pm(self, a1, a2, a3, a4, a5, a6):
        self.per = a1 + a2 + a3 + a4 + a5 + a6
h_1 = Hexagon()
h_1.pm(2, 3, 5, 8, 2, 4,)
print(h_1.per)   