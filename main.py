from tkinter import ttk, StringVar, W, E, N, END
from ttkthemes import ThemedTk
from AgentClient import AgentClient
from AgentSeller import AgentSeller
from Magasine import Magasine
import copy

class DataSet:
    def __init__(self, array, priority):
        self.array = array
        self.priority = priority


def arrayappend(arrayfrom, arrayto):
    arrayto.clear()
    for j in arrayfrom:
        if j.get() and j.get() != '0':
            arrayto.append(j.get())


def check(array):
    for j in array:
        if j.get():
            return 1
    return 0


def gui_user_choice(albums_to_display):
    def choice():
        labelchoice.config(text=var.get())

    root.destroy()
    userchoice = ThemedTk(theme='arc')
    userchoice.title('Wybór albumu')
    userchoice.geometry('350x200')
    userchoice.eval('tk::PlaceWindow . center')

    labelmain = ttk.Label(userchoice, text="Wybierz", font=("Arial", 12))
    labelmain.pack()
    buttonsubmit = ttk.Button(userchoice, text="Wybieram", command=choice)
    buttonsubmit.pack()

    var = StringVar()
    for onealbum in albums_to_display:
        label = "{} {}zł".format(onealbum.name, round(onealbum.price, 2))
        radio = ttk.Radiobutton(userchoice, text=label, value=onealbum.name, variable=var)
        radio.pack(anchor=W)

    labelchoice = ttk.Label(userchoice, text="", font=("Arial", 12))
    labelchoice.pack()
    userchoice.mainloop()


def submit():
    # Data Validation
    checksum = check(atmosphereVarStates) + check(ocassionVarStates)
    if checksum == 2 and maxprice and maxprice.get().isdigit() and minprice and minprice.get().isdigit() \
            and nosellers.get().isdigit():

        main_magasine = Magasine("main")
        agents_client = []
        agents_seller = []
        priors = []

        # Create agents
        for i in range(int(nosellers.get())):
            agents_client.append(AgentClient("AK" + str(i + 1)))
            agents_seller.append(AgentSeller("AS" + str(i + 1)))

        # Fill agents with albums from main magasine
        for agent in agents_seller:
            agent.take_albums_from_magasine(main_magasine)

        # Create data for agents
        arrayappend(lengthVarStates, lengthArr)
        arrayappend(yearsVarStates, yearsArr)
        arrayappend(nationVarStates, nationArr)
        arrayappend(atmosphereVarStates, atmosphereArr)
        arrayappend(formatVarStates, formatArr)
        arrayappend(ocassionVarStates, ocassionArr)
        arrayappend(languageVarStates, languageArr)
        arrayappend(priorities, priors)

        data_sets = [DataSet(lengthArr, priors[0]), DataSet(yearsArr, priors[1]), DataSet(nationArr, priors[2]),
                     DataSet(atmosphereArr, priors[3]), DataSet(formatArr, priors[4]), DataSet(ocassionArr, priors[5]),
                     DataSet(languageArr, priors[6])]

        # Return albums from sellers via client agents to user
        albums_returned = []
        for agent in agents_client:
            albums_from_agent = agent.returnalbums(data_sets, maxprice.get(), minprice.get(), agents_seller)
            for album in albums_from_agent:
                albums_returned.append(album)

        # Return albums without repeats
        albums_returned_merged = []
        found = 0
        for album in albums_returned:
            for album_m in albums_returned_merged:
                if album_m.name == album.name and album_m.albumformat == album.albumformat and album is not None:
                    found = 1
            if found == 0:
                albums_returned_merged.append(album)
                found = 0
            # elif found == 1:
            #     if album_copy.price < album.price:
            #         albums_returned_merged.append(album_copy)
            #     else:
            #         albums_returned_merged.append(album)
            #     found = 0

        # Display choice window
        gui_user_choice(albums_returned_merged)


def createheader(titlelabel):
    titlelabel = ttk.Label(root, text=titlelabel, font=("Arial", 12))
    titlelabel.pack(anchor=W)
    varstate = StringVar()
    select = ttk.Combobox(root, width=10, textvariable=varstate, values=prioritiesArr)
    select.pack(anchor=E)
    priorities.append(varstate)
    select.current(1)


def createselects(titlelabel, arrvalues, arrstates):
    createheader(titlelabel)
    varstate = StringVar()
    select = ttk.Combobox(root, width=27, textvariable=varstate, values=arrvalues)
    select.pack(anchor=W)
    arrstates.append(varstate)
    select.current(0)


def createcheckboxes(titlelabel, arrvalues, arrstates):
    createheader(titlelabel)
    index = 0

    for _ in arrvalues:
        varstate = StringVar()
        checkbox = ttk.Checkbutton(root, text=arrvalues[index], variable=varstate, onvalue=arrvalues[index])
        checkbox.pack(anchor=W)
        arrstates.append(varstate)
        index += 1


root = ThemedTk(theme='arc')
root.title('Doradca muzyczny')
root.geometry('350x900')
# root.eval('tk::PlaceWindow . center')

prioritiesArr = ["Wysoki", "Średni", "Niski"]
priorities = []
lengthArr = []
values = ["Krótka", "Średnia", "Długa"]
lengthVarStates = []
createselects("Długość", values, lengthVarStates)

yearsArr = []
values = ["Starsza", "Średnia", "Nowoczesna"]
yearsVarStates = []
createselects("Lata", values, yearsVarStates)

atmosphereArr = []
values = ["Smutna", "Wesoła", "Lekka", "Ciężka", "Relaksacyjna", "Szybka", "Podniosła"]
atmosphereVarStates = []
createcheckboxes("Nastrój", values, atmosphereVarStates)

formatArr = []
values = ["Kompakt", "Winyl", "MP3"]
formatVarStates = []
createselects("Format", values, formatVarStates)

languageArr = []
values = ["polski", "angielski", "inny"]
languageVarStates = []
createselects("Język", values, languageVarStates)

nationArr = []
values = ["Polska", "Zagraniczna"]
nationVarStates = []
createselects("Nacja", values, nationVarStates)

ocassionArr = []
values = ["Impreza", "Trening", "Praca", "Rozmowa", "Relaks"]
ocassionVarStates = []
createcheckboxes("Okazja", values, ocassionVarStates)

minprice = StringVar()
pricetitlelabel = ttk.Label(root, text="Min cena", font=("Arial", 12))
pricetitlelabel.pack(anchor=W)
minpriceinput = ttk.Entry(root, textvariable=minprice)
minpriceinput.pack(anchor=W)
minpriceinput.insert(END, '10')

maxprice = StringVar()
pricetitlelabel = ttk.Label(root, text="Max cena", font=("Arial", 12))
pricetitlelabel.pack(anchor=W)
maxpriceinput = ttk.Entry(root, textvariable=maxprice)
maxpriceinput.pack(anchor=W)
maxpriceinput.insert(END, '30')

nosellers = StringVar()
nosellerstitlelabel = ttk.Label(root, text="Liczba sprzedawców", font=("Arial", 12))
nosellerstitlelabel.pack(anchor=W)
nosellersinput = ttk.Entry(root, textvariable=nosellers)
nosellersinput.pack(anchor=W)
nosellersinput.insert(END, '3')

buttonSubmit = ttk.Button(root, text="Dalej", command=submit).pack()

root.mainloop()
