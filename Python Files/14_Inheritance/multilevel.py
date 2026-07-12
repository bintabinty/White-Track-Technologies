class vehicle:
    def display(self):
        print("this is a vehicle")
class car(vehicle):
    def show(self):
        print("car is a vehicle")
class sportscar(car):
    def view(self):
        print("sports car is a type of car")
sp=sportscar()
sp.display()
sp.show()
sp.view()