# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
from pygame.locals import * # pas obligatoire mais plus simple
def espace() :
    """ fonction qui fait une action lorsque l'on appuis sur la barre d'espace """
    print("espace")

def haut() :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("z ou fleche haut")

def bas() :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou s(azerty) """
    print("s ou fleche bas")

def droite() :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("d ou fleche droite")

def gauche() :
    """ fonction qui fait une action lorsque l'on appuis sur la fleche du haut ou z(azerty) """
    print("q ou fleche gauche")

def actions(touche) :
    """ fonction qui distribue le travail en fonction des touches appuyées
    le choix de ne pas utiliser de elif est volontaire pour permettre d'intercepter plusieurs touche à la fois.
    """
    if touche == K_SPACE :
        espace()
    if touche == K_UP or touche == K_w:
        haut()
    if touche == K_DOWN or touche == K_s:
        bas()
    if touche == K_LEFT or touche == K_d:
        droite()
    if touche == K_RIGHT or touche == K_a:
        gauche()
