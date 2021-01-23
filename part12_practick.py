class Apple:
    def __init__(self, w, c, t):
        self.weight = w
        self.color = c
        self.taste = t
        self.mold = 0

    def rot(self, days, temp):
        self.mold = days * temp

apple = Apple(8, 'red', 'tasty')
print(apple.color)
apple.rot(5, 43)
print(apple.mold)