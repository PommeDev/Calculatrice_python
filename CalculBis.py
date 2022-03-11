"""Fichier la pour tricher, et pouvoir executer la fonction Isole_parenthese"""


class Calcul:
    """Class du calcul que pour un calcul sur des chiffres"""

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
        """Ajoute les chiffres et les opérateur dans leurs listes associées"""

        for i in self.calcul:
            if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" \
                    or i == "0":
                self.chiffre.append(int(i))
            else:
                self.operator.append(i)


def est_un_chiffre(i: str):
    if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" \
            or i == "0":
        return True
    return False
