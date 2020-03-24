# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python

# fichier principal ou qui servira de base pour le jeu
from IHM import Jeu
from Carte import carte
from Joueur import joueur
from Regles import *

Nombre_cases_largeur = 60
Nombre_cases_hauteur = 45
la_carte = carte(Nombre_cases_largeur,Nombre_cases_hauteur)

for i in range(Nombre_cases_largeur):
    la_carte.modifier_case(i,20,1)

position_de_depart_X,position_de_depart_Y  =  0 , 0
le_joueur = joueur("player 1 ",position_de_depart_X,position_de_depart_Y)


liste_des_regles = [on_ne_sort_pas_de_la_carte] # attention l'ordre compte

liste_des_images = ['personnage.png'
                    ,'mur.png'] # attention l'ordre compte

jeu = Jeu(Nombre_cases_largeur,Nombre_cases_hauteur,la_carte,le_joueur,liste_des_regles,liste_des_images)

jeu.lancer_jeu()

del Jeu
del liste_des_images
del liste_des_regles
del la_carte
