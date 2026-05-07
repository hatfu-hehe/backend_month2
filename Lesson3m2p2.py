# Abstraction
# Abstaracted class is a pattern for other classes

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod    # USED ONLY WITH ABC CLASS
    def make_sound(self):
        pass

    @abstractmethod
    def test(self):
        ...

# concrete classes
class Dog(Animal):
    # realization of abstr. method
    def make_sound(self):
        print('Woof-woof')

    def test(self):
        print('test in dog')

class Cat(Animal):
    def test(self):
        print('test in cat')

    def make_sound(self):
        print('Meooooowww')


puppy = Dog()
print(puppy.make_sound())
# kitty = Cat()
# print(kitty.make_sound())

