# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
import copy
class carte() :
    """
    classe qui contient la description de la carte.
    Entrée  :
    Hauteur taille dans la premiere direction de la carte (en case)
    Largeur taille dans la deuxieme direction de la carte (en case)

    genere :
    tab : un tableau de Hauteur*Largeur cases à None
    """

    def __init__(self,Hauteur,Largeur):
        """ initialisation de la carte """
        super(carte,self).__init__()
        self.Hauteur = Hauteur
        self.Largeur = Largeur

        # construction du tableau tab, par append car par comprehension des effets
        # de bords apparaisent
        self.tab = []
        inter = Largeur*[None]
        for i in range(Hauteur):
            self.tab.append(copy.copy(inter))

        self.old_tab = self.tab

    def __str__(self):
        """ fonction qui permet d'afficher la carte dans la console """
        chaine_globale = "Impression de la carte\n"
        for j in range (len(self.tab[0])):
            for i in range(len(self.tab)) :
                if self.tab[i][j] is None :
                    chaine_globale += " "
                else :
                    chaine_globale +=str(self.tab[i][j])
            chaine_globale += "\n"
            chaine_globale += "Fin de la carte"
        return chaine_globale

    def modifier_case(self,X,Y,nouvelle_case):
        self.tab[X][Y]= nouvelle_case

    def redefinir_carte(self,nouvelle_carte) :
        try :
            nouvelle_carte[0][0] is not None
        except :
            self.assert_(False, "la nouvelle carte n'est pas 2D")

        assert len(nouvelle_carte) == len(self.tab)
        assert len(nouvelle_carte[0]) == len(self.tab[0])
        self.tab = copy.copy(nouvelle_carte)

    def sauver_etat(self):
        """ fonction qui enregistre la position actuelle. une sauvegarde est faites avant chaque evenement
        a coupler avec annuler_coup() .
        """
        self.old_tab = self.tab

    def annuler_coup(self):
        """ fonction qui restaure la configuration sauvegarder lors de l'appel de sauver_etat()
        """
        self.tab = self.old_tab

    def lire_carte(self,nom_fichier):
        """
        fonction qui permet de lire dans un fichier la carte utilisée
        entrée :  un str qui contient le nom du fichier. attention le chemin dois être relatif
        """
        with  open(nom_fichier, "r") as fichier :
            contenu = fichier.read()
            print(contenu)

    def sauvegarder_carte(self,nom_fichier):
        """
        fonction qui permet d'écrire dans un fichier la carte  génrée
        entrée :  un str qui contient le nom du fichier. attention le chemin dois être relatif
        """
        with  open(nom_fichier, "w") as fichier :
            chaine = str(self.Hauteur) + " " + str(self.Largeur) + "\n"
            fichier.write(chaine)

    def copie_carte(self):
        """ retourne une copie du tableau gerant la carte """
        return copy.copy(self.tab)
