# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python

class carte() :
    """docstring for carte
    classe qui contient la description de la carte.
    """

    def __init__(self,Hauteur,Largeur):
        super(carte,self).__init__()
        self.Hauteur = Hauteur
        self.Largeur = Largeur
        self.tab = Hauteur*[Largeur*[None]]
        self.old_tab = self.tab

    def modifier_case(self,X,Y,nouvelle_case):
        self.tab[X][Y]= nouvelle_case

    def redefinir_carte(self,nouvelle_carte) :
        try :
            nouvelle_carte[0][0] is not None
        except :
            self.assert_(False, "la nouvelle carte n'est pas 2D")

        self.assert_(len(nouvelle_carte) == len(self.tab))
        self.assert_(len(nouvelle_carte[0]) == len(self.tab[0]))
        slef.tab = nouvelle_carte

    def sauver_etat(self):
        self.old_tab = self.tab

    def annuler_coup(self):
        self.tab = self.old_tab
