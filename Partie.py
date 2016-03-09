"""
Partie
@author: Nexmat
last update: 21-02-2016
"""

import sys
from Colors import cprint

HR_LINE = chr(9472)
VR_LINE = chr(9474)
INTERSE = chr(9532)

class Partie:
    """Modélise une partie de jeu de Go."""

    def __init__(self, taille = 5):
        """Crée une Partie. 
        Partie a comme attribut le goban, ie le plateau de jeu dont la taille sera passée en paramètre."""
        self.taille = taille
        # On crée un tableau carré grâce à la taille passée en paramètre
        self.goban = [[None for i in range(taille)] for j in range(taille)]

    def affiche_goban(self):
        """Affiche dans le terminal le goban"""
        # Affichage des lettres des colonnes
        cprint('    ', bg = "brown", end = '')
        for i in range(len(self.goban[0])):
            cprint(chr(65 + i) + '  ', bg = "brown", end = '')
        print('')

        # Première ligne de verticaux
        cprint('    ', bg = "brown", end = '')
        for i in self.goban[0]:
            cprint(VR_LINE + '  ', bg = "brown", end = '')
        print('')

        nb_ligne = 1
        # Pour chaque ligne
        for ligne in self.goban:
            # Affichages des numéros de ligne
            cprint(repr(nb_ligne).rjust(2), bg = "brown", end = '')
            nb_ligne += 1

            # Lignes horizontales
            cprint(HR_LINE * 2, bg = "brown", end = '')

            # Affichage des intersections
            for colonne in ligne:
                # Intersection
                if colonne == None:
                    cprint(INTERSE + HR_LINE * 2, bg = "brown", end = '')
                # Pion
                else:
                    #print('O', end = HR_LINE * 2)
                    if colonne == 0:
                        cprint("0", bg = "brown", end = '')
                        cprint(HR_LINE * 2, fg = "white", bg = "brown", end = '')
                    else:
                        cprint("0", fg = "black", bg = "brown", end = '')
                        cprint(HR_LINE * 2, fg = "white", bg = "brown", end = '')
            print("")
            cprint('    ', bg = "brown", end = '')

            # Lignes verticales
            for colonne in ligne:
                cprint(VR_LINE + '  ', bg = "brown", end = '')
            print('')

    def pose_pion(self, colonne, ligne, joueur):
        """Permet d'effectuer un tour de jeu.
        colonne (lettre): Désigne la colonne dans laquelle la pièce sera posée.
        ligne   (nombre): Désigne la ligne   dans laquelle la pièce sera posée.
        joueur  (nombre): Désigne le joueur qui joue, 0 pour noir et 1 pour blanc.
        Retour: True ou False selon si l'opération a réussi ou non."""

        # On transforme la lettre de la colonne en nombre pour le tableau
        col = ord(colonne) - 65
        if col < 0 or col >= self.taille:
            return False

        # On adapte le numéro de ligne à l'utilisation du tableau
        lgn = int(ligne) - 1
        if lgn < 0 or lgn >= self.taille:
            return False

        # On vérifie que joueur est bien soit 1 soit 2
        if joueur != 0 and joueur != 1:
            return False

        # Si tout est valide, on pose la pièce
        self.goban[lgn][col] = joueur
        return True

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
