class vehicle:
    def start(self):
        print("to start the vehicle")
class car(vehicle):
    def drive(self):
        print("drive a car")
class bike(vehicle):
    def ride(self):
        print("ride a bike")
class electicvehicle(car,bike):
    def use(self):
        print("can both drive and ride")
ev=electicvehicle()
ev.start()
ev.drive()
ev.ride()
ev.use()


