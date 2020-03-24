# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
import os
import pygame # import total on limitera plus tard les besoins au minimum
from pygame.locals import * # pas obligatoire mais plus simple

def importer_image_de_fond(nom,repertoire="Code_jeu/Images"):
    """ Fonction qui importe une image sans transparence.
    entrée :
        * nom string: le nom de l'image avec extension
        * repetoire : le nom du repertoire
    Par default les
     """
    return pygame.image.load(os.path.join(repertoire,nom)).convert()

def importer_image_transparente(nom,repertoire="Code_jeu/Images"):
    return pygame.image.load(os.path.join(repertoire,nom)).convert_alpha()

def coller_image(image,position_x,position_y,fenetre) : # attention l'ordre compte
    fenetre.blit(image,(position_x,position_y))

# debut du programme

print("execute depuis", os.getcwd())
pygame.init()
pygame.display.set_caption("NSI_Labyrinthe")
rafraichisement =pygame.time.Clock()

Hauteur, Largeur = 640 ,480
fenetre = pygame.display.set_mode( (Hauteur, Largeur), RESIZABLE )

fond = importer_image_de_fond("background.jpg")
goomba = importer_image_transparente('goomba.png')

coller_image(fond,0,0,fenetre)
coller_image(goomba,0,0,fenetre)



Execution_en_cours = True
while Execution_en_cours :
    for event in pygame.event.get(): # on parcours les évenements reçu depuis la dernière mise à jour.
        if event.type == QUIT: # si on demande aun programme de se fermer.
            Execution_en_cours = False
            # fonction qui vide la mémoire à coder

    pygame.display.flip() # mise a jour de l'écran

    rafraichisement

pygame.quit()
