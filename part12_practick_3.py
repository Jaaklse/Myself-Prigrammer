class Triangle:
    def __init__(self):
        self.plo = 0

    def area(self, h, a):
        self.plo = (h * a) // 2

tr_1 = Triangle()
tr_1.area(2, 6)
print(tr_1.plo)    