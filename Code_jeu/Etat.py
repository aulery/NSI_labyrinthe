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

    def recuperer_Statistiques(self):
        """ renvoi le dictionnaire des statistiques """
        return self.stats
