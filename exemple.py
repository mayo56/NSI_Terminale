"""
Données: liste <- une liste d'entiers

fonction sommeliste(liste)
Si la longueur de la liste est égale à 1 alors
    renvoyer liste[0]
Sinon
    renvoyer liste[0] + simmeliste(liste[1:])
"""

def sommeliste(liste:list[int]) -> int:
    if len(liste) == 1:
        return liste[0]
    else:
        return liste[0] + sommeliste(liste[1:])

print(sommeliste([1,2,5,8,6,9,44,3]))