from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Rectangle Area =", self.length * self.width)
class Circle(shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area =", 3.14 * self.radius * self.radius)

# Object Creation
r = rectangle(10, 5)
r.area()

c = Circle(7)
c.area()


    