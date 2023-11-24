"""
Entrainement et Exercice 1
"""

class Cellule:
    def __init__(self, valeur: any = None, suivant:any = None) -> None:
        """
        valeur: any ou none
        suivant: cellule suivant ou none
        """
        self.valeur = valeur
        self.suivant = suivant # Si None, aucune cellule la suit
    
    def __repr__(self) -> str:
        return str(self.valeur)

class ListeC:
    def __init__(self) -> None:
        """
        """
        self.tete: Cellule | None = None
    
    def __repr__(self) -> str:
        liste = []
        
        element = self.tete
        while element != None and not self.est_vide():
            liste.append(element.valeur)
            element = element.suivant
        
        return str(liste)
    
    def est_vide(self):
        return self.tete is None

    def taille(self) -> int:
        """
        Renvoi la taille de la liste chainee
        """
        self._parcours_toute_la_chaine()[0]
    
    def get_dernier_maillon(self) -> Cellule:
        """
        Renvoi la dernière cellule
        """
        return self._parcours_toute_la_chaine()[1]
    
    def _parcours_toute_la_chaine (self, indice: int | None=None) -> list[int, Cellule]:
        """
        Methode mère pour parcourir la liste
        """
        assert not self.est_vide(), "La liste ne doit pas être vide"

        compteur = 0
        element = self.tete
        while element.suivant != None:
            if compteur == indice: # si i donnée
                return [compteur, element]
            element = element.suivant
            compteur += 1
        if compteur > indice: # Si l'indice donnée est plus grand que la liste
            return [indice, None]
        return [compteur + 1, element]

    def get_maillon_indice(self, i:int) -> Cellule:
        """
        Renvoi le maillon selon l'indice
        """
        return self._parcours_toute_la_chaine(i)[1]

    def ajout_debut(self, nM: any) -> None:
        """
        Attributs une nouvelle Cellule à la liste chainee
        """
        ma_cellule = Cellule(nM, self.tete)
        self.tete = ma_cellule

    def ajout_fin(self, nM:any) -> None:
        element = Cellule(nM, None)
        for _ in range(self.taille()):
            dernier = self.get_dernier_maillon()
            dernier.suivant = element
            element = dernier
        self.tete = element



L = ListeC()
M1, M2 = Cellule(21), Cellule(15)
M1.suivant = M2
L.tete = M1
print(L)
print(L.get_dernier_maillon())
print(L.get_maillon_indice(0))