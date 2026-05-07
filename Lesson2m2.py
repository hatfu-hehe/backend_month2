#principles of OOP -  Inheritage, Polymorphism. Git - commits, creating repository, git push
# directory = fold
# repository = project

# Principles of OOP
# 1. Inheritage
# 2. Polymorphism

# signature terminology?

"""Inheritage principal"""
class Car:                  # parental class (superclass) for Bus and Truck
    #constructor/initializator
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print(f"The car of the model {self.model} drives to {destination}.")

    def change_color(self, new_color):
        self.color = new_color


class Bus(Car):           # subsidiary class (descendant)
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

    def drive_to(self, destination):                 # rewriting the parental class's code
        super().drive_to(destination)                # returning to the method of the parental class Car
        print(f"The bus {self.number} of the model {self.model} drives to {destination}.")


class Truck(Car):        # subsidiary class
    def __init__(self, color, model):
        super().__init__(color, model)

    def change_color(self, new_color):
        self.color = new_color
        print(f"The truck's color has been changed to {self.color}.")


car2 = Car('black', 'BMW')
car2.change_color('gray')
bus_42 = Bus('green', 'Mercedes', '254')
print(bus_42.color, bus_42.model, bus_42.number)
bus_42.drive_to('Sokuluk')
truck22 = Truck('pink', 'Hz')
truck22.change_color('violet')
print(truck22.color, truck22.model)
truck22.drive_to('Tokmok')
car2.drive_to('Bishkek')

print(type(truck22))
print(isinstance(truck22, Truck))
print(isinstance(car2, Car))
print(isinstance(truck22, Car))

"""Polymorphism"""
vehicles = [car2, truck22, bus_42]           # polymorphism example (also in lesson's record)
for v in vehicles:
    v.drive_to('Karakol')
    # v.drive_to(destination='Karakol')      # not recommended way

