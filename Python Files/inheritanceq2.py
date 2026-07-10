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