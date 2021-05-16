import random

from tkinter import ttk, StringVar, W
from ttkthemes import ThemedTk
from Album import Album
from Magasine import Magasine


class AgentClient:
    def __init__(self, name):
        self.name = name

    def returnalbums(self, data_sets, maxprice, minprice, agents_seller):
        albums_to_return = []
        for agent in agents_seller:
            albums_from_seller = agent.returnalbums(data_sets)
            for album in albums_from_seller:
                albums_to_return.append(album)

        # print(length.array, length.priority, sep=" ")
        # print(years.array, years.priority, sep=" ")
        # print(nation.array, nation.priority, sep=" ")
        # print(atmosphere.array, atmosphere.priority, sep=" ")
        # print(formatv.array, formatv.priority, sep=" ")
        # print(ocassion.array, ocassion.priority, sep=" ")
        # print(language.array, language.priority, sep=" ")
        # print(minprice)
        # print(maxprice)

        # found = 0
        # for album in self.albums:
        #     if float(album.price) <= float(maxprice):
        #         found = 1
        #
        # if found == 0:
        #     return None

        # rand = random.randrange(0, len(self.albums), 1)
        # while float(self.albums[rand].price) > float(maxprice) or float(self.albums[rand].price) < float(minprice):
        #     rand = random.randrange(0, len(self.albums), 1)
        #
        # return self.albums[rand]
        return albums_to_return
