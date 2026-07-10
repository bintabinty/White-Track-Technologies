class fruit:
    def taste(self):
        print("fruit taste sweet")
class mango(fruit):
    def color(self):
        print("color of mango is yellow")
mg=mango()
mg.taste()
mg.color()

#2
class shape:
    def draw(self):
        print("to draw a shape")
class circle(shape):
    def radius(self):
        print("draw the cicle with the raduis")
class rectangle(shape):
    def length(self):
        print("draw rectangle with length")
cr=circle()
rt=rectangle()
cr.draw()
cr.radius()
rt.draw()
rt.length()