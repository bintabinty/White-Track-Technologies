from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog says: Bark")

class Cat(Animal):

    def sound(self):
        print("Cat says: Meow")

class Cow(Animal):

    def sound(self):
        print("Cow says: Moo")

d = Dog()
d.sound()

c = Cat()
c.sound()

cw = Cow()
cw.sound()