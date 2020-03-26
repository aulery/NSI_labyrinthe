# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
"""
Ensemble de fonctions qui definissent le comportement des touches du clavier.

"""

def suivi_statistiques(fonction):
    """
    decorateur pour le suivi des statistiques d'utilisation des Touches par un joueur
    """
    def touche_avec_stat(carte,personnage,etat):
        if fonction.__name__ in personnage.stats :
            personnage.stats[fonction.__name__] +=1
        else :
            personnage.stats[fonction.__name__] =1
        fonction(carte,personnage,etat)
    return touche_avec_stat

@suivi_statistiques
def espace(carte,personnage,etat) :
    """ fonction qui fait une action lorsque l'on appuis sur la barre d'espace """
    personnage.deplacer(1,1)

    print("espace")

@suivi_statistiques
def haut(carte,personnage,etat) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("z ou fleche haut")

@suivi_statistiques
def bas(carte,personnage,etat) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou s(azerty) """
    print("s ou fleche bas")

@suivi_statistiques
def droite(carte,personnage,etat) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("d ou fleche droite")

@suivi_statistiques
def gauche(carte,personnage,etat) :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("q ou fleche gauche")
