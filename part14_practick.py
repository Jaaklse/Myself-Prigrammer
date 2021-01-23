class Square:
    square_list = []
    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

    def change_size(self, s1):
        self.side += s1
s_1 = Square(29)
print(Square.square_list)
 