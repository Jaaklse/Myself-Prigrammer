class Horse:
    def __init__(self, n, r):
        self.name = n
        self.rider = r

class Rider:
    def __init__(self, n):
        self.name = n

Jakles = Rider('Яшка')
plotva = Horse('Плотва', Jakles)
print(plotva.rider.name)        