import random

from tkinter import ttk, StringVar, W
from ttkthemes import ThemedTk
from Album import Album

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

    def init(self):
        print("Agent typu {} o nazwie {} rozpoczął działanie.".format(self.agenttype, self.name))

    @staticmethod
    def returnalbums(length, years, nation, atmosphere, formatv, ocassion, language, maxprice):
        print(length.array, length.priority, sep=" ")
        print(years.array, years.priority, sep=" ")
        print(nation.array, nation.priority, sep=" ")
        print(atmosphere.array, atmosphere.priority, sep=" ")
        print(formatv.array, formatv.priority, sep=" ")
        print(ocassion.array, ocassion.priority, sep=" ")
        print(language.array, language.priority, sep=" ")
        print(maxprice)

        # rand = random.randrange(0, len(albumsArr), 1)
        # while float(albumsArr[rand].price) > float(maxprice):
        #     rand = random.randrange(0, len(albumsArr), 1)
        #
        # return albumsArr[rand]
