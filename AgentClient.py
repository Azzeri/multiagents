import random

from tkinter import ttk, StringVar, W
from ttkthemes import ThemedTk
from Album import Album
from Magasine import Magasine


# albumsArr = []
# atmospheres = ["Smutna", "Lekka"]
# languages = ["polski"]
# ocassions = ["Relaks", "Praca"]
# album = Album("Ballady", "Kat", "1989-10-10", 50, "Kompakt", 1, atmospheres, languages, ocassions, 25.5)
# albumsArr.append(album)
# album = Album("Death By Rock And Roll", "The Pretty Reckless", "1989-10-10", 50, "Kompakt", 1, atmospheres,
#               languages, ocassions, 20.0)
# albumsArr.append(album)
# album = Album("Infestissumam", "Ghost", "1989-10-10", 50, "Kompakt", 1, atmospheres, languages, ocassions, 40)
# albumsArr.append(album)
# album = Album("Róże", "KAT", "1989-10-10", 50, "Kompakt", 1, atmospheres, languages, ocassions, 50)
# albumsArr.append(album)


class AgentClient:
    def __init__(self, name, agenttype):
        self.name = name
        self.agenttype = agenttype
        # self.magasine = Magasine("main")
        self.albums = []

    def takealbumsfrommagasine(self, magasine):
        self.albums = magasine.returnalbumstoagent()

    def init(self):
        print("Agent typu {} o nazwie {} rozpoczął działanie.".format(self.agenttype, self.name))

    def displaydata(self):
        for album in self.albums:
            print(album.name, album.albumformat, album.quantity, sep=" : ")

    def returnalbums(self, length, years, nation, atmosphere, formatv, ocassion, language, maxprice, minprice):
        print(length.array, length.priority, sep=" ")
        print(years.array, years.priority, sep=" ")
        print(nation.array, nation.priority, sep=" ")
        print(atmosphere.array, atmosphere.priority, sep=" ")
        print(formatv.array, formatv.priority, sep=" ")
        print(ocassion.array, ocassion.priority, sep=" ")
        print(language.array, language.priority, sep=" ")
        print(minprice)
        print(maxprice)

        # found = 0
        # for album in self.albums:
        #     if float(album.price) <= float(maxprice):
        #         found = 1
        #
        # if found == 0:
        #     return None

        rand = random.randrange(0, len(self.albums), 1)
        while float(self.albums[rand].price) > float(maxprice) or float(self.albums[rand].price) < float(minprice):
            rand = random.randrange(0, len(self.albums), 1)

        return self.albums[rand]
