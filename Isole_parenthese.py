from Calcul import *
from Resultat import *


def isole_parenthese(pO: Calcul):
    """ test ajouter les chiffres des parenthèse en 1er"""
    a = Calcul(pO.calcul)
    Indice_debut, Indice_fin = 0, 0
    for Ic in range(len(a.calcul)):
        if a.calcul[Ic] == "(":
            z = Ic + 1
            Indice_debut = Ic
            while a.calcul[z] != ')':
                a.entre_parentheses.append(a.calcul[z])
                z += 1
                Indice_fin = z
    a.calcul = a.calcul[0:Indice_debut] + a.calcul[Indice_fin + 1: len(a.calcul) - 1]
    txt = ""
    for c in a.entre_parentheses:
        txt += str(c)
    Pr = Result(txt)
    Pr.Result()
    return Pr.result