# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
import os
import pygame # import total on limitera plus tard les besoins au minimum
from pygame.locals import * # pas obligatoire mais plus simple
from Code_jeu.Touches import actions
def importer_image_de_fond(nom,repertoire="Code_jeu/Images"):
    """ Fonction qui importe une image sans transparence.
    entrée :
        * nom string: le nom de l'image avec extension
        * repetoire : le nom du repertoire par default Code_jeu/Images
    sortie :
        * une image convertie utilisable par pygame avec fond noir en cas de transparence
    """
    return pygame.image.load(os.path.join(repertoire,nom)).convert()

def importer_image_transparente(nom,repertoire="Code_jeu/Images"):
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

def toto() :
    print("toto")
# debut du programme

print("executé depuis ", os.getcwd())
pygame.init()
pygame.display.set_caption("NSI_Labyrinthe")
rafraichisement =pygame.time.Clock()

Hauteur, Largeur = 640 ,480
fenetre = pygame.display.set_mode( (Hauteur, Largeur), RESIZABLE )

fond = importer_image_de_fond("background.jpg")
goomba = importer_image_transparente('goomba.png')

coller_image(fond,0,0,fenetre)
coller_image(goomba,50,0,fenetre)

dico= {QUIT:toto}
Execution_en_cours = True
while Execution_en_cours :
    for event in pygame.event.get(): # on parcours les évenements reçu depuis la dernière mise à jour.
        if event.type == QUIT: # si on demande aun programme de se fermer.
            Execution_en_cours = False
        if event.type in dico :
            dico[event.type]()
            # fonction qui vide la mémoire à coder
        if event.type == KEYDOWN :
            actions(event.key)

    pygame.display.flip() # mise à jour de l'écran

    rafraichisement.tick(25) # 25 mise à jour par secondes

pygame.quit()
