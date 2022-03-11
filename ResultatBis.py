from CalculBis import *


class ResultBis:
    """Classe qui donne le résultat en fonction d'un objet calcul"""
    def __init__(self, calcul: str):
        self.calcul = Calcul(calcul)
        self.result = 0
        self.calcul.add_in_list()

    def sum(self, a: int, b: int):
        """Effectue une somme sur 2 nombres"""
        return a + b

    def division(self, a: int, b: int):
        """effectue une division entre 2 nombre et arrondi à 4 decimals"""
        return round(a/b, 4)

    def root(self, a: int, b: int):
        """effectue la racine nième de a et arrondi à 4 decimals"""
        return round(a**1/b, 4)

    def product(self, a: int, b: int):
        """effectue le produit entre 2 nombres"""
        return round(a * b, 4)

    def soustraction(self, a: int, b: int):
        """effectue la soustraction entre 2 nombre"""
        return a - b

    def Result(self):
        """Donne le résultat de la suite de calcul"""
        tour = 1
        for i in self.calcul.operator:
            if tour == 1:
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

    def affichage(self):
        self.Result()
        print(f"Le résultat est: {self.result}")
