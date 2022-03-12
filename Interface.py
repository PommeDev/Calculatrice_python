
from tkinter import *
from Resultat import *

# from Command_user import *


def add1():
    global txt
    txt += "1"


def add2():
    global txt
    txt += "2"


def add3():
    global txt
    txt += "3"


def add4():
    global txt
    txt += "4"


def add5():
    global txt
    txt += "5"


def add6():
    global txt
    txt += "6"


def add7():
    global txt
    txt += "7"


def add8():
    global txt
    txt += "8"


def add9():
    global txt
    txt += "9"


def add0():
    global txt
    txt += "0"


def addplus():
    global txt
    txt += "+"


def addmoins():
    global txt
    txt += "-"


def addfois():
    global txt
    txt += "*"


def parentheseGauche():
    global txt
    txt += "("

def parentheseDroite():
    global txt
    txt += ")"


def getEntry():
    """Affiche le contenu du champ entree"""
    print(entree.get())


def Equal():
    global txt
    b = Result(txt)
    b.affichage()


screen = Tk("Calculatrice")
screen.geometry("200x600")
screen['bg'] = 'grey'
label = Label(screen, text="Calculatrice")

label.pack()
value = StringVar()
value.set("texte par défaut")
entree = Entry(screen, textvariable=value, width=30)
entree.pack()

txt = ""


def addi0():
    global  \
        txt
    txt += "0"


buttonQuitt = Button(screen, text="Fermer", command=screen.quit)
butonPrint = Button(screen, text="Affiche ce qu'il y a d'écrit", command=getEntry)
buton0 = Button(screen, text="0", command=add0)
buton1 = Button(screen, text="1", command=add1)
buton2 = Button(screen, text="2", command=add2)
buton3 = Button(screen, text="3", command=add3)
buton4 = Button(screen, text="4", command=add4)
buton5 = Button(screen, text="5", command=add5)
buton6 = Button(screen, text="6", command=add6)
buton7 = Button(screen, text="7", command=add7)
buton8 = Button(screen, text="8", command=add8)
buton9 = Button(screen, text="9", command=add9)
butonPlus = Button(screen, text="+", command=addplus)
butonMoins = Button(screen, text="-", command=addmoins)
butonFois = Button(screen, text="x", command=addfois)
butonEqual = Button(screen, text="=", command=Equal)
buttonPG = Button(screen, text="(", command=parentheseGauche)
buttonPD = Button(screen, text=")", command=parentheseDroite)

ListeButton = [buttonQuitt, butonPrint, buton0, buton1, buton2, buton3, buton4, buton5, buton6, buton7, buton8, buton9, butonPlus, butonMoins, butonFois, buttonPG, buttonPD, butonEqual]

for Boutton in ListeButton:
    Boutton.pack()


screen.mainloop()




