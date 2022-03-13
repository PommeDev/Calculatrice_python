from Resultat import *


class Calcul_Decimal:
    """Class du calcul que pour un calcul sur des nombres"""

    def __init__(self, calcul):
        for n in calcul:
            assert n == "1" or n == "2" or n == "3" or n == "4" or n == "5" or n == "6" or n == "7" or n == "8" \
                   or n == "9" or n == "0" or n == "+" or n == "-" or n == "*" or n == "/" \
                   or n == '(' or n == ')' or ",", "Le calcul ne contient pas que des chiffres et des opérateurs "

        assert est_un_chiffre(calcul[-1]) or calcul[-1] == ')', "Le  dernier nombre est un opérateur"

        self.chiffre = []
        self.operator = []
        self.entre_parentheses = []
        self.calcul = calcul

    def add_in_list_decimal(self):
        """Ajoute les nombres et les opérateurs dans leurs listes associées"""
        nb, coeff, taille, x, est_decimal, dec = 0, 1, [], 0, 0, 0
        for w in self.calcul:
            if (w == "1" or w == "2" or w == "3" or w == "4" or w == "5" or w == "6" or w == "7" or w == "8" or w == "9" \
                    or w == "0") and est_decimal == 0:
                x += 1

            elif w == ",":
                est_decimal = 1

            elif est_decimal == 1 and w == "1" or w == "2" or w == "3" or w == "4" or w == "5" or w == "6" or w == "7" or w == "8" or w == "9" \
                    or w == "0":
                dec += 1

            else:
                taille.append([x, dec])
                x, dec, est_decimal = 0, 0, 0

        taille.append([x, dec])
        x, dec, est_decimal = 0, 0, 0

        for j in range(len(taille)):
            f = taille[j][1]
            taille[j].remove(f)
            taille[j].append([ff+1 for ff in range(f)])
        for i in self.calcul:
            if (i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" \
                    or i == "0") and est_decimal == 0:
                coeff = 10 ** (taille[x][0] - 1)
                nb += int(i) * coeff
                taille[x][0] -= 1

            elif i == ",":
                est_decimal = 1
                z = 0

            elif est_decimal == 1 and i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" \
                    or i == "0":
                coeff = 10 ** -taille[x][1][z]
                nb += round(int(i) * coeff, 4)
                z += 1

            else:
                self.chiffre.append(nb)
                nb, coeff = 0, 1
                self.operator.append(i)
                x += 1
                est_decimal = 0

        self.chiffre.append(nb)



def est_un_chiffre(i: str):
    """Renvoie True si le le texte est un chiffre"""
    if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" \
            or i == "0":
        return True
    return False