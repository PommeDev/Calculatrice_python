
from tkinter import *
from ResultatDecimal import *


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


def addpuiss():
    """Ajoute ^ a la variable txt"""
    global txt
    txt += "^"
    global aff
    aff.set(txt)


def addRacine():
    """Ajoute √ a la variable txt"""
    global txt
    txt += "√"
    global aff
    aff.set(txt)


def Equal():
    """Calcul le résultat et remplace txt par ce résultat, l'affiche aussi"""
    global txt
    b = Result(txt)
    global aff
    b.Result()
    txt = str(b.result)
    aff.set(str(b.calcul.calcul) + " = " + txt)


def Clear():
    """Vide txt"""
    global txt
    txt = ""
    global aff
    aff.set(txt)


def addVirgule():
    global txt
    txt += "."
    global aff
    aff.set(txt)


def addDivide():
    global txt
    txt += "/"
    global aff
    aff.set(txt)


def del_last_elem():
    """Cette fonction supprime le dernier élement de txt"""
    global txt
    global aff
    txtBis = ""
    if txt != "":
        for i in range(len(txt)-1):
            txtBis += txt[i]
        txt = txtBis
    aff.set(txt)


"""--II/ Création de la fenetre--"""

screen = Tk()
screen.title("Calculatrice")
screen['bg'] = 'grey'
screen.geometry("292x281")
screen.iconbitmap('calculatrice.ico')
screen.resizable(False, False)
label = Label(screen, text="-- Calculatrice, by Pomme --", background="green")
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
buttonVirgule = Button(screen, text=",", command=addVirgule)
buttonDivide = Button(screen, text="/", command=addDivide)

buttonDel = Button(screen, text="<-", command=del_last_elem)
buttonPuiss = Button(screen, text="^", command=addpuiss)
buttonRacine = Button(screen, text="√", command=addRacine)


aff = StringVar()
affichage = Label(screen, textvariable=aff, width=40, justify='left')

ListeButton = [buttonQuitt, butonClear, buton0, buton1, buton2, buton3, buton4, buton5, buton6, buton7, buton8, buton9, butonPlus, butonMoins, butonFois, buttonPG, buttonPD, butonEqual]

"""--VI/ Définition de la position des boutons--"""

