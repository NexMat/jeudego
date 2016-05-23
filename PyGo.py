"""
Partie
@author: Nexmat
last update: 23-04-2016
"""

import sys
import timeit
from Gui import *
from Goban import *
from Joueur import *
from Exceptions import *
from Colors import cprint
from IA_random import IA_random
from IA_level1 import IA_level1
from optparse import OptionParser

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

    player_passed = False

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
        if current_player.isHuman == True:
            ret = parse_coord(coord)
        else:
            ret = coord

        # S'il faut quitter
        if ret == True:
            print()
            sys.exit(0)
        # Si l'entree est incorrecte
        elif ret == False:
            cprint("Erreur: entrée incorrecte", fg = "red")
        # Si le joueur passe
        elif ret == "pass":
            # Si le joueur précédent a passé
            if player_passed == True:
                #TODO Affichage de fin de partie
                print()
                sys.exit(0)
            else:
                player_passed = True
                valid = True
        else:
            player_passed = False
            try:
                (col, lgn) = ret
                # Si le coup est possible
                ret = game.goban.test_move(col, lgn, current_player)

                # S'il y a capture
                if not ret == False:
                    game.goban.cell = make_capture(game.goban.cell, ret)
                    for group in ret:
                        current_player.captures += len(group)

                # On pose le pion
                game.goban.make_move(col, lgn, current_id)

                # On enregistre la configuration actuelle
                tmp_goban = []
                for old_lines in game.goban.cell:
                    tmp_goban.append(list(old_lines))
                game.goban.save_goban(tmp_goban)

                # On enregistre le coup du joueur
                current_player.save_move(lgn, col)

                valid = True

            except Forbidden_move as e:
                cprint("Erreur: coup interdit,", str(e), fg = "red")
                valid = False
                if options.test_mode == True:
                    sys.exit(1)

        # Detection des territoires
        (black_territory, white_territory) = detect_territory(game.goban)

        # Si c'est valide
        if valid == True:
            # On passe au tour suivant
            game.tour += 1


def parse_coord(coord):
    # Pour quitter
    if coord == 'q' or coord == 'quit':
        return True

    # Pour passer
    if coord == "pass":
        return "pass"

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
    # Parsing komi
    parser.add_option("-k", "--komi",
        action = "store",
        type = "float",
        dest = "komi",
        help = "Determines the value of the komi",
        default = "0")
    options, args = parser.parse_args(sys.argv)

if __name__ == '__main__':
    read_opt()
    # Création d'une nouvelle partie
    game = PyGo(options.size)

    # Création des joueurs
    p1 = None
    p2 = None

    # Joueur noir
    if options.player1 == 'ai0':
        p1 = IA_random(0, game)
    elif options.player1 == 'ai1':
        p1 = IA_level1(0, game, score = options.komi)
    elif options.player1 == 'minimax2':
        p1 = Minimax2(0, game, score = options.komi)
    else:
        p1 = Joueur(0, game)

    # Joueur blanc
    if options.player2 == 'ai0':
        p2 = IA_random(1, game, score = options.komi)
    elif options.player2 == 'ai1':
        p2 = IA_level1(1, game, score = options.komi)
    elif options.player2 == 'minimax2':
        p1 = Minimax2(1, game, score = options.komi)
    else:
        p2 = Joueur(1, game, score = options.komi)

    game.player1 = p1
    game.player2 = p2

    # Lancement de la boucle de jeu
    game_loop(game)


