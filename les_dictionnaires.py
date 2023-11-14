# Exo 3

zoo_Beauval = {
    "éléphant": ("Asie", 5),
    "écureuil": ("Asie", 17),
    "panda": ("Asie", 2),
    "hippopotame": ("Afrique", 7),
    "girafe": ("Afrique", 4),
}

zoo_LaFleche = {
    "ours": ("Europe", 4),
    "tigre": ("Asie", 7),
    "girafe": ("Afrique", 11),
    "hippopotame": ("Afrique", 3),
}

def plus_grand_nombre(zoo: dict) -> str:
    """
    Fonction qui renvoie l'animal qui est en plus grand nombre.
    zoo: dict
    return: str
    """
    le_plus = ()
    for (key, value) in zoo.items():
        if le_plus == ():
            le_plus = (key, value)
        else:
            if le_plus[1][1] < value[1]:
                le_plus = (key, value)
        print(le_plus)
    return le_plus[0]

assert plus_grand_nombre(zoo_LaFleche) == "girafe"
assert plus_grand_nombre(zoo_Beauval) == 'écureuil'

# ---------------------------

def nombre_total (zoo:dict, continent:str) -> int:
    """
    Fonction qui renvoie le nombre total d'animaux selon son continent.
    zoo: dict
    continent: str
    return: int
    """
    total = 0
    for value in zoo.values():
        if value[0] == continent:
            total += value[1]
    return total

assert nombre_total(zoo_LaFleche, 'Afrique') == 14
assert nombre_total(zoo_Beauval, 'Asie') == 24