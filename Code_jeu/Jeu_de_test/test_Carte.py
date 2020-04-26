# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python

import Carte


def test_creation():
    carte_de_test = Carte.carte(3,4)
    assert carte_de_test.Largeur == 3
    assert carte_de_test.Hauteur == 4
    assert carte_de_test.tableau_cases == [[None,None,None,None]
                                ,[None,None,None,None]
                                ,[None,None,None,None]]
    assert carte_de_test.stats == dict()
    assert carte_de_test.old_tableau_cases == [[None,None,None,None]
                                    ,[None,None,None,None]
                                    ,[None,None,None,None]]

def test_modifier_case():
    carte_de_test = Carte.carte(1,1)
    carte_de_test.modifier_case(0,0,1)
    assert carte_de_test.tableau_cases[0][0] == 1

def test_dimension():
    carte_de_test = Carte.carte(47,23)
    assert carte_de_test.dimensions() == (47,23)

def test_copie_carte():
    carte_de_test = Carte.carte(2,3)
    carte_de_test.modifier_case(0,0,1)
    carte_de_test.modifier_case(1,0,2)
    carte_de_test.modifier_case(0,1,0)
    carte_de_test.modifier_case(1,1,3)
    assert carte_de_test.copie_carte() == [[1,0,None],[2,3,None]]

def test_redefinir_carte():
    carte_de_test = Carte.carte(2,2)
    nouvelle_carte = [[0,1],[2,3]]
    carte_de_test.redefinir_carte(nouvelle_carte)
    assert carte_de_test.copie_carte() == [[0,1],[2,3]]

def test_modifier_statistiques():
    carte_de_test = Carte.carte(2,2)
    carte_de_test.modifier_statistiques("cle_de_test2",2123)
    assert carte_de_test.recuperer_statistiques() == {"cle_de_test2":2123}

def test_recuperer_statistiques():
    carte_de_test = Carte.carte(2,2)
    carte_de_test.modifier_statistiques("cle_de_test",123)
    carte_de_test.modifier_statistiques("cle_de_test2",2123)
    assert carte_de_test.recuperer_statistiques() == {"cle_de_test":123,"cle_de_test2":2123}

def test_impression():
    carte_de_test = Carte.carte(2,3)
    carte_de_test.modifier_case(0,0,1)
    carte_de_test.modifier_case(1,0,2)
    carte_de_test.modifier_case(0,1,0)
    carte_de_test.modifier_case(1,1,3)
    carte_de_test.modifier_case(0,2,4)
    carte_de_test.modifier_case(1,2,5)
    attendu = "Impression de la carte\n12\n03\n45\nFin de la carte"
    assert carte_de_test.__str__() == attendu
    carte_de_test.modifier_case(1,2,None)
    attendu = "Impression de la carte\n12\n03\n4 \nFin de la carte"
    assert carte_de_test.__str__() == attendu
