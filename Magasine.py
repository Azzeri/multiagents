from datetime import datetime
import copy
from Album import Album
import math, random


class Magasine:
    def __init__(self, name):
        self.name = name
        self.albums = [
            Album("Death by Rock and Roll", "The Pretty Reckless", datetime(2021, 2, 2), 50, "Kompakt", 50.5,
                  [1, 2, 1, 3, 1, 3, 1], [0, 3, 0], [0, 3], [2, 3, 0, 1, 1], 10),
            Album("Unleashed Memories", "Lacuna Coil", datetime(2005, 2, 2), 54, "Kompakt", 45.53,
                  [3, 0, 2, 1, 3, 1, 1], [0, 3, 1], [0, 3], [0, 0, 1, 2, 3], 8),
            Album("Ballady", "Kat", datetime(1993, 1, 2), 55, "Kompakt", 25.1, [2, 1, 2, 2, 3, 1, 2], [3, 0, 0], [3, 0],
                  [1, 1, 1, 1, 3], 15),
            Album("Ponad Wszystko", "Ewelina Lisowska", datetime(2016, 11, 11), 55, "Kompakt", 20.29,
                  [3, 1, 3, 0, 3, 1, 2], [3, 0, 0], [3, 0], [1, 1, 2, 3, 3], 23),
            Album("Hybrid Theory", "Linkin Park", datetime(2000, 10, 24), 49, "Kompakt", 45.59, [2, 2, 1, 2, 1, 2, 1],
                  [0, 3, 0], [0, 3], [3, 2, 1, 1, 1], 43),
            Album("Ghost", "Infestissumam", datetime(2013, 4, 10), 47, "Kompakt", 45.62, [2, 1, 2, 2, 1, 2, 3],
                  [0, 3, 1], [0, 3], [2, 1, 2, 2, 2], 12),
            Album("Age of Excuse", "Age of Excuse", datetime(2019, 9, 2), 42, "Kompakt", 30.03, [2, 0, 0, 3, 1, 3, 1],
                  [0, 3, 0],
                  [3, 0], [1, 2, 0, 0, 1], 12),
            Album("Arachne", "Hunter", datetime(2019, 3, 8), 47, "Kompakt", 30.05, [2, 1, 1, 2, 1, 1, 2], [3, 0, 0],
                  [3, 0], [1, 1, 0, 1, 2], 54),
            Album("Exercises in Futility", "Mgła", datetime(2015, 9, 4), 42, "Kompakt", 28.94, [2, 0, 0, 3, 1, 3, 1],
                  [0, 3, 0], [3, 0], [1, 2, 0, 0, 1], 14),
            Album("Fallen", "Evanescence", datetime(2003, 3, 4), 48, "Kompakt", 45.52, [3, 0, 1, 2, 1, 1, 2], [0, 3, 0],
                  [0, 3], [2, 2, 0, 1, 2], 54),
            Album("Królestwo", "Hunter", datetime(2012, 11, 5), 38, "Kompakt", 23.31, [2, 1, 1, 2, 1, 2, 2], [3, 0, 0],
                  [3, 0], [2, 1, 1, 1, 1], 23),
            Album("Meliora", "Ghost", datetime(2015, 8, 21), 66, "Kompakt", 67.7, [1, 2, 1, 2, 1, 1, 3], [0, 3, 1],
                  [0, 3], [2, 1, 1, 1, 2], 23),
            Album("Oddech Wymarłych Światów", "kat", datetime(1987, 11, 10), 39, "Kompakt", 34.56,
                  [2, 1, 1, 3, 1, 3, 2], [3, 1, 0], [3, 0], [3, 3, 0, 0, 1], 54),
            Album("Songs of Love and Death", "Me and that Man", datetime(2017, 3, 24), 49, "Kompakt", 24.44,
                  [2, 0, 1, 1, 1, 1, 2], [0, 3, 0], [3, 3], [1, 1, 2, 1, 3], 65),
            Album("Niemożliwe", "Kwiat Jabłoni", datetime(2019, 2, 1), 46, "Kompakt", 27.88, [2, 2, 3, 0, 2, 0, 1],
                  [3, 0, 0], [3, 0], [1, 0, 2, 2, 3], 98),
            Album("Iron Maiden", "Iron Maiden", datetime(1980, 4, 14), 40, "Kompakt", 45.55, [1, 2, 0, 2, 1, 3, 1],
                  [0, 3, 0], [0, 3], [3, 3, 1, 1, 1], 23)
        ]

        self.noalbums = 0
        for album in self.albums:
            self.noalbums += album.quantity

    def returnalbumstoagent(self):
        noalbumstoreturntotal = math.floor(len(self.albums) * 0.75)
        # print("Albumy do zwrotu: ", noalbumstoreturntotal)
        noalbumstoreturn = 0
        albumstoreturn = []
        auxarr = []

        while noalbumstoreturn < noalbumstoreturntotal:
            randomizedalbum = self.albums[random.randint(0, len(self.albums) - 1)]
            while (randomizedalbum in auxarr) or (randomizedalbum.quantity == 0):
                randomizedalbum = self.albums[random.randint(0, len(self.albums) - 1)]
            # if randomizedalbum.quantity == 0:
            #     break
            # print(randomizedalbum.name,randomizedalbum.quantity, sep=" : Wylosowany : ")
            randomizedquantity = random.randint(1, randomizedalbum.quantity)
            noalbumstoreturn += 1
            #print("Wylosowana ilosc: {}",randomizedquantity)
            albumtoreturn = copy.deepcopy(randomizedalbum)
            randomizedalbum.quantity -= randomizedquantity
           # print(randomizedalbum.name, randomizedalbum.quantity, sep=" : Wylosowany po odjęciu ilości : ")
            albumtoreturn.quantity = randomizedquantity
           # print(albumtoreturn.name, albumtoreturn.quantity, sep=" : Zwracany : ")
            albumstoreturn.append(albumtoreturn)
            auxarr.append(randomizedalbum)
            # randomizedquantity = random.randint(1, randomizedalbum.quantity)
            # noalbumstoreturn += 1
            # aux = randomizedalbum.quantity - randomizedquantity
            # randomizedalbum.quantity = randomizedquantity
            # albumstoreturn.append(randomizedalbum)
            # randomizedalbum.quantity = aux

        return albumstoreturn

    def displaydata(self):
        for album in self.albums:
            print(album.name, album.albumformat, album.quantity, sep=" : ")

        # self.albums = [
        #     Album("Death by Rock and Roll", "The Pretty Reckless", datetime(2021, 2, 2), 50, "Kompakt", 50.5,
        #           [1, 2, 1, 3, 1, 3, 1], [0, 3, 0], [0, 3], [2, 3, 0, 1, 1], 10),
        #     Album("Unleashed Memories", "Lacuna Coil", datetime(2005, 2, 2), 54, "Kompakt", 45.53,
        #           [3, 0, 2, 1, 3, 1, 1], [0, 3, 1], [0, 3], [0, 0, 1, 2, 3], 8),
        #     Album("Ballady", "Kat", datetime(1993, 1, 2), 55, "Kompakt", 25.1, [2, 1, 2, 2, 3, 1, 2], [3, 0, 0], [3, 0],
        #           [1, 1, 1, 1, 3], 15),
        #     Album("Ponad Wszystko", "Ewelina Lisowska", datetime(2016, 11, 11), 55, "Kompakt", 20.29,
        #           [3, 1, 3, 0, 3, 1, 2], [3, 0, 0], [3, 0], [1, 1, 2, 3, 3], 23),
        #     Album("Hybrid Theory", "Linkin Park", datetime(2000, 10, 24), 49, "Kompakt", 45.59, [2, 2, 1, 2, 1, 2, 1],
        #           [0, 3, 0], [0, 3], [3, 2, 1, 1, 1], 43),
        #     Album("Ghost", "Infestissumam", datetime(2013, 4, 10), 47, "Kompakt", 45.62, [2, 1, 2, 2, 1, 2, 3],
        #           [0, 3, 1], [0, 3], [2, 1, 2, 2, 2], 12),
        #     Album("Age of Excuse", "Age of Excuse", datetime(2019, 9, 2), 42, "Kompakt", 30.03, [2, 0, 0, 3, 1, 3, 1],
        #           [0, 3, 0],
        #           [3, 0], [1, 2, 0, 0, 1], 12),
        #     Album("Arachne", "Hunter", datetime(2019, 3, 8), 47, "Kompakt", 30.05, [2, 1, 1, 2, 1, 1, 2], [3, 0, 0],
        #           [3, 0], [1, 1, 0, 1, 2], 54),
        #     Album("Exercises in Futility", "Mgła", datetime(2015, 9, 4), 42, "Kompakt", 28.94, [2, 0, 0, 3, 1, 3, 1],
        #           [0, 3, 0], [3, 0], [1, 2, 0, 0, 1], 14),
        #     Album("Fallen", "Evanescence", datetime(2003, 3, 4), 48, "Kompakt", 45.52, [3, 0, 1, 2, 1, 1, 2], [0, 3, 0],
        #           [0, 3], [2, 2, 0, 1, 2], 54),
        #     Album("Królestwo", "Hunter", datetime(2012, 11, 5), 38, "Kompakt", 23.31, [2, 1, 1, 2, 1, 2, 2], [3, 0, 0],
        #           [3, 0], [2, 1, 1, 1, 1], 23),
        #     Album("Meliora", "Ghost", datetime(2015, 8, 21), 66, "Kompakt", 67.7, [1, 2, 1, 2, 1, 1, 3], [0, 3, 1],
        #           [0, 3], [2, 1, 1, 1, 2], 23),
        #     Album("Oddech Wymarłych Światów", "kat", datetime(1987, 11, 10), 39, "Kompakt", 34.56,
        #           [2, 1, 1, 3, 1, 3, 2], [3, 1, 0], [3, 0], [3, 3, 0, 0, 1], 54),
        #     Album("Songs of Love and Death", "Me and that Man", datetime(2017, 3, 24), 49, "Kompakt", 24.44,
        #           [2, 0, 1, 1, 1, 1, 2], [0, 3, 0], [3, 3], [1, 1, 2, 1, 3], 65),
        #     Album("Niemożliwe", "Kwiat Jabłoni", datetime(2019, 2, 1), 46, "Kompakt", 27.88, [2, 2, 3, 0, 2, 0, 1],
        #           [3, 0, 0], [3, 0], [1, 0, 2, 2, 3], 98),
        #     Album("Iron Maiden", "Iron Maiden", datetime(1980, 4, 14), 40, "Kompakt", 45.55, [1, 2, 0, 2, 1, 3, 1],
        #           [0, 3, 0], [0, 3], [3, 3, 1, 1, 1], 23),
        #     Album("Age of Excuse", "Mgła", datetime(2019, 9, 2), 42, "MP3", 30.03, [2, 0, 0, 3, 1, 3, 1], [0, 3, 0],
        #           [3, 0], [1, 2, 0, 0, 1], 25),
        #     Album("Arachne", "Hunter", datetime(2019, 3, 8), 47, "MP3", 30.05, [2, 1, 1, 2, 1, 1, 2], [3, 0, 0],
        #           [3, 0], [1, 1, 0, 1, 2], 54),
        #     Album("Exercises in Futility", "Mgła", datetime(2015, 9, 4), 42, "MP3", 28.94, [2, 0, 0, 3, 1, 3, 1],
        #           [0, 3, 0], [3, 0], [1, 2, 0, 0, 1], 65),
        #     Album("Fallen", "Evanescence", datetime(2003, 3, 4), 48, "MP3", 45.52, [3, 0, 1, 2, 1, 1, 2], [0, 3, 0],
        #           [0, 3], [2, 2, 0, 1, 2], 34),
        #     Album("Królestwo", "Hunter", datetime(2012, 11, 5), 38, "MP3", 23.31, [2, 1, 1, 2, 1, 2, 2], [3, 0, 0],
        #           [3, 0], [2, 1, 1, 1, 1], 56),
        #     Album("Death by Rock and Roll", "The Pretty Reckless", datetime(2021, 2, 2), 50, "Winyl", 50.5,
        #           [1, 2, 1, 3, 1, 3, 1], [0, 3, 0], [0, 3], [2, 3, 0, 1, 1], 23),
        #     Album("Unleashed Memories", "Lacuna Coil", datetime(2005, 2, 2), 54, "Winyl", 45.53,
        #           [3, 0, 2, 1, 3, 1, 1], [0, 3, 1], [0, 3], [0, 0, 1, 2, 3], 88),
        #     Album("Ballady", "Kat", datetime(1993, 1, 2), 55, "Winyl", 25.1, [2, 1, 2, 2, 3, 1, 2], [3, 0, 0], [3, 0],
        #           [1, 1, 1, 1, 3], 56),
        #     Album("Ponad Wszystko", "Ewelina Lisowska", datetime(2016, 11, 11), 55, "Winyl", 20.29,
        #           [3, 1, 3, 0, 3, 1, 2], [3, 0, 0], [3, 0], [1, 1, 2, 3, 3], 76),
        #     Album("Hybrid Theory", "Linkin Park", datetime(2000, 10, 24), 49, "Winyl", 45.59, [2, 2, 1, 2, 1, 2, 1],
        #           [0, 3, 0], [0, 3], [3, 2, 1, 1, 1], 23),
        # ]
