
from tkinter import *
from Resultat import *


"""--I/ Les fonction utilisées par les bouton--"""


def add1():
    """Ajoute 1 a la variable txt"""
    global txt
    txt += "1"
    global aff
    aff.set(txt)


def add2():
    """Ajoute 2 a la variable txt"""
    global txt
    txt += "2"
    global aff
    aff.set(txt)


def add3():
    """Ajoute 3 a la variable txt"""
    global txt
    txt += "3"
    global aff
    aff.set(txt)


def add4():
    """Ajoute 4 a la variable txt"""
    global txt
    txt += "4"
    global aff
    aff.set(txt)


def add5():
    """Ajoute 5 a la variable txt"""
    global txt
    txt += "5"
    global aff
    aff.set(txt)


def add6():
    """Ajoute 6 a la variable txt"""
    global txt
    txt += "6"
    global aff
    aff.set(txt)


def add7():
    """Ajoute 7 a la variable txt"""
    global txt
    txt += "7"
    global aff
    aff.set(txt)


def add8():
    """Ajoute 8 a la variable txt"""
    global txt
    txt += "8"
    global aff
    aff.set(txt)


def add9():
    """Ajoute 9 a la variable txt"""
    global txt
    txt += "9"
    global aff
    aff.set(txt)


def add0():
    """Ajoute 0 a la variable txt"""
    global txt
    txt += "0"
    global aff
    aff.set(txt)


def addplus():
    """Ajoute + a la variable txt"""
    global txt
    txt += "+"
    global aff
    aff.set(txt)


def addmoins():
    """Ajoute - a la variable txt"""
    global txt
    txt += "-"
    global aff
    aff.set(txt)


def addfois():
    """Ajoute * a la variable txt"""
    global txt
    txt += "*"
    global aff
    aff.set(txt)


def parentheseGauche():
    """Ajoute ( a la variable txt"""
    global txt
    txt += "("
    global aff
    aff.set(txt)


def parentheseDroite():
    """Ajoute ) a la variable txt"""
    global txt
    txt += ")"
    global aff
    aff.set(txt)


def Equal():
    """Calcul le résultat et remplace txt par ce résultat, l'affiche aussi"""
    global txt
    b = Result(txt)
    global aff
    b.Result()
    txt = str(b.result)
    aff.set(txt)


def Clear():
    """Vide txt"""
    global txt
    txt = ""
    global aff
    aff.set(txt)


"""--II/ Création de la fenetre--"""

screen = Tk()
screen.title("Calculatrice")
screen['bg'] = 'grey'
screen.geometry("231x281")
screen.iconbitmap('calculatrice.ico')
label = Label(screen, text="Calculatrice, by Pomme", background="green")
label.grid(row=0, column=0, columnspan=4)


txt = ""  # La variable qui contient le calcul voulut par l'utilisateur

"""--III/ Création des boutons--"""

buttonQuitt = Button(screen, text="Fermer", command=screen.quit)
butonClear = Button(screen, text="C", command=Clear)
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
butonEqual = Button(screen, text="=", command=Equal, background='yellow')
buttonPG = Button(screen, text="(", command=parentheseGauche)
buttonPD = Button(screen, text=")", command=parentheseDroite)


aff = StringVar()
affichage = Label(screen, textvariable=aff, width=20, justify='left')

ListeButton = [buttonQuitt, butonClear, buton0, buton1, buton2, buton3, buton4, buton5, buton6, buton7, buton8, buton9, butonPlus, butonMoins, butonFois, buttonPG, buttonPD, butonEqual]

"""--VI/ Définition de la position des boutons--"""

"""---A) clavier des chiffres---"""
affichage.grid(row=2, column=0, padx=0, pady=5, ipady=5, columnspan=4)
buton9.grid(row=3, column=2, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton8.grid(row=3, column=1, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton7.grid(row=3, column=0, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton6.grid(row=4, column=2, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton5.grid(row=4, column=1, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton4.grid(row=4, column=0, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton3.grid(row=5, column=2, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton2.grid(row=5, column=1, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton1.grid(row=5, column=0, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
butonEqual.grid(row=6, column=2, ipadx=39, padx=0, ipady=28, sticky=W+N+E, columnspan=2, rowspan=2)
buton0.grid(row=6, column=1, ipadx=20, padx=0, ipady=10, sticky=W+N+E, columnspan=1)
butonClear.grid(row=6, column=0, ipadx=20, padx=0, ipady=10, sticky=W+N+E)

"""---B) Clavier des Opérateurs---"""
butonPlus.grid(row=3, column=3, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
butonMoins.grid(row=4, column=3, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
butonFois.grid(row=5, column=3, ipadx=19, padx=0, ipady=10, sticky=W+N+E)
buttonPD.grid(row=7, column=1, ipadx=20, padx=0, ipady=5, sticky=W+N+E)
buttonPG.grid(row=7, column=0, ipadx=20, padx=0, ipady=5, sticky=W+N+E)


screen.mainloop()




