class Person:
    def __init__(self, name, birth_date, profession):
        self.name = name
        self.birth_date = birth_date
        self.profession = profession

    def introduce(self):
        print(f"I'm {self.name} and I was born {self.birth_date}. "
              f"I work as a {self.profession}.")

class Classmate(Person):
    def __init__(self, name, birth_date, profession, group_name):
        super().__init__(name, birth_date, profession)
        self.group_name = group_name

    def introduce(self):
        print(f"I'm {self.name} and I was born {self.birth_date}. "
              f"I am a classmate of {self.group_name} and I work as a {self.profession}.")

class Friend(Person):
    def __init__(self, name, birth_date, profession, hobby):
        super().__init__(name, birth_date, profession)
        self.hobby = hobby

    def introduce(self):
        print(f"I'm {self.name} and I was born {self.birth_date}. "
              f"I kin on {self.hobby} and I work as a {self.profession}.")

class BestFriend(Friend):
    def __init__(self, name, birth_date, profession, hobby, shared_memory):
        super().__init__(name, birth_date, profession, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"One of the memories about her/him is referred to {self.shared_memory}.")


friend1 = Friend('Marsel', '19.09.2006', 'Designer', 'Reading books')
friend2 = Friend('Daniel', '09.05.2007', 'Racer', 'Playing games')
friend2.introduce()
friend1.introduce()

classmate1 = Classmate('Akmaral', '26.11.2007', 'Irada', 'Tourist manager')
classmate2 = Classmate('Sezim', '07.07.2007', 'Abduhakim', 'SMM')
classmate2.introduce()
classmate1.introduce()

person1 = Person('Niyara', '03.08.2017', 'Model for kids store')
friend3 = Friend('Adelya', '18.06.2009', 'Running', 'Mentor')
classmate3 = Classmate('Aigiza', '15.06.2005', 'Florist', 'Aizhamal')

people = [person1, friend3, classmate3]
for p in people:
    p.introduce()

bestfriend1 = BestFriend('Azaliya', '06.07.2007', 'DIY', 'Architector', 'Riding the bikes')
bestfriend1.introduce()