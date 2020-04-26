# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
import copy

from Statistiques import suivi_statistiques_interne
class joueur():
    """docstring for joueur.
    classe qui contient toute les informations sur le joueur
    On accedera a sa position en faisant :
    var_joueur.X et var_joueur.Y
    """

    def __init__(self, nom,X,Y,score = 0):
        """ initialisation
        Entrée :
        * nom : le nom d'un joueur
        * X : position de depart sur l'axe X
        * Y : position de depart sur l'axe Y
        * stats : statistiques du joueur
        par default contient un "score" qui par defaut est a 0
        """

        assert type(X) is int, "X doit être entier"
        assert type(Y) is int, "Y doit être entier"
        super(joueur, self).__init__()
        self.nom = nom
        self.X = X
        self.Y = Y
        self.stats ={"score":score}
        self.old_X = X
        self.old_Y = Y


    def __str__ (self):
        """ permet de faire print(joueur) directement """
        return self.nom + " est la position " + str(self.X)+ ":"+ str(self.Y)

    def deplacer(self,DX,DY) :
        """ fonction pour deplacer un joueur dans la grille.
        entrée :
        DX deplacement dans la Largeur
        DY deplacement dans la Hauteur
        """
        assert isinstance(DX,int)
        assert isinstance(DY,int)

        self.X = self.X + DX
        self.Y = self.Y + DY

    @suivi_statistiques_interne
    def annuler_coup(self):
        """ fonction qui restaure la position sauvegarder lors de l'appel de sauver_etat()
        """
        self.X = self.old_X
        self.Y = self.old_Y

    def sauver_etat(self):
        """ fonction qui enregistre la position actuelle. une sauvegarde est faites avant chaque evenement
        a coupler avec annuler_coup() .
        """
        self.old_X = self.X
        self.old_Y = self.Y

    def position(self):
        """ Retourne un couple X,Y contenant la position du joueur """
        return (self.X,self.Y)

    def afficher_statistiques(self):
        """ affiche de maniere brute les statistiques """
        print(self.stats)

    def recuperer_statistiques(self):
        """ renvoi le dictionnaire des statistiques """
        return self.stats

    def remplacer_statistiques(self,dictionnaire_des_statistiques):
        """ remplace les statistiques par un nouveau jeu complet """
        self.stats = copy.copy(dictionnaire_des_statistiques)

    def modifier_statistiques(self,cle, valeur):
        """ remplace le valeur d'une statistique par une nouvelle """
        self.stats[cle] = valeur
