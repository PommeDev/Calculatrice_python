from math import *
from Resultat import *


class Calcul:
    """Class du calcul que pour un calcul sur des nombres"""

    def __init__(self, calcul):
        for n in calcul:
            assert n == "1" or n == "2" or n == "3" or n == "4" or n == "5" or n == "6" or n == "7" or n == "8" \
                   or n == "9" or n == "0" or n == "+" or n == "-" or n == "*" or n == "/" \
                   or n == '(' or n == ')', "Le calcul ne contient pas que des chiffres et des opérateurs "

        assert est_un_chiffre(calcul[-1]) or calcul[-1] == ')', "Le  dernier nombre est un opérateur"

        self.chiffre = []
        self.operator = []
        self.entre_parentheses = []
        self.calcul = calcul

    def add_in_list(self):
        """Ajoute les nombres et les opérateurs dans leurs listes associées"""
        nb, coeff, taille, x = 0, 1, [], 0
        for w in self.calcul:
            if w == "1" or w == "2" or w == "3" or w == "4" or w == "5" or w == "6" or w == "7" or w == "8" or w == "9" \
                    or w == "0":
                x += 1
            else:
                taille.append(x)
                x = 0
        taille.append(x)
        x = 0

        for i in self.calcul:
            if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" \
                    or i == "0":
                coeff = 10 ** (taille[x] - 1)
                nb += int(i) * coeff
                taille[x] -= 1
            else:

                self.chiffre.append(nb)
                nb, coeff = 0, 1
                self.operator.append(i)
                x += 1
        self.chiffre.append(nb)


def est_un_chiffre(i: str):
    """Renvoie True si le le texte est un chiffre"""
    if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" \
            or i == "0":
        return True
    return False


