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
def lire_carte(nom_fichier):
    """
    fonction qui permet de lire dans un fichier la carte utilisée
    entrée :  un str qui contient le nom du fichier. attention le chemin dois être relatif
    """
    with  open(nom_fichier, "r") as fichier :
        contenu = fichier.read()
        print(contenu)
        taille_X_lue = 2
        taille_Y_lue = 1
        statistiques_lues = dict()
        tableau_des_cases_lue = [[0],[0]]
        carte_lue = carte(taille_X_lue,taille_Y_lue)
        carte.remplacer_statistiques(statistiques_lues)
        carte.redefinir_carte(tableau_des_cases_lue)

def sauvegarder_carte(carte,nom_fichier):
    """
    fonction qui permet d'écrire dans un fichier la carte  génrée
    entrée :  un str qui contient le nom du fichier. attention le chemin dois être relatif
    """
    X,Y = carte.dimensions()
    Tableau_des_cases = carte.copie_carte()
    statistiques = carte.recuperer_statistiques()
    with  open(nom_fichier, "w") as fichier :
        chaine = str(X) + " " + str(Y) + "\n"
        fichier.write(chaine)

# fichier principal ou qui servira de base pour le jeu

if __name__ == "__main__" :
    from IHM import Jeu
    from Carte import carte
    from Joueur import joueur
    from Regles import *

    liste_des_regles = [on_ne_sort_pas_de_la_carte
                       ,victoire] # attention l'ordre compte
    liste_des_images = [("personnage",'personnage.png')
                       ,("mur",'mur.png')
                       ,("arrivée",'fin.png')] # attention l'ordre compte
    Nombre_cases_Largeur = 20
    Nombre_cases_hauteur = 20
    la_carte = carte(Nombre_cases_Largeur,Nombre_cases_hauteur)

    # generer ou lire la carte.
    # lire_carte("monfichier_de_niveau.map")
    # ici un exemple de comment s'y prendre pour faire une carte à la main.
    position_de_depart_X,position_de_depart_Y  =  0 , 0

    tableau_carte = la_carte.copie_carte() # on recopie le tableau pour le modifier.
    for colonne in tableau_carte:
        colonne[8] = "mur" # on met un mur.

    la_carte.redefinir_carte(tableau_carte)
    # le joueur doit être sur une case vide.
    la_carte.modifier_case(position_de_depart_X,position_de_depart_Y,None)
    # le gagne s'il arrive a la position 5 , 5
    la_carte.modifier_case(position_de_depart_X+2,position_de_depart_Y+2,"arrivée")
    print(la_carte)

    le_joueur = joueur("player 1 ",position_de_depart_X,position_de_depart_Y,100)

    jeu = Jeu(Nombre_cases_Largeur
             ,Nombre_cases_hauteur
             ,la_carte,le_joueur
             ,liste_des_regles
             ,liste_des_images)
    jeu.lancer_jeu()

    # des Statistiques sont accèssibles
    statistiques_joueur = le_joueur.recuperer_statistiques()
    statistiques_carte = la_carte.recuperer_statistiques()
    print("votre score est de ",statistiques_joueur['score'])
    # ou imprimer de maniere brute.
    le_joueur.afficher_statistiques()
    la_carte.afficher_statistiques()
    # fonction de sauvegarde de la carte a completer
    sauvegarder_carte(la_carte,"carte.map")
    del Jeu
    del liste_des_images
    del liste_des_regles
    del la_carte
