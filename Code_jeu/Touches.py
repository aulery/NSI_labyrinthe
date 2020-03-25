# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
"""
Ensemble de fonctions qui definissent le comportement des touches du clavier.

"""

def espace(carte,personnage) :
    """ fonction qui fait une action lorsque l'on appuis sur la barre d'espace """
    personnage.deplacer(1,1)
    print("espace")

def haut(carte,personnage) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("z ou fleche haut")

def bas(carte,personnage) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou s(azerty) """
    print("s ou fleche bas")

def droite(carte,personnage) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("d ou fleche droite")

def gauche(carte,personnage) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("q ou fleche gauche")
