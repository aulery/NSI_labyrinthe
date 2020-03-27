# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python

"""
Ensemble des regles du jeu, tout impact sur le jeu
dois se faire au travers des classes en argument
par default il s'agit de carte et joueur
"""
from Statistiques import ajout_statistique_ponctuelle

def on_ne_sort_pas_de_la_carte(carte,joueur,etat_du_jeu) :
    """
    Fonction qui interdit le mouvement si le joueur depasse les bords de la carte.
    Pour MODELISER CECI, on restaure le joueur précédent
    """
    X,Y = joueur.position()
    Max_X, Max_Y = carte.dimensions()
    on_depasse_sur_X =  (X < 0)  or (X >= Max_X)
    on_depasse_sur_Y =  (Y < 0)  or (Y >= Max_Y)

    if on_depasse_sur_X or on_depasse_sur_Y:
        joueur.annuler_coup()

def victoire(carte,joueur,etat_du_jeu) :
    """
    Fonction qui donne la victoire quand le joueur touche l'arrivée sur la case de victoire.
    """
    X, Y = joueur.position()
    if carte.tab[X][Y] == 2 :
        print("le joueur a gagné")
        ajout_statistique_ponctuelle(joueur,"Victoire")
        etat_du_jeu.fin_de_partie()

def compter_deplacement(carte,joueur,etat_du_jeu):
    """
    Fonction du modifie le score si le joueur c'est deplacer
    """
    pass
