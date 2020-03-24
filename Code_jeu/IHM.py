# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
import os
import pygame # import total on limitera plus tard les besoins au minimum
from pygame.locals import * # pas obligatoire mais plus simple
from Touches import *

def importer_image_de_fond(nom,repertoire="Images"):
    """ Fonction qui importe une image sans transparence.
    entrée :
        * nom string: le nom de l'image avec extension
        * repetoire : le nom du repertoire par default Code_jeu/Images
    sortie :
        * une image convertie utilisable par pygame avec fond noir en cas de transparence
    """
    return pygame.image.load(os.path.join(repertoire,nom)).convert()

def importer_image_transparente(nom,repertoire="Images"):
    """ Fonction qui importe une image avec transparence.
    entrée :
        * nom string: le nom de l'image avec extension
        * repetoire string : le nom du repertoire par default Code_jeu/Images
    sortie :
        * une image convertie utilisable par pygame avec transparence
    """
    return pygame.image.load(os.path.join(repertoire,nom)).convert_alpha()

def coller_image(image,largeur,hauteur,fenetre) : # attention l'ordre compte
    """ Fonction qui position une image dans la fenetre
    entrée :
        * image format image (obtenue avec importer_image_XXXXXX ): L'image a positionner.
        * largeur entier : position horizontale de l'objet.
        * hauteur entier: position verticale de l'objet.
        * fenetre : fenetre utilisée pour l'affichage.
    sortie :
        * une image convertie utilisable par pygame avec fond noir en cas de transparence
    """
    fenetre.blit(image,(largeur,hauteur))

class Jeu():
    """ Classe qui gere le jeu.
        elle change l'etat du jeu 25 fois par secondes
        La boucle de jeu est la suivante :
        1 - sauvegarder la carte
        2 - verifier les interactions utilisateurs voir https://www.pygame.org/docs/ref/event.html
        3 - verifier les règles du jeu. et annuler si besoin
        4 - afficher la carte puis le joueur.

    """

    def __init__(self, Nombre_cases_largeur,Nombre_cases_hauteur,la_carte,le_joueur,liste_des_regles,liste_des_images):
        super(Jeu, self).__init__()
        self.Largeur = Nombre_cases_largeur
        self.Hauteur = Nombre_cases_hauteur
        self.carte   = la_carte
        self.joueur  = le_joueur
        self.regles  = liste_des_regles
        self.Taille_case_pixel = 20
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
        for i,img in enumerate(liste_des_images) :
            self.images[i]= importer_image_transparente(img)

    def gerer_evenement(self):
        for event in pygame.event.get(): # on parcours les évenements reçu depuis la dernière mise à jour.
            if event.type == QUIT: # si on demande au programme de se fermer.
                return False # pour faire l'arret
            if event.type == KEYDOWN :
                if event.key in self.actions :
                    self.actions[event.key](self.carte,self.joueur)
                print(self.joueur)
        return True # on continue

    def dessiner(self):
        self.fenetre.fill((0,0,0))
        for i,colonne in enumerate(self.carte.tab) :
            for j, numero_image in enumerate(colonne) :
                if numero_image is not None:
                    coller_image(self.images[numero_image]
                                ,self.Taille_case_pixel*i
                                ,self.Taille_case_pixel*j
                                ,self.fenetre)
        coller_image(self.images[0],
                     self.joueur.X*self.Taille_case_pixel,
                     self.joueur.Y*self.Taille_case_pixel
                     ,self.fenetre)

    def lancer_jeu(self):
        rafraichisement =pygame.time.Clock()
        self.dessiner()
        Execution_en_cours = True
        while Execution_en_cours :
            #interception des evenements
            self.carte.sauver_etat() # pour la gestion des regles
            self.joueur.sauver_etat() # pour la gestion des regles
            Execution_en_cours = self.gerer_evenement()
            # regles
            for regle in self.regles :
                regle(self.carte,self.joueur)
            # dessin de la carte
            self.dessiner()
            pygame.display.flip() # mise à jour de l'écran
            rafraichisement.tick(self.tick_rate) # 25 mise à jour par secondes

        pygame.quit()
