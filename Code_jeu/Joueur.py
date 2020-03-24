# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
import copy
class joueur():
    """docstring for joueur.
    classe qui contient toute les informations sur le joueeur
    """

    def __init__(self, nom,X,Y):
        super(joueur, self).__init__()
        self.nom = nom
        self.X = X
        self.Y = Y

    def __str__ (self):
        return self.nom + " est la position " + str(self.X)+ ":"+ str(self.Y)

    def __copy__(self):
        J2 = joueur(self.nom,self.X,self.Y)
        return J2

    def deplacer(self,DX,DY) :
        assert isinstance(DX,int)
        assert isinstance(DY,int)
        self.X = self.X + DX
        self.Y = self.Y + DY
