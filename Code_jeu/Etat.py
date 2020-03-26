# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
class Etat():
    """
    Contient l'etat de la partie
    basiquement permet juste de savoir
    si la partie se fini.

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
