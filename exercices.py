# -=-=-=-=-=-=-=-=-
#     Exercice 2
# -=-=-=-=-=-=-=-=-
from timeit import default_timer as timer
from random import randint

from exemple import somme, somme2, sommeliste

L = [randint(0,100) for i in range(500)]

# debut = timer()
# print(sommeliste(L))
# fin = timer()
# print("SommeListe:", fin - debut) # Bat des records de temps huhu

# debut = timer()
# print(somme(L))
# fin = timer()
# print("Somme:", fin - debut)

# debut = timer()
# print(somme2(L))
# fin = timer()
# print("Somme2:", fin - debut)

# -=-=-=-=-=-=-=-=-
#    Exercice 3
# -=-=-=-=-=-=-=-=-
from exemple import miniLt, miniRec

# debut = timer()
# print(miniLt(L))
# fin = timer()
# print("MiniLt:", fin - debut)

# debut = timer()
# print(miniRec(L))
# fin = timer()
# print("MiniRec:", fin - debut)


# -=-=-=-=-=-=-=-
#   Exercice 4
# -=-=-=-=-=-=-=-

# Renvoyer le maximum dans une liste
def maximum(nombre, autre) -> int:
    if autre < nombre:
        return autre
    return nombre

# Itérable
def maxLt(liste: list[int]) -> int:
    S = liste[0]
    for i in range(1, len(liste)):
        S = maximum(S, liste[i])
    return S

# Récursive
def maxRec(liste: list[int]) -> int:
    if len(liste) == 1:
        return liste[0] 
    else:
        return maximum(liste[0], maxRec(liste[1:]))

# debut = timer()
# print(maxLt(L))
# fin = timer()
# print("maxLt:", fin - debut)

# debut = timer()
# print(maxRec(L))
# fin = timer()
# print("maxRec:", fin - debut)


# -=-=-=-=-=-=-=-=-=-
#     Exercice 5
# -=-=-=-=-=-=-=-=-=-

# Calcul x^n où n € N et x € R
def puissance(x, nombre) -> int:
    return nombre * x

# iterable
def puissanceLt(x, n):
    puiss = x
    if n == 1:
        return x
    for _ in range(n - 1):
        puiss *= x
    return puiss

# recursive (lé pas jolie)
def puissanceRec(nombre, x, n, first):
    if n == 1 and first:
        return nombre
    elif n == 1 and not first:
        return nombre * x
    else:
        if first:
            n -= 1
        return puissanceRec(puissance(x, nombre), x, n-1, False)


# x = randint(1,100)
# n = randint(1,100)

# print(x, n)
# debut = timer()
# print(puissanceLt(x, n))
# fin = timer()
# print("puissanceLt:", fin - debut)

# debut = timer()
# print(puissanceRec(x, x,n, True))
# fin = timer()
# print("puissanceRec:", fin - debut)


# -=-=-=-=-=-=-=-=-=-=-
#      Exercice 6
# -=-=-=-=-=-=-=-=-=-=-