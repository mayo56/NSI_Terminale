# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:09:09 2024

@author: resptechno
"""
import sqlite3
import csv
bdd = sqlite3.connect("dis_db.db")
curseur = bdd.cursor()


# Creation table Communes
requete = """
CREATE TABLE IF NOT EXISTS Communes
(
    IdCommune INTEGER  PRIMARY KEY AUTOINCREMENT UNIQUE,
    inseecommune TEXT,
    nomcommune TEXT,
    quartier TEXT,
    cdreseau TEXT,
    nomreseau TEXT,
    debutalim DATE
);"""
curseur.execute(requete)



# On enregistre les changements !

bdd.commit()

#On rempli la table
with open('DIS_COM_UDI_2023_V2.txt', newline='') as csvfile:
    nb_lignes = 0
    lignes = csv.reader(csvfile)
    entete = True
    for l in lignes:
        if entete:
            entete = False
            print(entete)
        else:
            nb_lignes += 1
            requete = """
            INSERT INTO Communes
                (inseecommune,nomcommune,quartier,cdreseau,nomreseau,debutalim)
            VALUES
                (?, ?, ?, ?, ?, ?)
            """
            curseur.execute(requete, l)
    bdd.commit()
    print(f"{nb_lignes} enregistrements créés")




#On cloture les objets
curseur.close()
bdd.close()