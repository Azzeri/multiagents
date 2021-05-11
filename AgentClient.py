from tkinter import ttk, StringVar, W
from ttkthemes import ThemedTk
from Album import Album

albumsArr = []
atmospheres = ["Smutna", "Lekka"]
languages = ["polski"]
ocassions = ["Relaks", "Praca"]
album = Album("Ballady", "Kat", "1989-10-10", 50, "Kompakt", 1, 1, atmospheres, languages, ocassions, 25.5)
albumsArr.append(album)
album = Album("Death By Rock And Roll", "The Pretty Reckless", "1989-10-10", 50, "Kompakt", 1, 1, atmospheres,
              languages, ocassions, 20.0)
albumsArr.append(album)
album = Album("Infestissumam", "Ghost", "1989-10-10", 50, "Kompakt", 1, 1, atmospheres, languages, ocassions, 22.3)
albumsArr.append(album)


class AgentClient:
    def __init__(self, name, agenttype):
        self.name = name
        self.agenttype = agenttype

    def init(self):
        print("Agent typu {} o nazwie {} rozpoczął działanie.".format(self.agenttype, self.name))

    @staticmethod
    def returnalbums(lengtharr, yearsarr, nationarr, atmospherearr, vocalarr, formatarr, ocassionarr, languagearr):
        def choice():
            labelchoice.config(text=var.get())

        print(lengtharr)
        print(yearsarr)
        print(nationarr)
        print(atmospherearr)
        print(vocalarr)
        print(formatarr)
        print(ocassionarr)
        print(languagearr)

        userchoice = ThemedTk(theme='arc')
        userchoice.title('Wybór albumu')
        userchoice.geometry('350x200')
        userchoice.eval('tk::PlaceWindow . center')

        labelmain = ttk.Label(userchoice, text="Wybierz", font=("Arial", 12))
        labelmain.pack()
        buttonsubmit = ttk.Button(userchoice, text="Wybieram", command=choice)
        buttonsubmit.pack()

        var = StringVar()
        for onealbum in albumsArr:
            radio = ttk.Radiobutton(userchoice, text=onealbum.name, value=onealbum.name, variable=var)
            radio.pack(anchor=W)

        labelchoice = ttk.Label(userchoice, text="", font=("Arial", 12))
        labelchoice.pack()
        userchoice.mainloop()
