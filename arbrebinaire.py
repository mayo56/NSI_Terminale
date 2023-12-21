class ArbreBinaire:
    """
    
    """

    def __init__ (self, data, gauche=None, droite=None):
        self.data = data
        self.gauche = gauche
        self.droite = droite

    # Méthode qui permet d'afficher la valeur
    # de la racine avec la fonctin print
    def __str__ (self):
        return str(self.data)
    
    def est_vide(self):
        return self.gauche and self.droite
    
    def est_feuille(self):
        return self.est_vide()
    

ng = ArbreBinaire(9)
nd = ArbreBinaire(4)
ng = ArbreBinaire(1, ng, nd)
nd = ArbreBinaire(12)
nd = ArbreBinaire(6, ng, nd)
ngd = ArbreBinaire(3)
ng = ArbreBinaire(10, droite=ngd)
arbre = ArbreBinaire(5, ng, nd)
print("Racine:", arbre)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-


