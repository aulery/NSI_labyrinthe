# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
"""
Ensemble de fonctions qui definissent le comportement des touches du clavier.

"""
from Statistiques import suivi_statistiques_joueur

@suivi_statistiques_joueur
def espace(carte,personnage,etat) :
    """ fonction qui fait une action lorsque l'on appuis sur la barre d'espace """
    personnage.deplacer(1,1)

    print("espace")

@suivi_statistiques_joueur
def haut(carte,personnage,etat) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("z ou fleche haut")

@suivi_statistiques_joueur
def bas(carte,personnage,etat) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou s(azerty) """
    print("s ou fleche bas")

@suivi_statistiques_joueur
def droite(carte,personnage,etat) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("d ou fleche droite")

@suivi_statistiques_joueur
def gauche(carte,personnage,etat) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("q ou fleche gauche")
