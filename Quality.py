"""
Quality
@author: MrChapelle
last update: 13-04-2016
"""

import sys
import timeit
import random
from Gui import *
from Goban import *
from Joueur import *
from Exceptions import *
from Colors import cprint
from optparse import OptionParser;

class Quality :
    """ Evalue la qualité d'un coup proposé """

    def __init__(self,arg):
        """
        Constructeur
        """
        self.arg = arg      # ne sait pas quoi mettre

    def importance(self,col,lgn):
        imp = 0
        if not self.gaban.test_move(self,col,lgn,self.joueur.number):
            return(imp)
        return(1)
