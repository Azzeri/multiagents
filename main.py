from tkinter import ttk, StringVar, W, E, N
from tkinter.ttk import Combobox

from ttkthemes import ThemedTk

from AgentClient import AgentClient


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


def submit():
    arrayappend(lengthVarStates, lengthArr)
    arrayappend(yearsVarStates, yearsArr)
    arrayappend(nationVarStates, nationArr)
    arrayappend(atmosphereVarStates, atmosphereArr)
    arrayappend(formatVarStates, formatArr)
    arrayappend(ocassionVarStates, ocassionArr)
    arrayappend(languageVarStates, languageArr)

    priors = []
    arrayappend(priorities, priors)

    ds0 = DataSet(lengthArr, priors[0])
    ds1 = DataSet(yearsArr, priors[1])
    ds2 = DataSet(nationArr, priors[2])
    ds3 = DataSet(atmosphereArr, priors[3])
    ds4 = DataSet(formatArr, priors[4])
    ds5 = DataSet(ocassionArr, priors[5])
    ds6 = DataSet(languageArr, priors[6])

    # print(check(lengthVarStates))
    # print(check(yearsVarStates))
    # print(check(nationVarStates))
    # print(check(atmosphereVarStates))
    # print(check(formatVarStates))
    # print(check(ocassionVarStates))
    # print(check(languageVarStates))

    checksum = check(lengthVarStates) + check(yearsVarStates) + check(nationVarStates) + check(
        atmosphereVarStates) + check(
        formatVarStates) + check(ocassionVarStates) + check(languageVarStates)

    if checksum == 7 and maxprice and maxprice.get().isdigit():
        root.destroy()
        Ak1.returnalbums(ds0, ds1, ds2, ds3, ds4, ds5, ds6, maxprice.get())
        # Ak2.returnalbums(lengthArr, yearsArr, nationArr, atmosphereArr, vocalArr, formatArr, ocassionArr, languageArr)


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


Ak1 = AgentClient("AK1", 'client')
Ak1.init()
Ak2 = AgentClient("AK2", 'client')
Ak2.init()

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
# createcheckboxes("Długość", values, lengthVarStates)

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
values = ["polski", "angielski", "francuski", "hiszpański", "inny"]
languageVarStates = []
createselects("Język", values, languageVarStates)

nationArr = []
values = ["Polska", "Zagraniczna"]
nationVarStates = []
createselects("Nacja", values, nationVarStates)

# vocalArr = []
# values = ["Obecny", "Nieobecny"]
# vocalVarStates = []
# createcheckboxes("Wokal", values, vocalVarStates)

ocassionArr = []
values = ["Impreza", "Trening", "Praca", "Rozmowa", "Relaks"]
ocassionVarStates = []
createcheckboxes("Okazja", values, ocassionVarStates)

maxprice = StringVar()
pricetitlelabel = ttk.Label(root, text="Max cena", font=("Arial", 12))
pricetitlelabel.pack(anchor=W)
maxpriceinput = ttk.Entry(root, textvariable=maxprice)
maxpriceinput.pack(anchor=W)

# combovalues = ["as", "asd", "dsf"]
# combo1 = Combobox(root)
# combo1['values'] = combovalues
# combo1.pack(anchor=W)
# combo2 = Combobox(root)
# combo2['values'] = combovalues
# combo2.pack(anchor=W)
# combo3 = Combobox(root)
# combo3['values'] = combovalues
# combo3.pack(anchor=W)

# titlelabel3 = ttk.Label(root, text='Priorytet 3').pack(anchor=W)
# titlelabel2 = ttk.Label(root, text='Priorytet 2').pack(anchor=W)
# titlelabel1 = ttk.Label(root, text='Priorytet 1').pack(anchor=W)
# titlelabel4 = ttk.Label(root, text='Priorytet 4').pack(anchor=W)
# titlelabel5 = ttk.Label(root, text='Priorytet 5').pack(anchor=W)
# titlelabel6 = ttk.Label(root, text='Priorytet 6').pack(anchor=W)
# titlelabel7 = ttk.Label(root, text='Priorytet 7').pack(anchor=W)
# titlelabel8 = ttk.Label(root, text='Priorytet 8').pack(anchor=W)

buttonSubmit = ttk.Button(root, text="Dalej", command=submit).pack()

root.mainloop()
