# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
"""
Ensemble de décorateur pour le suivi des statistiques
Pas pour les elèves donc pas de test unitaires.
"""
from functools import wraps
def suivi_statistiques_joueur(fonction):
    """
    decorateur pour le suivi des statistiques d'utilisation des Touches
    par un joueur dans un dictionnaire stats

    dans l'absolue je devrai creer un décorateur' ou une super classe
    afin d'inclure automatiquement le suivi.
    """
    @wraps(fonction)
    def fonction_avec_stat(carte,personnage,etat):
        if fonction.__name__ in personnage.stats :
            personnage.stats[fonction.__name__] +=1
        else :
            personnage.stats[fonction.__name__] =1
        fonction(carte,personnage,etat)
    return fonction_avec_stat

def suivi_statistiques_interne(fonction):
    """
    decorateur pour le suivi des statistiques d'utilisation des Touches par un joueur
    """
    @wraps(fonction)
    def fonction_avec_stat(self):
        if fonction.__name__ in self.stats :
            self.stats[fonction.__name__] +=1
        else :
            self.stats[fonction.__name__] =1
        fonction(self)
    return fonction_avec_stat

def ajout_statistique_ponctuelle(classe,cle):
    """ fonction pour l'ajout d'une statistiques
        Entrée :
        classe a modifier
        cle string qui definie la clé dans le dictionnaire
    """
    if cle in classe.stats :
        classe.stats[cle] +=1
    else :
        classe.stats[cle] =1
