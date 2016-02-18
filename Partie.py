"""
Partie
@author: Nexmat
last update: 15-02-2016
"""

HR_LINE = 9472
VR_LINE = 9474
INTERSE = 9532

class Partie:
    """Modélise une partie de jeu de Go."""

    def __init__(self, taille = 9):
        """Crée une Partie. 
        Partie a comme attribut le goban, ie le plateau de jeu dont la taille sera passée en paramètre."""
        # On crée un tableau carré grâce à la taille passée en paramètre
        self.goban = [[None for i in range(taille)] for j in range(taille)]

    def affiche_goban(self):
        """Affiche dans le terminal le goban"""
        # Affichage des lettres des colonnes
        print('    ', end = '')
        for i in range(len(self.goban[0])):
            print(chr(65 + i) + '  ', end = '')
        print('')

        # Première ligne de verticaux
        print('    ', end = '')
        for i in self.goban[0]:
            print(chr(VR_LINE) + '  ', end = '')
        print('')

        nb_ligne = 1
        # Pour chaque ligne
        for ligne in self.goban:
            # Affichages des numéros de ligne
            print(repr(nb_ligne).rjust(2), end = '')
            nb_ligne += 1

            # Lignes horizontales
            print(chr(HR_LINE) * 2, end = '')

            # Affichage des intersections
            for colonne in ligne:
                # Intersection
                if colonne == None:
                    print(chr(INTERSE), end = chr(HR_LINE) * 2)
                # Pion
                else:
                    print('O', end = chr(HR_LINE) * 2)
            print('\n    ', end = '')

            # Lignes verticales
            for colonne in ligne:
                print(chr(VR_LINE) + '  ', end = '')
            print('')

if __name__ == '__main__':
    p = Partie(5)
    p.goban[2][3] = 1
    p.affiche_goban();

