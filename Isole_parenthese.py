from CalculBis import *
from ResultatBis import *


def isole_parenthese(pO: Calcul):
    """ test ajouter les chiffres des parenthèse en 1er"""
    a = Calcul(pO.calcul)
    Indice_debut, Indice_fin, repet = 0, 0, 0
    for Ic in range(len(a.calcul)):
        if a.calcul[Ic] == "(" and repet == 0:
            z = Ic + 1
            Indice_debut = Ic
            while a.calcul[z] != ')':
                a.entre_parentheses.append(a.calcul[z])
                z += 1
                Indice_fin = z

            repet += 1

    a.calcul = a.calcul[0:Indice_debut] + a.calcul[Indice_fin + 1: len(a.calcul)]

    txt, txt2 = "", ""
    for c in a.entre_parentheses:
        txt += str(c)
    Pr = ResultBis(txt)
    Pr.Result()
    for Membre_c in range(len(a.calcul)):
        txt2 += a.calcul[Membre_c]
        if Membre_c == Indice_debut-1:
            txt2 += str(Pr.result)
    return txt2

