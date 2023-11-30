"""
Données: liste <- une liste d'entiers

fonction sommeliste(liste)
Si la longueur de la liste est égale à 1 alors
    renvoyer liste[0]
Sinon
    renvoyer liste[0] + simmeliste(liste[1:])
"""
# Récursive
def sommeliste(liste:list[int]) -> int:
    if len(liste) == 1:
        return liste[0]
    else:
        return liste[0] + sommeliste(liste[1:])

"""
Données: liste <- une liste d'entiers

fonction sommeliste(liste)
S <- 0
n <- longueur de la liste
Pour i allant de 0 à n faire
    S <- S + liste[i]
revoyer S
"""
# Non récursive
def somme(liste: list[int]) -> int:
    S = 0
    n = len(liste)
    for i in range(0,n):
        S += liste[i]
    return S

"""
Données: liste <- une liste d'entiers

fonction sommeliste(liste)
S <- 0
n <- longueur de la liste
Pour chaque element de liste faire
    S <- S + liste[i]
revoyer S
"""
def somme2(liste:list[int]) -> int:
    S = 0
    N = len(liste)
    for element in liste:
        S += element
    return S



# -=-=-=-=-=-=-=-
# Partie V
# -=-=-=-=-=-=-=-
def minimum(nombre: int, autre: int) -> int:
    if autre < nombre:
        return autre
    return nombre


# Version itérale
"""
fonction minLt
Données: L <- une liste d'entiers
Mini <- L[0]
Pour i allant de 1 à n faire
    Mini = minimum(mini, L[i])
renvoyer mini
"""
def miniLt(liste:list[int]) -> int:
    Mini = liste[0]
    for i in range(1,len(liste)):
        Mini = minimum(Mini, liste[i])
    return Mini

# Version recursive
"""
fonction miniRec
Données: L <- une liste d'entiers
Si la longueur de la lisye est égale à 1 alors
    renvoyer L[0]
Sinon 
    renvoyer minimum(L[0], miniRec(L[1:]))
"""
def miniRec(liste: list[int]) -> int:
    if len(liste) == 1:
        return liste[0]
    else:
        return minimum(liste[0], miniRec(liste[1:]))