from tkinter import ttk, StringVar, W
from tkinter.ttk import Combobox

from ttkthemes import ThemedTk

from AgentClient import AgentClient


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
    arrayappend(vocalVarStates, vocalArr)
    arrayappend(formatVarStates, formatArr)
    arrayappend(ocassionVarStates, ocassionArr)
    arrayappend(languageVarStates, languageArr)

    # print(check(lengthVarStates))
    # print(check(yearsVarStates))
    # print(check(nationVarStates))
    # print(check(atmosphereVarStates))
    # print(check(vocalVarStates))
    # print(check(formatVarStates))
    # print(check(ocassionVarStates))
    # print(check(languageVarStates))

    checksum = check(lengthVarStates) + check(yearsVarStates) + check(nationVarStates) + check(
        atmosphereVarStates) + check(vocalVarStates) + check(
        formatVarStates) + check(ocassionVarStates) + check(languageVarStates)

    if checksum == 8:
        root.destroy()
        Ak1.returnalbums(lengthArr, yearsArr, nationArr, atmosphereArr, vocalArr, formatArr, ocassionArr, languageArr)
        # Ak2.returnalbums(lengthArr, yearsArr, nationArr, atmosphereArr, vocalArr, formatArr, ocassionArr, languageArr)


def createcheckboxes(titlelabel, arrvalues, arrstates):
    titlelabel = ttk.Label(root, text=titlelabel, font=("Arial", 12))
    titlelabel.pack(anchor=W)
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
root.geometry('350x1080')
# root.eval('tk::PlaceWindow . center')

lengthArr = []
values = ["Krótka", "Średnia", "Długa"]
lengthVarStates = []
createcheckboxes("Długość", values, lengthVarStates)

yearsArr = []
values = ["Starsza", "Średnia", "Nowoczesna"]
yearsVarStates = []
createcheckboxes("Lata", values, yearsVarStates)

atmosphereArr = []
values = ["Smutna", "Wesoła", "Lekka", "Ciężka", "Relaksacyjna", "Szybka", "Podniosła"]
atmosphereVarStates = []
createcheckboxes("Nastrój", values, atmosphereVarStates)

formatArr = []
values = ["Kompakt", "Winyl", "MP3"]
formatVarStates = []
createcheckboxes("Format", values, formatVarStates)

languageArr = []
values = ["polski", "angielski", "francuski", "hiszpański", "inny"]
languageVarStates = []
createcheckboxes("Język", values, languageVarStates)

nationArr = []
values = ["Polska", "Zagraniczna"]
nationVarStates = []
createcheckboxes("Nacja", values, nationVarStates)

vocalArr = []
values = ["Obecny", "Nieobecny"]
vocalVarStates = []
createcheckboxes("Wokal", values, vocalVarStates)

ocassionArr = []
values = ["Impreza", "Trening", "Praca", "Rozmowa", "Relaks"]
ocassionVarStates = []
createcheckboxes("Okazja", values, ocassionVarStates)

# combovalues = ["as", "asd", "dsf"]
#
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
