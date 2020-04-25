# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
import Joueur
import pytest

def test_creation():
    with pytest.raises(AssertionError):
        joueur_de_test  = Joueur.joueur("toto",11,189.3)
    with pytest.raises(AssertionError):
        joueur_de_test  = Joueur.joueur("toto",11.3,189)
    joueur_de_test  = Joueur.joueur("toto",12,189)
    assert joueur_de_test.X == 12
    assert joueur_de_test.Y == 189
    assert joueur_de_test.nom == "toto"
    assert joueur_de_test.stats["score"] == 0
    joueur_de_test  = Joueur.joueur("toto",12,189,score = 28)
    assert joueur_de_test.stats["score"] == 28

def test_deplacer():
    joueur_de_test  = Joueur.joueur("toto",12,189)
    with pytest.raises(AssertionError):
        joueur_de_test  = joueur_de_test.deplacer(1,0.1)
    with pytest.raises(AssertionError):
        joueur_de_test  = joueur_de_test.deplacer(0.1,1)
    joueur_de_test  = joueur_de_test.deplacer(1,1)

def test_sauver_etat():
    joueur_de_test  = Joueur.joueur("toto",12,189)
    joueur_de_test.sauver_etat()
    assert joueur_de_test.old_X == 12
    assert joueur_de_test.old_Y == 189

def test_annuler_coup():
    joueur_de_test  = Joueur.joueur("toto",12,189)
    joueur_de_test.sauver_etat()
    joueur_de_test.deplacer(1,1)
    joueur_de_test.annuler_coup()
    assert joueur_de_test.old_X == 12
    assert joueur_de_test.old_Y == 189

def test_position():
    joueur_de_test  = Joueur.joueur("toto",12,189)
    assert joueur_de_test.position() == (12,189)

def test_recuperer_statistiques():
    joueur_de_test  = Joueur.joueur("toto",12,189)
    joueur_de_test.stats["cle_de_test"] = 123
    joueur_de_test.stats["cle_de_test2"] = 2123
    assert joueur_de_test.recuperer_statistiques() == {"cle_de_test":123,
                                                       "cle_de_test2":2123,
                                                       "score":0}
