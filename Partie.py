"""
Partie
@author: Nexmat
last update: 21-02-2016
"""

import sys
from Joueur import *
from Plateau import *
from Colors import cprint

class Partie:
    """Modélise une partie de jeu de Go."""

    def __init__(self, taille = 5):
        """Crée une Partie. 
        Partie a comme attribut le goban, ie le plateau de jeu dont la taille sera passée en paramètre."""
        self.tour = 0
        self.goban = Plateau(taille)

    def afficher_tour(self):
        # On affiche le numéro du tour
        cprint("\n   - Tour numéro", str(self.tour + 1), "-", fg = "blue")
        cprint("-----------------------\n", fg = "blue")

        # Affichage du goban
        self.goban.afficher()
        print()

        cprint(" Au tour du joueur ", bg = "blue", end = "")
        # Tour du joueur noir
        if self.tour % 2 == 0:
            cprint("noir ", fg = "black",  bg = "blue", end = "")
        # Tour du joueur blanc
        else: 
            cprint("blanc ", fg = "white",  bg = "blue", end = "")
        cprint(">> ", fg = "white",  bg = "blue", end = "")

def boucle_jeu(p):
    while True:
        p.afficher_tour()

        # Entrée des coordonnées
        coord = input(" ")
        # On parse l'entrée
        ret = parse_coord(coord)
        if ret == True:
            sys.exit(0)
        # On pose le pion
        else:
            ret = p.goban.pose_pion(ret[0], ret[1], p.tour % 2)
        
        # Si c'est valide
        if ret:
            # On passe au tour suivant
            p.tour += 1


def parse_coord(coord):
    if coord == 'q':
        return True
    return coord[0], coord[1:]

if __name__ == '__main__':
    # Création d'une nouvelle partie
    p = Partie(15)

    # Création des joueurs #TODO
    #j1 = Joueur()
    #j2 = Joueur()

    # Lancement de la boucle de jeu
    boucle_jeu(p)
    #boucle_jeu(p, j1, j2) #TODO


