#OOP: first lesson

class Car:
    #constructor/initializator               # classes are usually created with the title letter
    def __init__(self, color, model):        # functions in classes are called "methods"
        self.color = color                   # some functions are special and were reserved in the system
        self.model = model                   # it's not calling, it's creating the object (initializing)

    def drive_to(self, destination):
        print(f"The car of the model {self.model} drives to {destination}.")

#github.com

"""Initializing (Using) of objects"""
car1 = Car('white', 'Mercedes')
car2 = Car('black', 'BMW')
# print(car2)
# print(car1)
# print(type(car1))    # class of this object is refered to class Car

print(car1.color, car1.model)
print(car2.color, car2.model)
car1.drive_to('Naryn')

# car1.color = 'grey'      # changing properties
# car2.steering_wheel = 'left'
# print(car2.steering_wheel, car2.color, car2.model)   # creating the random property only for an exact object


