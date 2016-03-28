from Colors import cprint

HR_LINE = chr(9472)
VR_LINE = chr(9474)
INTERSE = chr(9532)

def color_display(plateau):
    """Affiche dans le terminal le goban"""
    # Affichage des lettres des colonnes
    cprint('    ', bg = "brown", end = '')
    for i in range(len(plateau.goban[0])):
        cprint(chr(65 + i) + '  ', bg = "brown", end = '')
    print('')

    # Première ligne de verticaux
    cprint('    ', bg = "brown", end = '')
    for i in plateau.goban[0]:
        cprint(VR_LINE + '  ', bg = "brown", end = '')
    print('')

    nb_ligne = 1
    # Pour chaque ligne
    for ligne in plateau.goban:
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
                # Le joueur blanc
                if colonne == 1:
                    cprint("0", bg = "brown", end = '')
                    cprint(HR_LINE * 2, fg = "white", bg = "brown", end = '')
                # Le joueur noir
                else:
                    cprint("0", fg = "black", bg = "brown", end = '')
                    cprint(HR_LINE * 2, fg = "white", bg = "brown", end = '')
        print("")
        cprint('    ', bg = "brown", end = '')

        # Lignes verticales
        for colonne in ligne:
            cprint(VR_LINE + '  ', bg = "brown", end = '')
        print('')

def display_min(plateau):
    """Affiche dans le terminal le goban"""
    # Affichage des lettres des colonnes
    print('    ', end = '')
    for i in range(len(plateau.goban[0])):
        print(chr(65 + i) + '  ', end = '')
    print('')

    # Première ligne de verticaux
    print('    ', end = '')
    for i in plateau.goban[0]:
        print(VR_LINE + '  ', end = '')
    print('')

    nb_ligne = 1
    # Pour chaque ligne
    for ligne in plateau.goban:
        # Affichages des numéros de ligne
        print(repr(nb_ligne).rjust(2), end = '')
        nb_ligne += 1

        # Lignes horizontales
        print(HR_LINE * 2, end = '')

        # Affichage des intersections
        for colonne in ligne:
            # Intersection
            if colonne == None:
                print(INTERSE + HR_LINE * 2, end = '')
            # Pion
            else:
                if colonne == 0:
                    print("0", end = '')
                    print(HR_LINE * 2, end = '')
                else:
                    print("1", end = '')
                    print(HR_LINE * 2, end = '')
        print("")
        print('    ', end = '')

        # Lignes verticales
        for colonne in ligne:
            print(VR_LINE + '  ', end = '')
        print('')

def round_display(partie):
    # On affiche le numéro du tour
    cprint("\n        - Tour numéro", str(partie.tour + 1), "-", fg = "blue")
    cprint("----------------------------------", fg = "blue")
    
    # Score du joueur noir
    cprint(" Joueur noir: 0 ", fg = "black",  bg = "blue", end = "")
    #cprint(j1.score, fg = "black", bg = "blue", end = "")

    # Score du joueur blanc
    cprint("Joueur blanc: 0 ", fg = "white",  bg = "blue", end = "")
    #cprint(j1.score, fg = "black", bg = "blue", end = "")
    cprint("\n----------------------------------\n", fg = "blue")

    # Affichage du goban
    color_display(partie.goban)
    print()

    # Affichage de la ligne d'input
    cprint(" Au tour du joueur ", bg = "blue", end = "")
    # Tour du joueur noir
    if partie.tour % 2 == 0:
        cprint("noir ", fg = "black",  bg = "blue", end = "")
    # Tour du joueur blanc
    else: 
        cprint("blanc ", fg = "white",  bg = "blue", end = "")
    cprint(">> ", fg = "white",  bg = "blue", end = "")

def round_display_min(partie):
    # On affiche le numéro du tour
    print("\n        - Tour numéro", str(partie.tour + 1), "-")
    print("----------------------------------")
    
    # Score du joueur noir
    print(" Joueur noir: 0 ", end = "")
    #cprint(j1.score, fg = "black", bg = "blue", end = "")

    # Score du joueur blanc
    print("Joueur blanc: 0 ", end = "")
    #cprint(j1.score, fg = "black", bg = "blue", end = "")
    print("\n----------------------------------\n")

    # Affichage du goban
    display_min(partie.goban)
    print()

    print(" Au tour du joueur ", end = "")
    # Tour du joueur noir
    if partie.tour % 2 == 0:
        print("noir ", end = "")
    # Tour du joueur blanc
    else: 
        print("blanc ", end = "")
    print(">>", end = "")

