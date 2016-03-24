from Colors import cprint

HR_LINE = chr(9472)
VR_LINE = chr(9474)
INTERSE = chr(9532)


def afficher_couleur(plateau):
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

def afficher_min(plateau):
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
                #print('O', end = HR_LINE * 2)
                if colonne == 0:
                    print("0", end = '')
                    print(HR_LINE * 2, end = '')
                else:
                    print("0", end = '')
                    print(HR_LINE * 2, end = '')
        print("")
        print('    ', end = '')

        # Lignes verticales
        for colonne in ligne:
            print(VR_LINE + '  ', end = '')
        print('')
