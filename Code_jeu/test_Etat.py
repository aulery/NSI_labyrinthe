import Etat

etat_de_test  = Etat.Etat()

def test_creation():
    assert etat_de_test.en_cours

def test_fin_de_partie():
    etat_de_test.fin_de_partie()
    assert not etat_de_test.en_cours #il est a false

def test_recuperer_statistiques():
    etat_de_test.stats["cle_de_test"] = 123
    etat_de_test.stats["cle_de_test2"] = 2123
    assert etat_de_test.recuperer_Statistiques() == {"cle_de_test":123,"cle_de_test2":2123}
