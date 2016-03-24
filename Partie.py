"""
Partie
@author: Nexmat
last update: 21-02-2016
"""

import sys
from Gui import *
from Joueur import *
from Plateau import *
from Colors import cprint
from optparse import OptionParser;

args    = None
options = None

class Partie:
    """Modélise une partie de jeu de Go."""

    def __init__(self, taille = 9):
        """Crée une Partie. 
        Partie a comme attribut le goban, ie le plateau de jeu dont la taille sera passée en paramètre."""
        self.tour  = 0
        self.goban = Plateau(taille)

    def afficher_tour(self):
        # On affiche le numéro du tour
        cprint("\n        - Tour numéro", str(self.tour + 1), "-", fg = "blue")
        cprint("----------------------------------", fg = "blue")
        
        # Score du joueur noir
        cprint(" Joueur noir: 0 ", fg = "black",  bg = "blue", end = "")
        #cprint(j1.score, fg = "black", bg = "blue", end = "")

        # Score du joueur blanc
        cprint("Joueur blanc: 0 ", fg = "white",  bg = "blue", end = "")
        #cprint(j1.score, fg = "black", bg = "blue", end = "")
        cprint("\n----------------------------------\n", fg = "blue")

        # Affichage du goban
        afficher_couleur(self.goban)
        print()

        cprint(" Au tour du joueur ", bg = "blue", end = "")
        # Tour du joueur noir
        if self.tour % 2 == 1:
            cprint("noir ", fg = "black",  bg = "blue", end = "")
        # Tour du joueur blanc
        else: 
            cprint("blanc ", fg = "white",  bg = "blue", end = "")
        cprint(">> ", fg = "white",  bg = "blue", end = "")

    def afficher_tour_min(self):
        # On affiche le numéro du tour
        print("\n        - Tour numéro", str(self.tour + 1), "-")
        print("----------------------------------")
        
        # Score du joueur noir
        print(" Joueur noir: 0 ", end = "")
        #cprint(j1.score, fg = "black", bg = "blue", end = "")

        # Score du joueur blanc
        print("Joueur blanc: 0 ", end = "")
        #cprint(j1.score, fg = "black", bg = "blue", end = "")
        print("\n----------------------------------\n")

        # Affichage du goban
        afficher_min(self.goban)
        print()

        print(" Au tour du joueur ", end = "")
        # Tour du joueur noir
        if self.tour % 2 == 1:
            print("noir ", end = "")
        # Tour du joueur blanc
        else: 
            print("blanc ", end = "")
        print(">> ", end = "")

def boucle_jeu(p):
    global args
    global options

    while True:
        if options.minim == True:
       	    p.afficher_tour_min()
        else:
            p.afficher_tour()

        # Entrée des coordonnées
        coord = input(" ")
        # On parse l'entrée
        ret = parse_coord(coord)
        if ret == True:
            print()
            sys.exit(0)
        # On pose le pion
        else:
            if p.goban.tester_coup(ret[0], ret[1], p.tour % 2):
                cprint("OK")
                ret = p.goban.pose_pion(ret[0], ret[1], p.tour % 2)
            else:
                cprint("Erreur", fg = "red")
                if options.test_mode == True:
                    sys.exit(1)
                ret = False
        
        # Si c'est valide
        if ret:
            # On passe au tour suivant
            p.tour += 1


def parse_coord(coord):
    if coord == 'q':
        return True
    return coord[0], coord[1:]

def read_opt():
    global args
    global options
    
    parser = OptionParser()
    # Parsing size
    parser.add_option("-s", "--size",
        action = "store",
        type = "int",
        dest = "size",
        help = "Determines the size of the goban",
        default = "9")
    # Parsing player 1
    parser.add_option("--player1",
        action = "store",
        type = "string",
        dest = "player1",
        help = "Determines the type of player 1: human or ai",
        default = "player1")
    # Parsing player 2
    parser.add_option("--player2",
        action = "store",
        type = "string",
        dest = "player2",
        help = "Determines the type of player 2: human or ai",
        default = "player2")
    # Parsing test mode
    parser.add_option("-t", "--test",
        action = "store_true",
        dest = "test_mode",
        help = "Test mode (default false). In test mode, any error will stop the program",
        default = "False")
    # Parsing no color display
    parser.add_option("-m", "--min",
        action = "store_true",
        dest = "minim",
        help = "Minimalist display (default False). With minimalist display, colors are not used.",
        default = "False")
    options, args = parser.parse_args(sys.argv)

if __name__ == '__main__':
    read_opt();
    # Création d'une nouvelle partie
    p = Partie(options.size)

    # Création des joueurs #TODO
    #j1 = Joueur()
    #j2 = Joueur()

    # Lancement de la boucle de jeu
    boucle_jeu(p)
    #boucle_jeu(p, j1, j2) #TODO


