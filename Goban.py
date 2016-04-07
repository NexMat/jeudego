"""
Plateau
@author: Nexmat
last update: 03-04-2016
"""

import sys
from Colors import cprint

class Goban:
    """Modélise un plateau de jeu de Go, le goban."""

    def __init__(self, taille = 9):
        """Creates a Goban. 
        Goban takes as parameter the size of the goban itself."""
        self.taille = taille
        # On crée un tableau carré grâce à la taille passée en paramètre
        self.cell = [[None for i in range(taille)] for j in range(taille)]


    def make_move(self, colonne, ligne, joueur):
        """Permet d'effectuer un tour de jeu.
        colonne (lettre): Désigne la colonne dans laquelle la pièce sera posée.
        ligne   (nombre): Désigne la ligne   dans laquelle la pièce sera posée.
        joueur  (nombre): Désigne le joueur qui joue, 0 pour noir et 1 pour blanc.
        Retour: True ou False selon si l'opération a réussi ou non."""
        
        # Si tout est valide, on pose la pièce
        self.cell[ligne][colonne] = joueur
        
        return True
    
    
    def test_move(self, col, lgn, joueur):
        """Tester le coup choisi par le joueurs.
        col     (nombre): Désigne la colonne dans laquelle la pièce sera posée.
        lgn     (nombre): Désigne la ligne   dans laquelle la pièce sera posée.
        joueur  (nombre): Désigne le joueur qui joue, 0 pour noir et 1 pour blanc.
        Retour: True ou False selon si l'opération est possible ou non."""
        
        if col < 0 or col >= self.taille:
            return False

        if lgn < 0 or lgn >= self.taille:
            return False

        # On vérifie que joueur est bien soit 1 soit 2
        if joueur != 0 and joueur != 1:
            return False

    
        """règle du ko: Un joeur en posant un pierre, ne doit pas redonner au goban
        un état idetentique à l'un de ceux qu'il lui avait était déjà donné."""
        
        # Cas d'un possible ko sur les bords du bogan
        
        #1er cas: le coup testé est à la dernière ligne du bogan
        if lgn==self.taille:
            if self.cell[lgn][col+1]==self.cell[lgn][col-1]==self.cell[lgn-1][col]==(joueur+1)%2 and self.cell[lgn-2][col]==self.cell[lgn-1][col-1]==self.cell[lgn-1][col+1]==joueur:
                return False
        #2ème cas : le coup testé est à la première ligne du bogan
        elif lgn==0:
            if self.cell[lgn][col-1]==self.cell[lgn][col+1]==self.cell[lgn+1][col]==(joueur+1)%2 and self.cell[lgn+1][col-1]==self.cell[lgn+1][col+1]==self.cell[lgn+2][col]==joueur:
                return False
        
        #3ème cas : le coup testé est à la dernière colonne du bogan
        elif col==self.taille:
            if self.cell[lgn-1][col]==self.cell[lgn+1][col]==self.cell[lgn][col-1]==(joueur+1)%2 and self.cell[lgn-1][col-1]==self.cell[lgn][col-2]==self.cell[lgn+1][col-1]:
                return False
       
        #4ème cas : le coup testé est à la première colonne du bogan
        elif col==0:
            if self.cell[lgn-1][col]==self.cell[lgn][col+1]==self.cell[lgn+1][col]==(joueur+1)%2 and self.cell[lgn-1][col+1]==self.cell[lgn][col+2]==self.cell[lgn+1][col+1]==joueur:
                return False
        
        #""" Cas d'un possible ko dans le bogan"""    
        
        else:
            if self.cell[lgn+1][col]==self.cell[lgn-1][col]==self.cell[lgn][col-1]==self.cell[lgn][col+1]==(joueur+1)%2:
                if self.cell[lgn][col-2]==self.cell[lgn+1][col-1]==self.cell[lgn-1][col-1]==joueur:
                    return False
                elif self.cell[lgn-1][col-1]==self.cell[lgn-2][col]==self.cell[lgn-1][col+1]==joueur:
                    return False
                elif self.cell[lgn-1][col+1]==self.cell[lgn][col+2]==self.cell[lgn+1][col+1]==joueur:
                    return False
                elif self.cell[lgn+1][col+1]==self.cell[lgn+2][col]==self.cell[lgn+1][col-1]==joueur:
                    return False
                else:
                    return True
            else:
                return True

        return True
                
    #def neighbourg(joueur,lgn,col,L,L0,L1):
    #    """ Renvoi la liste des coups joués et la liste des voisins.
    #        L : liste des coups joués (joueur,ligne,colonne,indice)
    #        L0 : liste des voisins pour le joueur 0 (indice,[ligne,colonne],...)
    #        L1: liste des voisins pour le joueur 1
    #    """
    #    number_neighbourg=[]
    #    for i in range(len(L)):
    #        if joueur==L[i][0]:
    #            if ((L[i][1]==lgn+1 or L[i][1]==lgn-1) and (L[i][2]==col+1 or L[i][2]==col-1))
    #            or ((L[i][1]==lgn+1 or L[i][1]==lgn-1) and (L[i][2]==col))
    #            or ((L[i][1]==lgn) and (L[i][2]==col+1 or L[i][2]==col-1)):
    #                indice=L[i][3]
    #                if joueur==0:
    #                    L0[indice]+=[L[i][1],L[i][2]]
    #                    L+=[joueur,L[i][1],L[i][2],indice]
    #                    for k in range (len(number_neighbourg)):
    #                        if number_neighbourg[k]!=indice:
    #                            number_neighbourg+=[indice]
    #                if joueur==1:
    #                    L1[indice]+=[L[i][1],L[i][2]]
    #                    L+=[joueur,L[i][1],L[i][2],indice]
    #                    for k in range (len(number_neighbourg)):
    #                        if number_neighbourg[k]!=indice:
    #                            number_neighbourg+=[indice]
    #    if len(number_neighbourg)>1:
    #        if joueur==0:
    #            for i in range (len(number_neighbourg)):
    #                L0[number_neighbourg[0]]+=L0[number_neighbourg[i][1:]
    #                L0.remove(L0[number_neighbourg[i]])  # remove ne marche pas avec des matrices ?
    #            for i in range (len(L0)):
    #                L0[i][0]=i
    #        if joueur:        
    #            for i in range (len(number_neighbourg)):
    #                L1[number_neighbourg[0]]+=L1[number_neighbourg[i][1:]
    #                L1.remove(L1[number_neighbourg[i])
    #            for i in range (len(L1)):
    #                L1[i][0]=i
    #    return(L,L0,L1)


