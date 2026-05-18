# Magical methods. Pockets (Lesson6)
# There is the large set of registered methods in Python. The structure = __'method'__.

class Playlist:
    # Magical method example. (Dunder = double underscore)
    def __init__(self, name, songs=None):
        self.name = name
        self.__songs = songs

    def __str__(self):                    # returns the value of a stream
        return f'<Playlist name = {self.name}>'

    def __len__(self):                    # works even with private attributes
        return len(self.__songs)

    def __contains__(self, item):
        return item in self.__songs

    def __bool__(self):
        return bool(self.__songs)

