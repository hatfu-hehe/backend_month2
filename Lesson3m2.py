#  principles of OPP: Incapsulation, Abstraction. Git - branches

"""Incapsulation"""
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.__max_speed = 400     # private attribute: can not be used outside the class
        self._fined = False        # protected attribute: not recommended to use outside the class

    def _calculated_fuel(self):    # protected method
        print(self.color)
        return 1

    def drive_to(self, destination):
        if not self._calculated_fuel():
            print('No fuel')
        print(f"The car of the model {self.model} drives to {destination},"
              f" Fined:", 'yes' if car1._fined else "no")

    def change_color(self, new_color):
        self.color = new_color

    # such types of methods are called "getters" (for returning the values of private attributes
    def get_max_speed(self):
        return self.__max_speed

    # setters insert the value. The second way to recall the value of private attribute. Or monitor the process
    def set_max_speed(self, new_speed):
        if new_speed < 0:
            raise ValueError('New speed is slower than 0 km per h')
        self.__max_speed = new_speed

    # more pythonic way to use getter/setter
    @property         # one of decorators (svoistvo)
    def max_speed(self):
        # getter only
        return self.__max_speed

    @max_speed.setter      # creating setter from @property
    def max_speed(self, new_speed):
        if new_speed < 0:
            raise ValueError('New speed is slower than 0 km per h')
        self.__max_speed = new_speed


car1 = Car('black', 'lixiang')
car2 = Car('white', 'ford')

print(car1.color, car1.model)
car1.drive_to('Kant')
print('Fined:', 'yes' if car1._fined else 'no')
car1._calculated_fuel()
car1.__max_speed = 294    # non-existent attribute. It may be similar to the one in Car (illusion)
# print(car2.__max_speed)
print(f"Car1's speed: {car1.get_max_speed()}")
car1.set_max_speed(79)
print(f"Car1's speed: {car1.get_max_speed()}")
print(f"Car1's speed: {car1.max_speed}")     # was called with @property
car1.max_speed = 365
print(f"Car1's speed: {car1.max_speed}")
# MANGLING next
print(f'car1 max_speed private: {car1._Car__max_speed}')   # such codes only for testing! without getter/setter