# Algorithms. Find some information about this theme.
# Magical methods. Pockets
# Learn smthg about 'with' = context manager
# Learn some magical methods

# directory = fold
# files = modules
# rewatch last 2 lessons on the platform

from lessons.playlist import Playlist
from lessons.Lesson3m2 import Car

playlist_pop = Playlist(
    name = 'Pop',
    songs = ['Shape of my heart']
)
print(playlist_pop)
car_1 = Car('bmw','black')
print(car_1)
print(len(playlist_pop))
print("GO" in playlist_pop)
print("Shape of my heart" in playlist_pop)

if playlist_pop:
    print("Playlist is not empty")
else:
    print('Empty')