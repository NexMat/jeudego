"""
Partie
@author: Nexmat
last update: 21-02-2016
"""

import sys
from Gui import *
from Joueur import *
from Goban import *
from Colors import cprint
from optparse import OptionParser;

args    = None
options = None

class PyGo:
    """Models a Go game."""

    def __init__(self, size = 9):
        """Creates a Go game. 
        Game a comme attribut le goban, ie le plateau de jeu dont la taille sera passée en paramètre."""
        self.tour  = 0
        self.goban = Goban(size)

def game_loop(p):
    global args
    global options

    while True:
        if options.minim == True:
       	    afficher_tour_min(p)
        else:
            afficher_tour(p)

        # Entrée des coordonnées
        coord = input(" ")
        # On parse l'entrée
        ret = parse_coord(coord)
        if ret == True:
            print()
            sys.exit(0)
        else:
            if p.goban.test_move(ret[0], ret[1], p.tour % 2):
                # On pose le pion
                ret = p.goban.make_move(ret[0], ret[1], p.tour % 2)
            else:
                cprint("Erreur: coup interdit", fg = "red")
                if options.test_mode == True:
                    sys.exit(1)
                ret = False
        
        # Si c'est valide
        if ret:
            # On passe au tour suivant
            p.tour += 1


def parse_coord(coord):
    # Pour quitter
    if coord == 'q' or coord == 'quit':
        return True

    # On transforme la lettre de la colonne en nombre pour le tableau
    col = ord(coord[0]) - 65

    # On adapte le numéro de ligne à l'utilisation du tableau
    lgn = int(coord[1]) - 1

    return col, lgn

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
        help = "Minimalist display (default False). With minimalist display, colors are not used",
        default = "False")
    options, args = parser.parse_args(sys.argv)

if __name__ == '__main__':
    read_opt();
    # Création d'une nouvelle partie
    game = PyGo(options.size)

    # Création des joueurs #TODO
    #j1 = Joueur()
    #j2 = Joueur()

    # Lancement de la boucle de jeu
    game_loop(game)
    #boucle_jeu(p, j1, j2) #TODO


