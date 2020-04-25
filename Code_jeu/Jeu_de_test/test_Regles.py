# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
import Regles
import Joueur
import Carte
import Etat


def test_on_ne_sort_pas_de_la_carte():
    carte_de_test = Carte.carte(3,3)
    joueur_de_test  = Joueur.joueur("toto",1,0)
    etat_de_test = Etat.Etat()

    joueur_de_test.deplacer(10,0)
    Regles.on_ne_sort_pas_de_la_carte(carte_de_test,joueur_de_test,etat_de_test)
    assert joueur_de_test.position() == (1,0)

    joueur_de_test.deplacer(0,10)
    Regles.on_ne_sort_pas_de_la_carte(carte_de_test,joueur_de_test,etat_de_test)
    assert joueur_de_test.position() == (1,0)

    joueur_de_test.deplacer(1,2)
    Regles.on_ne_sort_pas_de_la_carte(carte_de_test,joueur_de_test,etat_de_test)
    assert joueur_de_test.position() == (2,2)

def test_victoire():
    carte_de_test = Carte.carte(3,3)
    joueur_de_test  = Joueur.joueur("toto",1,0)
    etat_de_test = Etat.Etat()

    carte_de_test.modifier_case(1,0,1)
    Regles.victoire(carte_de_test,joueur_de_test,etat_de_test)
    assert etat_de_test.en_cours == True

    carte_de_test.modifier_case(1,0,2)
    Regles.victoire(carte_de_test,joueur_de_test,etat_de_test)
    assert etat_de_test.en_cours == False
