# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
import copy
class carte() :
    """
    classe qui contient la description de la carte.
    Entrée  :
    Hauteur taille dans la premiere direction de la carte (en case)
    Largeur taille dans la deuxieme direction de la carte (en case)

    attribue :
    Hauteur : hauteur de la carte
    Largeur : Largeur de la carte
    tab : un tableau de Hauteur*Largeur cases à None
    """

    def __init__(self,Largeur,Hauteur):
        """ initialisation de la carte """
        super(carte,self).__init__()
        self.Hauteur = Hauteur
        self.Largeur = Largeur

        # construction du tableau tab, par append car par comprehension des effets
        # de bords apparaisent
        self.tableau_cases = []
        inter = Hauteur*[None]
        for i in range(Largeur):
            self.tableau_cases.append(copy.copy(inter))

        self.old_tableau_cases = self.tableau_cases
        self.stats = dict()

    def __str__(self):
        """ fonction qui permet d'afficher la carte dans la console
        NE PAS TOUCHER !!!!!
        """
        chaine_globale = "Impression de la carte\n"
        for j in range (len(self.tableau_cases[0])):
            for i in range(len(self.tableau_cases)) :
                if self.tableau_cases[i][j] is None :
                    chaine_globale += " "
                else :
                    chaine_globale +=str(self.tableau_cases[i][j])
            chaine_globale += "\n"
        chaine_globale += "Fin de la carte"
        return chaine_globale

    def modifier_case(self,X,Y,nouvelle_case):
        self.tableau_cases[X][Y]= nouvelle_case

    def redefinir_carte(self,nouvelle_carte) :
        try :
            nouvelle_carte[0][0] is not None
        except :
            self.assert_(False, "la nouvelle carte n'est pas 2D")

        assert len(nouvelle_carte) == len(self.tableau_cases)
        assert len(nouvelle_carte[0]) == len(self.tableau_cases[0])
        self.tableau_cases = copy.copy(nouvelle_carte)

    def sauver_etat(self):
        """ fonction qui enregistre la position actuelle.
        Une sauvegarde est faites avant chaque evenement
        a coupler avec annuler_coup() .
        """
        self.old_tableau_cases = self.tableau_cases

    def annuler_coup(self):
        """ fonction qui restaure la configuration sauvegarder lors de l'appel de sauver_etat()
        """
        self.tableau_cases = self.old_tableau_cases

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
        return copy.copy(self.tableau_cases)

    def dimensions(self):
        """ retourne les dimensions de la carte dans un tuple"""
        return (self.Largeur,self.Hauteur)

    def afficher_statistiques(self):
        """ affiche de maniere brute les statistiques """
        print(self.stats)

    def recuperer_statistiques(self):
        """ renvoi le dictionnaire des statistiques """
        return self.stats
