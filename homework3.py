class Person:
    def __init__(self, name, birth_date, profession, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__profession = profession
        self.__higher_education = higher_education

    def set_profession(self, new_profession):
        self.__profession = new_profession

    def get_education(self):
        return self.__higher_education

    @property
    def get_new_profession(self):
        return self.__profession

    @get_new_profession.setter
    def get_new_profession(self, very_new_profession):
        self.__profession = very_new_profession

    @property
    def get_new_education(self):
        return self.__higher_education

    def introduce(self):
        print(f"I'm {self.name} and I was born {self.birth_date}. "
              f"I work as a {self.get_new_profession}. Bachelor Degree: {self.get_new_education}")


class Classmate(Person):
    def __init__(self, name, birth_date, profession, higher_education, group_name):
        super().__init__(name, birth_date, profession, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"I'm {self.name} and I was born {self.birth_date}. "
              f"I am a classmate of {self.group_name} and I work as a {self.get_new_profession}. "
              f"Bachelor degree: {self.get_new_education}.")


class Friend(Person):
    def __init__(self, name, birth_date, profession, higher_education, hobby):
        super().__init__(name, birth_date, profession, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"I'm {self.name} and I was born {self.birth_date}. "
              f"I kin on {self.hobby} and I work as a {self.get_new_profession}. "
              f"Bachelor degree: {self.get_new_education}.")


class BestFriend(Friend):
    def __init__(self, name, birth_date, profession, higher_education, hobby, shared_memory):
        super().__init__(name, birth_date, profession, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"One of the memories about her/him is referred to {self.shared_memory}.")


friend1 = Friend('Marsel', '19.09.2006', 'Designer', False, 'Reading books')
friend2 = Friend('Daniel', '09.05.2007', 'Racer', False, 'Playing games')
friend2.introduce()
friend1.introduce()

classmate1 = Classmate('Akmaral', '26.11.2007', 'Tourist manager', False, 'Irada')
classmate2 = Classmate('Sezim', '07.07.2007', 'SMM', False, 'Abduhakim')
classmate2.introduce()
classmate1.introduce()

person1 = Person('Niyara', '03.08.2017', 'Model for kids store', False)
friend3 = Friend('Adelya', '18.06.2009', 'Mentor', False, 'Running')
classmate3 = Classmate('Aigiza', '15.06.2005', 'Florist', False, 'Aizhamal')

people = [person1, friend3, classmate3]
for p in people:
    p.introduce()

bestfriend1 = BestFriend('Azaliya', '06.07.2007', 'Architector', False, 'DIY', 'Riding the bikes')
bestfriend1.introduce()

person1.set_profession('Model for kids store')