"""---A) clavier des chiffres---"""
affichage.grid(row=2, column=0, padx=0, pady=5, ipady=5, columnspan=5)
buton9.grid(row=3, column=2, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton8.grid(row=3, column=1, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton7.grid(row=3, column=0, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton6.grid(row=4, column=2, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton5.grid(row=4, column=1, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton4.grid(row=4, column=0, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton3.grid(row=5, column=2, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton2.grid(row=5, column=1, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buton1.grid(row=5, column=0, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
butonEqual.grid(row=7, column=2, ipadx=60, padx=0, ipady=5, sticky=W+N+E, columnspan=3, rowspan=1)
buttonDel.grid(row=6, column=2, ipadx=20, padx=0, ipady=10, sticky=W+N+E, columnspan=1, rowspan=1)
buton0.grid(row=6, column=1, ipadx=20, padx=0, ipady=10, sticky=W+N+E, columnspan=1)
butonClear.grid(row=7, column=1, ipadx=20, padx=0, ipady=5, sticky=W+N+E)


"""---B) Clavier des Opérateurs---"""
butonPlus.grid(row=3, column=3, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
butonMoins.grid(row=3, column=4, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
butonFois.grid(row=4, column=3, ipadx=19, padx=0, ipady=10, sticky=W+N+E)
buttonPD.grid(row=6, column=4, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buttonPG.grid(row=6, column=3, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buttonVirgule.grid(row=6, column=0, ipadx=20, padx=0, ipady=10, sticky=W+N+E, columnspan=1, rowspan=1)
buttonDivide.grid(row=4, column=4, ipadx=20, padx=0, ipady=10, sticky=W+N+E, columnspan=1, rowspan=1)
buttonPuiss.grid(row=5, column=3, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
buttonRacine.grid(row=5, column=4, ipadx=20, padx=0, ipady=10, sticky=W+N+E)
"""--V/ Pouvoir utilisé les touche du clavier pour taper le calcul--"""

"""---A) definition des fonctions"""


def clavier1(event):
    """Ajoute 1 a la variable txt quand la touche "1" est pressé"""
    global txt
    txt += "1"
    global aff
    aff.set(txt)


def clavier2(event):
    """Ajoute 2 a la variable txt quand la touche "2" est pressé"""
    global txt
    txt += "2"
    global aff
    aff.set(txt)


def clavier3(event):
    """Ajoute 3 a la variable txt quand la touche "3" est pressé"""
    global txt
    txt += "3"
    global aff
    aff.set(txt)


def clavier4(event):
    """Ajoute 4 a la variable txt quand la touche "4" est pressé"""
    global txt
    txt += "4"
    global aff
    aff.set(txt)


def clavier5(event):
    """Ajoute 5 a la variable txt quand la touche "5" est pressé"""
    global txt
    txt += "5"
    global aff
    aff.set(txt)


def clavier6(event):
    """Ajoute 6 a la variable txt quand la touche "6" est pressé"""
    global txt
    txt += "6"
    global aff
    aff.set(txt)


def clavier7(event):
    """Ajoute 7 a la variable txt quand la touche "7" est pressé"""
    global txt
    txt += "7"
    global aff
    aff.set(txt)


def clavier8(event):
    """Ajoute 8 a la variable txt quand la touche "8" est pressé"""
    global txt
    txt += "8"
    global aff
    aff.set(txt)


def clavier9(event):
    """Ajoute 9 a la variable txt quand la touche "9" est pressé"""
    global txt
    txt += "9"
    global aff
    aff.set(txt)


def clavier0(event):
    """Ajoute 0 a la variable txt quand la touche "0" est pressé"""
    global txt
    txt += "0"
    global aff
    aff.set(txt)


def clavierPlus(event):
    """Ajoute + a la variable txt quand la touche "+" est pressé"""
    global txt
    txt += "+"
    global aff
    aff.set(txt)


def clavierMoins(event):
    """Ajoute - a la variable txt quand la touche "-" est pressé"""
    global txt
    txt += "-"
    global aff
    aff.set(txt)


def clavierFois(event):
    """Ajoute * a la variable txt quand la touche "*" est pressé"""
    global txt
    txt += "*"
    global aff
    aff.set(txt)


def clavierDivide(event):
    """Ajoute / a la variable txt quand la touche "/" est pressé"""
    global txt
    txt += "/"
    global aff
    aff.set(txt)


def clavierVirgule(event):
    """Ajoute . a la variable txt quand la touche "." est pressé"""
    global txt
    txt += "."
    global aff
    aff.set(txt)


def clavier_del_last_elem(elem):
    """Cette fonction supprime le dernier élement de txt quand la touche "" est pressé """
    global txt
    global aff
    txtBis = ""
    if txt != "":
        for i in range(len(txt)-1):
            txtBis += txt[i]
        txt = txtBis
    aff.set(txt)


def clavierEqual(event):
    """Calcul le résultat et remplace txt par ce résultat, l'affiche aussi quand la touche entrée est préssée"""
    global txt
    b = Result(txt)
    global aff
    b.Result()
    txt = str(b.result)
    aff.set(str(b.calcul.calcul) + " = " + txt)


def clavierPuissance(event):
    """Ajoute ^ a la variable txt quand la touche "^" est pressée"""
    global txt
    txt += "^"
    global aff
    aff.set(txt)


"""---B) Definition des touches"""

screen.bind("0", clavier0)
screen.bind("1", clavier1)
screen.bind("2", clavier2)
screen.bind("3", clavier3)
screen.bind("4", clavier4)
screen.bind("5", clavier5)
screen.bind("6", clavier6)
screen.bind("7", clavier7)
screen.bind("8", clavier8)
screen.bind("9", clavier9)
screen.bind("+", clavierPlus)
screen.bind("-", clavierMoins)
screen.bind("*", clavierFois)
screen.bind("/", clavierDivide)
screen.bind(".", clavierVirgule)
screen.bind("<Return>", clavierEqual)
screen.bind("<BackSpace>", clavier_del_last_elem)
screen.bind("<ccedilla>", clavierPuissance)


screen.mainloop()




