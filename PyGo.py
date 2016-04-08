"""
Partie
@author: Nexmat
last update: 03-04-2016
"""

import sys
import timeit
from Gui import *
from Goban import *
from Joueur import *
from Exceptions import *
from Colors import cprint
from optparse import OptionParser;

args    = None
options = None

class PyGo:
    """Models a Go game."""

    def __init__(self, size = 9):
        """Creates a Go game. 
        Game a comme attribut le goban, ie le plateau de jeu dont la taille sera passée en paramètre."""
        self.tour    = 0
        self.goban   = Goban(size)
        self.player1 = None
        self.player2 = None

def game_loop(game):
    global args
    global options

    while True:
        valid = False

        # Si c'est le tour du joueur 1
        if game.tour % 2 == 0:
            current_id     = 0
            current_player = game.player1
        # Si c'est le tour du joueur 2
        else:
            current_id     = 1
            current_player = game.player2

        # On recompte les scores
        game.player1.update_score()
        game.player2.update_score()

        # Affichage du goban
        if options.minim == True:
       	    round_display_min(game)
        else:
            round_display(game)

        # Entrée des coordonnées
        coord = current_player.choose_move()

        # On parse l'entrée
        ret = parse_coord(coord)
        if ret == True:
            print()
            sys.exit(0)
        elif ret == False:
            cprint("Erreur: entree incorrecte", fg = "red")
        else:
            try:
                (col, lgn) = ret
                # Si le coup est possible
                ret = game.goban.test_move(col, lgn, current_player)

                # S'il y a capture TODO: erreur car quand même execute apres exception
                if not ret == False:
                    game.goban.cell = make_capture(game.goban.cell, ret)

                # On pose le pion
                game.goban.make_move(col, lgn, current_id)

                # On enregistre la configuration actuelle
                game.goban.save_goban(game.goban.cell)

                # On enregistre le coup du joueur
                current_player.save_move(lgn, col)

                valid = True

            except Forbidden_move as e:
                cprint("Erreur: coup interdit,", str(e), fg = "red")
                valid = False
                if options.test_mode == True:
                    sys.exit(1)

        # Detection des territoires TODO: Affichage
        (black_territory, white_territory) = detect_territory(game.goban)

        # Si c'est valide
        if valid == True:
            # On passe au tour suivant
            game.tour += 1


def parse_coord(coord):
    # Pour quitter
    if coord == 'q' or coord == 'quit':
        return True

    # Mauvaises entrées
    if len(coord) != 2 and len(coord) != 3:
        return False

    # On transforme la lettre de la colonne en nombre pour le tableau
    col = ord(coord[0]) - 65

    # On adapte le numéro de ligne à l'utilisation du tableau
    lgn = int(coord[1:]) - 1

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

    # Création des joueurs
    p1 = Joueur(0, game) # Joueur noir
    p2 = Joueur(1, game) # Joueur blanc
    game.player1 = p1
    game.player2 = p2

    # Lancement de la boucle de jeu
    game_loop(game)


