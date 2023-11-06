"""
Author: Maxence Le Roy
Devoir maison: Pile et Changement de base
À faire pour le: 07/11/23
"""

def decToBin(n:int) -> str:
    """
    Fonction permettant de transformer n nombre décimal en nombre binaire.
    n: int (positif)
    return: str
    """
    assert isinstance(n, int), "n doit être un entier."
    assert n > 0, "n doit être positif."

    # Si c'est 0, alors en binaire c'est pareil
    if n == 0:
        return "0"
    
    binaire = [] # Notre pile

    while n > 0:
        binaire.append(n % 2) # Reste de la division par 2
        n //= 2 # On divise également n

    # On inverse la lecture du résultat
    strBinaire = ""
    for _ in range(len(binaire)):
        strBinaire += str(binaire.pop())
    
    return strBinaire
    

def baseConverter(n:int, b:int) -> str:
    """
    Foction qui permet de transformer n'importe quel nombre entier positif dans une base compris entre 2 et 16.
    n: int (positif)
    b: int (entre 2 et 16)
    return: str
    """
    assert isinstance(n, int) and isinstance(b, int), "Les paramètres n et b doivent être des entiers."
    assert n > 0, "n doit être positif."
    assert 2 <= b <= 16, "Le paramètre b doit être comprit entre 2 et 16."

    # Peu importe la base, 0 vaut 0.
    if n == 0:
        return "0"
    
    nombre_convertit = [] # Notre pile

    while n > 0:
        nombre_convertit.append(n % b) # On divise n par b
        n //= b # On divise également n par b
    
    # On inverse la lecture du choix et adaptons les nombres selon la base
    strBase = ""
    lettres = ["A", "B", "C", "D", "E", "F"] # Le lettres pour les base au dessus de 10
    for _ in range(len(nombre_convertit)):
        nombre = nombre_convertit.pop()

        # Si le nombre au dessus de 9 et convertit dans une base supérieur à 10
        if nombre > 9 and b > 10:
            nombre = lettres[nombre - 10] # On récupère la lettre adéquat
        strBase += str(nombre)

    return strBase


# --------------------------------
#           TEST ZONE
# --------------------------------
#
print("Decimal en Binaire:", decToBin(77))
print("Decimal en n'importe quel base:", baseConverter(255, 16))
#
# --------------------------------