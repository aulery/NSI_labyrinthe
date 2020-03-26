# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python

"""
Ensemble des regles du jeu, tout impact sur le jeu
dois se faire au travers des classes en argument
par default il s'agit de carte et joueur
"""

def on_ne_sort_pas_de_la_carte(carte_apres,joueur_apres,etat_du_jeu) :
    """
    Fonction qui interdit le mouvement si le joueur depasse les bords de la carte.
    Pour MODELISER CECI, on restaure le joueur précédent
    """
    on_depasse_sur_X =  joueur_apres.X < 0  or joueur_apres.X >= carte_apres.Largeur
    on_depasse_sur_Y =  joueur_apres.Y < 0  or joueur_apres.Y >= carte_apres.Hauteur

    if on_depasse_sur_X or on_depasse_sur_Y:
        joueur_apres.annuler_coup()

def victoire(carte,joueur,etat_du_jeu) :
    """
    Fonction qui donne la victoire quand le joueur touche l'arrivée sur la case de victoire.
    """
    position_X, position_Y = joueur.X, joueur.Y
    if carte.tab[position_X][position_Y] == 2 :
        print("le joueur a gagné")
        etat_du_jeu.en_cours = False

def compter_deplacement(carte,joueur,etat_du_jeu):
    """
    Fonction du modifie le score si le joueur c'est deplacer
    """
    pass
