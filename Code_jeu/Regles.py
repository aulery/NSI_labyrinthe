# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
def on_ne_sort_pas_de_la_carte(carte_avant,carte_apres,joueur_avant,joueur_apres) :
    """
    Fonction qui interdit le mouvement si le joueur depasse les bords de la carte.
    Pour MODELISER CECI, le on restaure le joueur et la carte précédente
    """

    on_depasse_sur_X =  joueur_apres.X < 0  or joueur_apres.X >= carte_avant.Largeur
    on_depasse_sur_Y =  joueur_apres.Y < 0  or joueur_apres.Y >= carte_avant.Hauteur
    print(joueur_avant.X," vs ", joueur_apres.X)
    if on_depasse_sur_X or on_depasse_sur_Y:

        carte_apres  = carte_avant
        joueur_apres = joueur_avant
