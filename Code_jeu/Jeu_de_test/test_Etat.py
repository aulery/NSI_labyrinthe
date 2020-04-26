# coding: utf8
# pensez a recopier l'encodage dans chaque fichier Python
import Etat

def test_creation():
    etat_de_test  = Etat.Etat()
    assert etat_de_test.en_cours

def test_fin_de_partie():
    etat_de_test  = Etat.Etat()
    etat_de_test.fin_de_partie()
    assert not etat_de_test.en_cours #il est a false

def test_recuperer_statistiques():
    etat_de_test  = Etat.Etat()
    etat_de_test.stats["cle_de_test"] = 123
    etat_de_test.stats["cle_de_test2"] = 2123
    assert etat_de_test.recuperer_statistiques() == {"cle_de_test":123,"cle_de_test2":2123}

def test_recuperer_statistiques():
    etat_de_test  = Etat.Etat()
    etat_de_test.stats["cle_de_test"] = 123
    etat_de_test.stats["cle_de_test2"] = 2123
    assert etat_de_test.recuperer_statistiques() == {"cle_de_test":123,"cle_de_test2":2123}

def test_modifier_statistiques():
    etat_de_test = Etat.Etat()
    etat_de_test.modifier_statistiques("cle_de_test2",2123)
    assert etat_de_test.recuperer_statistiques() == {"cle_de_test2":2123}
