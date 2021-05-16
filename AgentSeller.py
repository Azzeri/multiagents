import random

from tkinter import ttk, StringVar, W
from ttkthemes import ThemedTk
from Album import Album
from Magasine import Magasine


class AgentSeller:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def take_albums_from_magasine(self, magasine):
        self.albums = magasine.returnalbumstoagent()

    def displaydata(self):
        for album in self.albums:
            print(album.name, album.albumformat, album.quantity, sep=" : ")

    def returnalbums(self, data_sets):
        albums_to_return = []
        for album in self.albums:
            albums_to_return.append(album)

        # data_sets = [DataSet(lengthArr, priors[0]), DataSet(yearsArr, priors[1]), DataSet(nationArr, priors[2]),
        #              DataSet(atmosphereArr, priors[3]), DataSet(formatArr, priors[4]), DataSet(ocassionArr, priors[5]),
        #              DataSet(languageArr, priors[6])]
        # print(length.array, length.priority, sep=" ")
        # print(years.array, years.priority, sep=" ")
        # print(nation.array, nation.priority, sep=" ")
        # print(atmosphere.array, atmosphere.priority, sep=" ")
        # print(formatv.array, formatv.priority, sep=" ")
        # print(ocassion.array, ocassion.priority, sep=" ")
        # print(language.array, language.priority, sep=" ")
        # print(minprice)
        # print(maxprice)
        #
        # # found = 0
        # # for album in self.albums:
        # #     if float(album.price) <= float(maxprice):
        # #         found = 1
        # #
        # # if found == 0:
        # #     return None
        #
        # rand = random.randrange(0, len(self.albums), 1)
        # while float(self.albums[rand].price) > float(maxprice) or float(self.albums[rand].price) < float(minprice):
        #     rand = random.randrange(0, len(self.albums), 1)

        return albums_to_return
