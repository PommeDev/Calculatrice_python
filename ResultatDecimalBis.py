from Calcul_decimalBis import *
from Isole_parentheseDecimal import *


class Result:
    """Classe qui donne le résultat en fonction d'un objet calcul"""
    def __init__(self, calcul: str):
        self.calcul = Calcul_Decimal(calcul)
        self.result = 0

        for i in self.calcul.calcul:
            if i == "(":
                self.calcul = Calcul_Decimal(isole_parenthese(self.calcul))
        self.calcul.add_in_list_decimal()

    def sum(self, a: int, b: int):
        """Effectue une somme sur 2 nombres"""
        return a + b

    def division(self, a: int, b: int):
        """effectue une division entre 2 nombre et arrondi à 4 decimals"""
        return round(a/b, 4)

    def root(self, a: int, b: int):
        """effectue la racine nième de a et arrondi à 4 decimals"""
        c = 1/b
        return round(a**c, 4)

    def product(self, a: int, b: int):
        """effectue le produit entre 2 nombres"""
        return round(a * b, 4)

    def soustraction(self, a: int, b: int):
        """effectue la soustraction entre 2 nombre"""
        return a - b

    def puissance(self, a: int, b: int):
        """Met le chiffre a à la puissance b"""
        return round(a ** b, 4)

    def Result(self):
        """Donne le résultat de la suite de calcul"""
        tour = 1
        if len(self.calcul.chiffre) > 2:
            for i in self.calcul.operator:
                if len(self.calcul.chiffre) > 2:
                    if i == "+" and tour == 1:
                        self.result += self.sum(self.calcul.chiffre[0], self.calcul.chiffre[1])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        tour += 1

                    elif i == "-" and tour == 1:
                        self.result += self.soustraction(self.calcul.chiffre[0], self.calcul.chiffre[1])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])

                        tour += 1
                    elif i == "/" and tour == 1:
                        self.result += self.division(self.calcul.chiffre[0], self.calcul.chiffre[1])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        tour += 1

                    elif i == "*" and tour == 1:
                        self.result += self.product(self.calcul.chiffre[0], self.calcul.chiffre[1])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        tour += 1

                    elif i == "^" and tour == 1:
                        self.result += self.puissance(self.calcul.chiffre[0], self.calcul.chiffre[1])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        tour += 1

                    elif i == "√" and tour == 1:
                        self.result += self.root(self.calcul.chiffre[0], self.calcul.chiffre[1])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
                        tour += 1

                elif tour > 1:
                    if i == "+":
                        self.result = self.sum(self.result, self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])

                    elif i == "-":
                        self.result = self.soustraction(self.result, self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])

                    elif i == "*":
                        self.result = self.product(self.result, self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])

                    elif i == "/":
                        self.result = self.division(self.result, self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])

                    elif i == "^":
                        self.result = self.puissance(self.result, self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])

                    elif i == "√":
                        self.result = self.root(self.result, self.calcul.chiffre[0])
                        self.calcul.chiffre.remove(self.calcul.chiffre[0])
        else:
            x = self.calcul.operator[0]
            if x == "+":
                self.result += self.sum(self.calcul.chiffre[0], self.calcul.chiffre[1])
            elif x == "-":
                self.result += self.soustraction(self.calcul.chiffre[0], self.calcul.chiffre[1])
            elif x == "/":
                self.result += self.division(self.calcul.chiffre[0], self.calcul.chiffre[1])
            elif x == "*":
                self.result += self.product(self.calcul.chiffre[0], self.calcul.chiffre[1])
            elif x == "^":
                self.result += self.puissance(self.calcul.chiffre[0], self.calcul.chiffre[1])
            elif x == "√":
                self.result += self.root(self.calcul.chiffre[0], self.calcul.chiffre[1])

    def affichage(self):
        self.Result()
        print(f"Le résultat est: {self.result}")
