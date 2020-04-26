# NSI_labyrinthe
Support pour projet élève de codage d'un labyrinthe et de ses règles  

# prérequis
Les modules pygame et pytest sont nécessaires.
S'il ne sont pas déja installé la commande est :
- Sur linux :
   - pip3 install pygame
   - pip3 install pytest
- Sur windows :
  - pip install pygame
  - pip install pytest

# Utilisation de git
Le code est accessible à l'adresse :  
https://github.com/aulery/NSI_labyrinthe.git
pour le copier localement et travailler taper :
- Aller dans le répertoire ou vous voulez copier le projet :
- Tapez : git clone https://github.com/aulery/NSI_labyrinthe.git
- Se créer un compte sur le site de github
- Lancer Atom et faire ouvrir un dossier dans le répertoire que vous venez de télécharger.
- Avec Atom Créer une branche pour vous et lancez vous dans l'aventure.


# Structure du projet :
  - Code_jeu : contient le code python du jeu
      * images : contient les images qui seront utilisée pour le jeu.
      * jeu_de_test : contient les codes python des test unitaires fait avec Pytest
  - Site_Web : contient un exemple minimal d'un site web gérer avec Fflask
      * static : contient les images du site web
          + Documentation : contient la documentation autogénérée par python
      * templates : contient les modèles  utilisés par Flask

# Générer la documentation
Pour que python génère une série de pages web reprenant la documentation incluse dans le code, exécuter le script prévu à cet effet :
- Sur linux : generer_documentation_linux.sh
- Sur windows : generer_documentation_win.sh


La documentation est mise dans Site_Web/static/Documentation

# Exécuter le jeu
Dans le repertoire Code_jeu, taper la commande  :
- Sur linux : python3 main.py
- Sur windows : py main.py

# Lancer le site web
Dans le repertoire Site_web, taper la commande :
- Sur linux : python3 site_web.py
- Sur windows : py site_web.py
Pour accéder au site web, ouvrir le navigateur et accéder à la page :
http://localhost:5000/


# Exécuter les tests de validation
Dans le repertoire Code_jeu, taper la commande  :
- Sur linux : python3 -m  pytest
- Sur windows : py -m pytest
Pour plus d'information ajouter l'option -v :
- Sur linux : python3 -m  pytest  -v
- Sur windows : py -m pytest -v

Pour une exécutions continue des test toutes les X secondes :
- Sur linux : watch -n X --color "python3 -m pytest -v -s --color=yes"
- Sur windows : while (1){py -m pytest -v ;sleep X}
Faire CTRL+C pour interrompre
