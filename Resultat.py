from Calcul import *


class Result:
    def __init__(self, calcul: str):
        self.calcul = Calcul(calcul)
        self.result = 0
        self.calcul.add_in_list()

    def sum(self, a: int, b: int):
        return a + b

    def division(self, a: int, b: int):
        return round(a/b, 4)

    def root(self, a: int, b: int):
        return round(a**1/b, 4)

    def product(self, a: int, b: int):
        return round(a * b, 4)

    def soustraction(self, a: int, b: int):
        return a - b

    def Result(self):
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