black_territory = []
white_territory = []

def detect_territory(goban):
    """Detecte les territoires qui sont sur le goban
    et leurs couleurs d'appartenance
    Arg: goban concerne"""
    global black_territory
    global white_territory

    black_territory = []
    white_territory = []

    for i in range(goban.taille):
        for j in range(goban.taille):
            if goban.cell[i][j] == None and not is_in_territory(i,j):
                group = find_group(goban, i, j, [])
                if group_color(goban, group) == 0:
                    black_territory.append(group)

                elif group_color(goban, group) == 1:
                    white_territory.append(group)

    print('\nWhite:', white_territory)
    print('Black:', black_territory)

def is_in_territory(i, j):
    """Determine si la cellule en (i,j) est deja dans un groupe ou non"""
    global black_territory
    global white_territory
    
    for group in black_territory:
        if not group == None and (i, j) in group:
            return True

    for group in white_territory:
        if not group == None and  (i, j) in group:
            return True

    return False

def get_neighbour(goban, i, j):
    """Trouve les voisins directs d'une case
    Arg: goban, le goban concerne
         (i,j) les coordonnees
    Ret: La liste des voisins """
    ret = []

    # Pas la premiere ligne
    if not i == 0:
        ret.append((i-1, j))
    # Pas la première colonne
    if not j == 0:
        ret.append((i, j-1)) # Pas la derniere ligne
    if not i == goban.taille - 1:
        ret.append((i+1, j))
    # Pas la première colonne
    if not j == goban.taille - 1:
        ret.append((i, j+1))

    return ret


def find_group(goban, i, j, group):
    # On recupere la liste des voisins
    voisins = get_neighbour(goban, i, j)
    # On parcourt la liste des voisins
    for (k, l) in voisins:
        # Si le voisin est bien vide et n'est pas deja dans le groupe
        if goban.cell[k][l] == None and not (k, l) in group:
            # On l'ajoute au groupe
            group.append((k,l))
            find_group(goban, k, l, group)
    return group

def group_color(goban, group):
    """Determine la couleur d'appartenance d'un groupe
    Arg: goban, le goban concerne
         group, le group dont la couleur est a determiner
    Ret: la couleur, 0 pour noir, 1 pour blanc, 2 pour aucun"""
    color = None
    
    # On parcourt les elements du groupe
    for (i, j) in group:
        # Pour chaque element, on determine les voisins
        voisins = get_neighbour(goban, i, j)
        # Parcours des voisins
        for (k, l) in voisins:
            if color == None:
                color = goban.cell[k][l]

            elif goban.cell[k][l] != None and goban.cell[k][l] != color:
                return 2

    return color


if __name__ == '__main__':
    g = Goban()
    
