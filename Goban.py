"""
Plateau
@author: Nexmat
last update: 09-03-2016
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
    
        #Préviens l'autre joueur s'il une de ces pièces est en atari à cause du coup joué.
        
        #les 4 prochains cas sont quand la dernière pierre posée est en bout pour créer l'atari
        #1er cas : l'atari est en bout gauche.
        ligne=i
        colonne=j
        if self.goban[i][j-1]==(joueur+1)%2 and self.goban[i-1][j-1]==self.goban[i+1][j-1]==joueur:
            while self.goban[i][j-2]==self.goban[i-1][j-2]==self.goban[i+1][j-2]!=null:
                j=j-1
            if self.goban[i][j-1]==(joueur+1)%2 and self.goban[i-1][j-1]==self.goban[i+1][j-1]==joueur:
                colonne=chr(j+65)
                ligne=i+1
                print("Le joueur" + (joueur+1)%2 +"est en atari en " + ligne+","+colonne )
        #2ème cas : l'atari est en bout droit.
        if self.goban[i][j+1]==(joueur+1)%2 and self.goban[i-1][j+1]==self.goban[i+1][j+1]==joueur:
            while self.goban[i][j+2]==self.goban[i-1][j+2]==self.goban[i+1][j+2]!=null:
                j=j+1
            if self.goban[i][j+1]==(joueur+1)%2 and self.goban[i-1][j+1]==self.goban[i+1][j+1]==joueur:
                colonne=chr(j+65)
                ligne=i+1
                print("Le joueur"+(joueur+1)%2+"est en atari en"+ligne+","+colonne)
        # 3ème cas : l'atari est en bout bas.
        if self.goban[i+1][j]==(joueur+1)%2 and self.goban[i+1][j+1]==self.goban[i+1][j-1]==joueur:
            while self.goban[i+2][j]==self.goban[i+2][j+1]==self.goban[i+2][j-1]!=null:
                i=i+1
            if self.goban[i+1][j]==(joueur+1)%2 and self.goban[i+1][j+1]==self.goban[i+1][j-1]==joueur:
                colonne=chr(j+65)
                ligne=i+1
                print("Le joueur"+(joueur+1)%2+"est en atari en"+ligne+","+colonne)
        #4 ème cas : l'atari est en bout en haut.
        if self.goban[i-1][j]==(joueur+1)%2 and self.goban[i-1][j+1]==self.goban[i-1][j-1]==joueur:
            while self.goban[i-2][j]==self.goban[i-2][j+1]==self.goban[i-2][j-1]!=null:
                i=i-1
            if self.goban[i-1][j]==(joueur+1)%2 and self.goban[i-1][j+1]==self.goban[i-1][j-1]==joueur:
                colonne=chr(j+65)
                ligne=i+1
                print("Le joueur"+(joueur+1)%2+"est en atari en"+ligne+","+colonne)
    
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
    

if __name__ == '__main__':
    p = Plateau(5)
