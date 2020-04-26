# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python

class Etat():
    """
    Contient l'etat de la partie
    basiquement permet de savoir si la partie se fini.

    """

    def __init__(self):
        """ construction de la classes
        entrée :
        - aucune

        Attribut
        * en_cours : dit si la partie est encore en cours
        """
        super(Etat, self).__init__()
        self.en_cours = True
        self.stats = dict()

    def fin_de_partie(self):
        """
        met l'attribut en cours a False
        """
        self.en_cours = False

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
