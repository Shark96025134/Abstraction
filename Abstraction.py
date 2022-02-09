from abc import ABC,abstractmethod

class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):
        print('3 sides')

class Pentagon(Polygon):
    def sides(self):
        print('5 sides')

class Hexagon(Polygon):
    def sides(self):
        print('6 sides')

class Quad(Polygon):
    def sides(self):
        print('4 sides')

t = Triangle()
q = Quad()
p = Pentagon()
h = Hexagon()

t.sides()
q.sides()
p.sides()
h.sides()
