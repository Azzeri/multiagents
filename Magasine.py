from Album import Album


class Magasine:
    def __init__(self, name):
        self.name = name
        self.albums = [Album("Ballady", "Kat", "1989-10-10", 50, "Kompakt", 1, 1, ["Smutna", "Lekka"], [], [], 25.5),
                       ]
