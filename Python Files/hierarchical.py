class animal:
    def eat(self):
        print("aimals eat")
class dog(animal):
    def bark(self):
        print("dog barks")
class cat(animal):
    def cry(self):
        print("cat cries")
dg=dog()
ct=cat()
dg.eat()
dg.bark()
ct.eat()
ct.cry()
