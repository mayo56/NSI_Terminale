# Chapitre 7: La récursivité
> La récursivité est une méthode de résolution de problèmes qui siste à décomposer le problème en sous-problèmes identiques de plus en plus petits jusqu'à obtenir un problème suffisamment petit pour qu'il puisse être résolu de manière triviale.

### Exemple:
Étant donné une liste d'entiers L=[2,12,1,8,5,10,20], calculer la somme des éléments de cette liste. Comme les listes sont **itérables**, nous pouvons simplement srésoudre ce problème avec l'un de ces algorithmes que l'on dit **itératid**:
```
Données: liste <- une liste d'entiers
fonction somme(liste)
S <- 0
n <- longueur de la liste
Pour i allant de 0 à n faire
    S <- S+liste[i]
renvoyer S
```
```
Données: liste <- une liste d'entiers
fonction somme(liste)
S <- 0
N <- longueur de la liste
Pour ichaque element de la liste faire
    S <- S + element
renvoyer S
```
Supposons maintenant que nous n'ayons pas la possibilité de faire de "boucles"

On peut alors aborder le problème sous un autre angle:

La somme des termes de cette liste est:
> 2 + (la somme des termes de [12,1,8,5,10,20])

> Soit: 2+ (12+ (la somme des termes de [1,8,5,10,20]))

> et ainsi de suite...

> jusqu'à: 2 + (12 + (1 + (5 + (10 + (la somme des termes de [20])))))

> Il est clair que: la somme des termes de [20] est 20

Au final le calcul à faire est: 2 + (12 + (1 + (5 + (10 + (20))))) = 58

Considérons alors une fonction *sommeliste(liste)* et qui revoie le résultat de la somme des éléments de la liste.

L'algorithme ci-dessous que l'on dit **récursif** réalise cette seconde approche:

```
Données: liste <- une liste d'entiers
fonction somme(liste)
Si la longueur de la liste est égale à 1 alors
    renvoyer liste[0]
Sinon
    renvoyer liste[0] + sommeliste(liste[1:])
```
### Exercice 1
Écrire en Python cette fonction, et la tester avec plusiquers exemples.