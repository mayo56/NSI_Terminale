
def recherche_indices_classement(elt:int, tab:list):
    inf = []
    egal = []
    supp = []

    for i in range(len(tab)):
        if elt > tab[i]:
            inf.append(i)
        elif elt < tab[i]:
            supp.append(i)
        else:
            egal.append(i)
    return (inf, egal, supp)

print(recherche_indices_classement(3,[1, 3, 4, 2, 4, 6, 3, 0]))

def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire
    resultats. Si nom n'est pas dans le dictionnaire,
    la fonction renvoie None.'''
    if nom in resultats:
        notes = resultats[nom]
        if not len(notes): # pas de notes
            return 0
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round( total_points / total_coefficients, 1 )
    else:
        return None

resultat = {
    'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [13, 4],
        'PROJET1': [16, 3],
        'DS3': [14, 4]
    },
    'Durand': {
        'DS1': [6 , 4],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [12, 4]
    }
}

print(moyenne('Durand', resultat))