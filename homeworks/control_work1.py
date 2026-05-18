
class Animal:
    def __init__(self, name):
        self.__name = name
        self.__age = 0

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, new_name):
        self.__name = new_name

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def get_age(self, new_age):
        self.__age = new_age

    def make_sound(self):
        print(f"A pet named {self.get_name} is {self.get_age} years/months old <3."
              f"It makes cute sounds <3.")


class Chihuahua(Animal):
    def make_sound(self):
        print(f"A chihuahua named {self.get_name} is {self.get_age} years/months old <3."
              f"It barks really loudly <3.")


class Hamster(Animal):
    def make_sound(self):
        print(f"A hamster named {self.get_name} is {self.get_age} years/months old <3."
              f"It squeaks way too much <3.")

dog = Chihuahua('Bimo')
dog.get_age = 3
print(dog.get_age)
# dog.make_sound()

rodent = Hamster('Bella')
rodent.get_age = 1
print(rodent.get_age)
# rodent.make_sound()

pets = [dog, rodent]
for pet in pets:
    pet.make_sound()