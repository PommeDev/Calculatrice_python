from Calcul import *
from Resultat import *
from Isole_parenthese import *

if __name__ == "__main__":
    c = Calcul("1+(3+3)+4-9-2+2*2")
    print(isole_parenthese(c))

    """
    b = Result(c.calcul)
    b.affichage()
    """