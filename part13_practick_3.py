class Shape:
    def who_am_i(у):
       print('Я - фигура')        

class Rectangle(Shape):
    def __init__(self, s1, s2):
        self.side_1 = s1
        self.side_2 = s2
        
    def calculate_perimeter(self):
        return 2 * (self.side_1 + self.side_2) 

class Square(Shape):
    def __init__(self, s):
        self.side = s
        
    def calculate_perimeter(self):
        return 4 * self.side
r_1 = Rectangle(3, 8)
r_1.who_am_i()
s_1 = Square(4)
s_1.who_am_i()