from datetime import datetime

from Album import Album


class Magasine:
    def __init__(self, name):
        self.name = name
        self.albums = [
            Album("Death by Rock and Roll", "The Pretty Reckless", datetime(2021, 2, 2), 50, "Kompakt", 50.5,
                  [1, 2, 1, 3, 1, 3, 1], [0, 3, 0], [0, 3], [2, 3, 0, 1, 1]),
            Album("Unleashed Memories", "Lacuna Coil", datetime(2005, 2, 2), 54, "Kompakt", 45.53,
                  [3, 0, 2, 1, 3, 1, 1], [0, 3, 1], [0, 3], [0, 0, 1, 2, 3]),
            Album("Ballady", "Kat", datetime(1993, 1, 2), 55, "Kompakt", 25.1, [2, 1, 2, 2, 3, 1, 2], [3, 0, 0], [3, 0],
                  [1, 1, 1, 1, 3]),
            Album("Ponad Wszystko", "Ewelina Lisowska", datetime(2016, 11, 11), 55, "Kompakt", 20.29,
                  [3, 1, 3, 0, 3, 1, 2], [3, 0, 0], [3, 0], [1, 1, 2, 3, 3]),
            Album("Hybrid Theory", "Linkin Park", datetime(2000, 10, 24), 49, "Kompakt", 45.59, [2, 2, 1, 2, 1, 2, 1],
                  [0, 3, 0], [0, 3], [3, 2, 1, 1, 1]),
            Album("Ghost", "Infestissumam", datetime(2013, 4, 10), 47, "Kompakt", 45.62, [2, 1, 2, 2, 1, 2, 3],
                  [0, 3, 1], [0, 3], [2, 1, 2, 2, 2]),
            Album("Mgła", "Age of Excuse", datetime(2019, 9, 2), 42, "Kompakt", 30.03, [2, 0, 0, 3, 1, 3, 1], [0, 3, 0],
                  [3, 0], [1, 2, 0, 0, 1]),
            Album("Arachne", "Hunter", datetime(2019, 3, 8), 47, "Kompakt", 30.05, [2, 1, 1, 2, 1, 1, 2], [3, 0, 0],
                  [3, 0], [1, 1, 0, 1, 2]),
            Album("Exercises in Futility", "Mgła", datetime(2015, 9, 4), 42, "Kompakt", 28.94, [2, 0, 0, 3, 1, 3, 1],
                  [0, 3, 0], [3, 0], [1, 2, 0, 0, 1]),
            Album("Fallen", "Evanescence", datetime(2003, 3, 4), 48, "Kompakt", 45.52, [3, 0, 1, 2, 1, 1, 2], [0, 3, 0],
                  [0, 3], [2, 2, 0, 1, 2]),
            Album("Królestwo", "Hunter", datetime(2012, 11, 5), 38, "Kompakt", 23.31, [2, 1, 1, 2, 1, 2, 2], [3, 0, 0],
                  [3, 0], [2, 1, 1, 1, 1]),
            Album("Meliora", "Ghost", datetime(2015, 8, 21), 66, "Kompakt", 67.7, [1, 2, 1, 2, 1, 1, 3], [0, 3, 1],
                  [0, 3], [2, 1, 1, 1, 2]),
            Album("Oddech Wymarłych Światów", "kat", datetime(1987, 11, 10), 39, "Kompakt", 34.56,
                  [2, 1, 1, 3, 1, 3, 2], [3, 1, 0], [3, 0], [3, 3, 0, 0, 1]),
            Album("Songs of Love and Death", "Me and that Man", datetime(2017, 3, 24), 49, "Kompakt", 24.44,
                  [2, 0, 1, 1, 1, 1, 2], [0, 3, 0], [3, 3], [1, 1, 2, 1, 3]),
            Album("Niemożliwe", "Kwiat Jabłoni", datetime(2019, 2, 1), 46, "Kompakt", 27.88, [2, 2, 3, 0, 2, 0, 1],
                  [3, 0, 0], [3, 0], [1, 0, 2, 2, 3]),
            Album("Iron Maiden", "Iron Maiden", datetime(1980, 4, 14), 40, "Kompakt", 45.55, [1, 2, 0, 2, 1, 3, 1],
                  [0, 3, 0], [0, 3], [3, 3, 1, 1, 1])
        ]
