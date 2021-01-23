class Rectangle:
    def __init__(self, s1, s2):
        self.side_1 = s1
        self.side_2 = s2
    
    def calculate_perimeter(self):
        return 2 * (self.side_1 + self.side_2) 

class Square:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 4 * self.side

r_1 = Rectangle(10, 4)
print(r_1.calculate_perimeter())       
s_2 = Square(6)
print(s_2.calculate_perimeter())