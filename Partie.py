"""
Partie
@author: Nexmat
last update: 15-02-2016
"""

class Partie:
    """Modélise une partie de jeu de Go."""

    def __init__(self, taille = 9):
        """Crée une Partie. 
        Partie a comme attribut le goban, ie le plateau de jeu dont la taille sera passée en paramètre."""
        # On crée un tableau carré grâce à la taille passée en paramètre
        self.goban = [[None for i in range(taille)] for j in range(taille)]

    def affiche_goban(self):
        for ligne in self.goban:
            for colonne in ligne:
                print(colonne, end = ' ')
            print('')

if __name__ == '__main__':
    p = Partie(5)
    p.affiche_goban();
        

