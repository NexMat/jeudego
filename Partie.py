"""
Partie
@author: Nexmat
last update: 21-02-2016
"""

import sys
from Colors import cprint
from Plateau import *

HR_LINE = chr(9472) VR_LINE = chr(9474)
INTERSE = chr(9532)

class Partie:
    """Modélise une partie de jeu de Go."""

    def __init__(self, taille = 5):
        """Crée une Partie. 
        Partie a comme attribut le goban, ie le plateau de jeu dont la taille sera passée en paramètre."""
        self.p = Plateau(taille)


def boucle_jeu():
    # Création d'une nouvelle partie
    p = Partie(15)

    # Détermine le tour actuel
    tour = 0

    while True:
        # On affiche le numéro du tour
        cprint("\n   - Tour numéro", str(tour + 1), "-", fg = "blue")
        cprint("-----------------------", fg = "blue")

        # Tour du joueur noir
        if tour % 2 == 0:
            print("Au tour du joueur noir:", end = "\n\n")
        # Tour du joueur blanc
        else: 
            print("Au tour du joueur blanc:", end = "\n\n")

        # Affichage du goban
        p.affiche_goban()

        # Entrée des coordonnées
        coord = input("\n>> ")
        # On parse l'entrée
        ret = parse_coord(coord)
        if ret == True:
            sys.exit(0)
        # On pose le pion
        else:
            ret = p.pose_pion(ret[0], ret[1], tour % 2)
        
        # Si c'est valide
        if ret:
            # On passe au tour suivant
            tour += 1


def parse_coord(coord):
    if coord == 'q':
        return True
    return coord[0], coord[1:]

if __name__ == '__main__':
    boucle_jeu()
