# -*- coding: <encoding name> -*-
"""
Module qui gere l'affichage graphique.
Les élèves n'ont pas besoin de travailler ici, tout se gère dans le main.
"""
# coding=utf8
# pensez a recopier l'encodage dans chaque fichier Python

import os
import pygame # import total on limitera plus tard les besoins au minimum
from pygame.locals import * # pas obligatoire mais plus simple
from Actions import *
from Etat import *
class Jeu():
    """ Classe qui gere le jeu.
        elle change l'etat du jeu 25 fois par secondes
        La boucle de jeu est la suivante :
        1 - verifier les interactions utilisateurs gerer_evenement()
        voir https://www.pygame.org/docs/ref/event.html
        2 - pour chaque evenement, verifier les regles du jeu. et annuler si besoin actions()
        3 - afficher la carte puis le joueur. dessiner()

    """
    def importer_image_transparente(self,nom,repertoire="Images"):
        """ Fonction qui importe une image avec transparence.
        entree :
            * nom string: le nom de l'image avec extension
            * repetoire string : le nom du repertoire par default Code_jeu/Images
        sortie :
            * une image convertie utilisable par pygame avec transparence
        """
        return pygame.image.load(os.path.join(repertoire,nom)).convert_alpha()

    def __init__(self, Nombre_cases_Largeur,Nombre_cases_hauteur,la_carte,le_joueur,liste_des_regles,liste_des_images):
        """ fonction d'initialisation de l'interface graphique.
        Entree :
        * Nombre_cases_Largeur type int
        * Nombre_cases_hauteur type int
        * la_carte represente la carte en utilisant la classe carte
        * le_joueur represente le joueur en utilisant la classe joueur_apres
        * liste_des_regles liste de fonction
        * liste_des_images liste de str
        Par default une case de carte fait 20x20px
        """
        super(Jeu, self).__init__()
        self.Largeur = Nombre_cases_Largeur
        self.Hauteur = Nombre_cases_hauteur
        self.carte   = la_carte
        self.joueur  = le_joueur
        self.regles  = liste_des_regles
        self.Taille_case_pixel = 20
        self.etat = Etat()

        pygame.init()
        pygame.display.set_caption("NSI_Labyrinthe")
        self.fenetre = pygame.display.set_mode( (self.Taille_case_pixel*self.Largeur,self.Taille_case_pixel*self.Hauteur))
        self.tick_rate = 25
        pygame.key.set_repeat(100,100)
        self.actions = {K_SPACE:espace,
                    K_UP:haut,
                    K_w:haut,
                    K_DOWN:bas,
                    K_s:bas,
                    K_LEFT:droite,
                    K_a:droite,
                    K_RIGHT:gauche,
                    K_d:gauche}
        self.images = dict()
        for cle, img  in liste_des_images :
            self.images[cle]= self.importer_image_transparente(img)

    def coller_image(self,cle_image,X,Y) : # attention l'ordre compte
        """ Fonction qui position une image dans la fenetre
        entree :
            * numero de l'image prechargee.
            * coordonee X sur la grille
            * coordonee Y sur la grille
            """
        self.fenetre.blit(self.images[cle_image]
                         ,(self.Taille_case_pixel*X,self.Taille_case_pixel*Y))

    def gerer_evenement(self):
        """ fonction qui gere les evenements"""
        for event in pygame.event.get(): # on parcours les evenements recu depuis la derniere mise a jour.
            if event.type == QUIT: # si on demande au programme de se fermer.
                return False # pour faire l'arret
            if event.type == KEYDOWN :
                if event.key in self.actions :
                    self.carte.sauver_etat() # pour la gestion des regles
                    self.joueur.sauver_etat() # pour la gestion des regles
                    self.actions[event.key](self.carte,self.joueur,self.etat)
                    # regles
                    for regle in self.regles :
                        stop = regle(self.carte,self.joueur,self.etat)
                print(self.joueur)
        return self.etat.en_cours # on continue

    def dessiner(self):
        """
        fonction qui dessine la fenetre de jeu, la procedure est :
        1 - remplit le fond en noir
        2 - coller chaque morceau de carte
        3 - coller le personnage
        """
        self.fenetre.fill((0,0,0))
        for i,colonne in enumerate(self.carte.tableau_cases) :
            for j, cle_image in enumerate(colonne) :
                if cle_image is not None:
                    self.coller_image(cle_image,i,j)
        self.coller_image("personnage",self.joueur.X,self.joueur.Y)

    def lancer_jeu(self):
        """ boucle de jeu a proprement parler elle suis le schema de description de la classe"""
        rafraichisement =pygame.time.Clock()
        self.dessiner()
        Execution_en_cours = True
        while Execution_en_cours :
            Execution_en_cours = self.gerer_evenement()
            self.dessiner()
            pygame.display.flip() # mise a jour de l'ecran
            rafraichisement.tick(self.tick_rate) # 25 mise a jour par secondes
        pygame.quit()
