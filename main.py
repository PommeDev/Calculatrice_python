from Calcul import *
from Resultat import *

if __name__ == "__main__":
    c = Calcul("1+3+3+4-9-2+2*2")
    c.add_in_list()
    print(c.operator, c.chiffre)
    b = Result(c.calcul)
    b.affichage()
