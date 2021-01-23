class Square:
    def __init__(self, s):
        self.side = s

    def change_size(self, s1):
        self.side += s1
s_1 = Square(8)
print(s_1.side)
s_1.change_size(-8)
print(s_1.side)            