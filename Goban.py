"""
Plateau
@author: Nexmat
last update: 28-03-2016
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
        self.goban = [[None for i in range(taille)] for j in range(taille)]


    def make_move(self, colonne, ligne, joueur):
        """Permet d'effectuer un tour de jeu.
        colonne (lettre): Désigne la colonne dans laquelle la pièce sera posée.
        ligne   (nombre): Désigne la ligne   dans laquelle la pièce sera posée.
        joueur  (nombre): Désigne le joueur qui joue, 0 pour noir et 1 pour blanc.
        Retour: True ou False selon si l'opération a réussi ou non."""

        # Si tout est valide, on pose la pièce
        self.goban[ligne][colonne] = joueur

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
        
        #""" Cas d'un possible ko sur les bords du bogan"""
        
        #1er cas: le coup testé est à la dernière ligne du bogan
        if lgn==self.taille:
            if self.goban[lgn][col+1]==self.goban[lgn][col-1]==self.goban[lgn-1][col]==(joueur+1)%2 and self.goban[lgn-2][col]==self.goban[lgn-1][col-1]==self.goban[lgn-1][col+1]==joueur:
                return False
        #2ème cas : le coup testé est à la première ligne du bogan
        elif lgn==0:
            if self.goban[lgn][col-1]==self.goban[lgn][col+1]==self.goban[lgn+1][col]==(joueur+1)%2 and self.goban[lgn+1][col-1]==self.goban[lgn+1][col+1]==self.goban[lgn+2][col]==joueur:
                return False
        
        #3ème cas : le coup testé est à la dernière colonne du bogan
        elif col==self.taille:
            if self.goban[lgn-1][col]==self.goban[lgn+1][col]==self.goban[lgn][col-1]==(joueur+1)%2 and self.goban[lgn-1][col-1]==self.goban[lgn][col-2]==self.goban[lgn+1][col-1]:
                return False
       
        #4ème cas : le coup testé est à la première colonne du bogan
        elif col==0:
            if self.goban[lgn-1][col]==self.goban[lgn][col+1]==self.goban[lgn+1][col]==(joueur+1)%2 and self.goban[lgn-1][col+1]==self.goban[lgn][col+2]==self.goban[lgn+1][col+1]==joueur:
                return False
        
        #""" Cas d'un possible ko dans le bogan"""    
        
        else:
            if self.goban[lgn+1][col]==self.goban[lgn-1][col]==self.goban[lgn][col-1]==self.goban[lgn][col+1]==(joueur+1)%2:
                if self.goban[lgn][col-2]==self.goban[lgn+1][col-1]==self.goban[lgn-1][col-1]==joueur:
                    return False
                elif self.goban[lgn-1][col-1]==self.goban[lgn-2][col]==self.goban[lgn-1][col+1]==joueur:
                    return False
                elif self.goban[lgn-1][col+1]==self.goban[lgn][col+2]==self.goban[lgn+1][col+1]==joueur:
                    return False
                elif self.goban[lgn+1][col+1]==self.goban[lgn+2][col]==self.goban[lgn+1][col-1]==joueur:
                    return False
                else:
                    return True
            else:
                return True
                
    def neighbourg(joueur,lgn,col,L,L0,L1):
        """ Renvoi la liste des coups joués et la liste des voisins.
            L : liste des coups joués (joueur,ligne,colonne,indice)
            L0 : liste des voisins pour le joueur 0 (indice,[ligne,colonne],...)
            L1: liste des voisins pour le joueur 1
        """
        number_neighbourg=[]
        for i in range (len(L)):
            if joueur==L[i][0]:
                if ((L[i][1]==lgn+1 or L[i][1]==lgn-1) and (L[i][2]==col+1 or L[i][2]==col-1))
                or ((L[i][1]==lgn+1 or L[i][1]==lgn-1) and (L[i][2]==col))
                or ((L[i][1]==lgn) and (L[i][2]==col+1 or L[i][2]==col-1)):
                    indice=L[i][3]
                    if joueur==0:
                        L0[indice]+=[L[i][1],L[i][2]]
                        L+=[joueur,L[i][1],L[i][2],indice]
                        for k in range (len(number_neighbourg)):
                            if number_neighbourg[k]!=indice:
                                number_neighbourg+=[indice]
                    if joueur==1:
                        L1[indice]+=[L[i][1],L[i][2]]
                        L+=[joueur,L[i][1],L[i][2],indice]
                        for k in range (len(number_neighbourg)):
                            if number_neighbourg[k]!=indice:
                                number_neighbourg+=[indice]
        if len(number_neighbourg)>1:
            if joueur==0:
                for i in range (len(number_neighbourg)):
                    L0[number_neighbourg[0]]+=L0[number_neighbourg[i][1:]
                    L0.remove(L0[number_neighbourg[i]])  # remove ne marche pas avec des matrices ?
                for i in range (len(L0)):
                    L0[i][0]=i
            if joueur:        
                for i in range (len(number_neighbourg)):
                    L1[number_neighbourg[0]]+=L1[number_neighbourg[i][1:]
                    L1.remove(L1[number_neighbourg[i])
                for i in range (len(L1)):
                    L1[i][0]=i
        return(L,L0,L1)

if __name__ == '__main__':
    p = Plateau(5)
    
    
