# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
"""
Fichier principal du logiciel NSI_Labyrinthe.
Il suit la logique suivante :
1 - import des bibliotèques.
2 - choix des regles
3 - choix des Images
4 - creation d'une carte vide
5 - construcion de la carte (manuelle / lecture / copie)
6 - boucle de Jeu
7 - destructions des objets créer pour assurer qu'il n'y a pas de problemes

"""

# fichier principal ou qui servira de base pour le jeu

if __name__ == "__main__" :
    from IHM import Jeu
    from Carte import carte
    from Joueur import joueur
    from Regles import *

    liste_des_regles = [on_ne_sort_pas_de_la_carte,victoire] # attention l'ordre compte
    liste_des_images = ['personnage.png'
                        ,'mur.png','fin.png'] # attention l'ordre compte
    Nombre_cases_largeur = 20
    Nombre_cases_hauteur = 20
    la_carte = carte(Nombre_cases_largeur,Nombre_cases_hauteur)

    # generer ou lire la carte.
    # ici un exemple de comment s'y prendre pour faire une carte à la main.
    position_de_depart_X,position_de_depart_Y  =  0 , 0

    tableau_carte = la_carte.copie_carte() # on recopie le tableau pour le modifier.
    for colonne in tableau_carte:
        colonne[8] = 1 # on met un mur.

    la_carte.redefinir_carte(tableau_carte)
    # le joueur doit être sur une case vide.
    la_carte.modifier_case(position_de_depart_X,position_de_depart_Y,None)
    # le gagne s'il arrive a la position 5 , 5
    la_carte.modifier_case(position_de_depart_X+2,position_de_depart_Y+3,2)
    print(la_carte)

    le_joueur = joueur("player 1 ",position_de_depart_X,position_de_depart_Y,100)

    jeu = Jeu(Nombre_cases_largeur
             ,Nombre_cases_hauteur
             ,la_carte,le_joueur
             ,liste_des_regles
             ,liste_des_images)
    jeu.lancer_jeu()
    print(le_joueur.stats)

    del Jeu
    del liste_des_images
    del liste_des_regles
    del la_carte
