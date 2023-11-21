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
        assert not self.est_vide(), "La liste ne doit pas être vide"

        compteur = 1
        element = self.tete
        while element.suivant != None:
            element = element.suivant
            compteur += 1
        return compteur
    
    def get_dernier_maillon(self) -> Cellule:
        assert not self.est_vide(), "La liste ne doit pas être vide."

        element = self.tete
        while element.suivant != None:
            element = element.suivant
        return element

L = ListeC()
M1, M2 = Cellule(21), Cellule(15)
M1.suivant = M2
L.tete = M1
print(L)
print(L.get_dernier_maillon())