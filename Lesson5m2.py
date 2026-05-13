# Multitute inheritage, class' methods
#  PEP8

class Animal:
    def move(self):
        print('An animal moves')


class Swimming(Animal):
    def move(self):
        print('Swims')


class Flying(Animal):
    def move(self):
        print('Flies')


class Duck(Swimming, Flying):     # queue matters
        def move(self):
            print('A duck flies and swims.')

duck = Duck()
duck.move()
print(Duck.__mro__)    # method resolution order

bird = Flying()
bird.move()
print(Flying.__mro__)   # method resolution order