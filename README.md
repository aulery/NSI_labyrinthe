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
Le code est accéssible

# Structure du projet :
  - Code_jeu : contient le code python du jeu
      * images : contient les images qui seront utilisée pour le jeu.
      * jeu_de_test : contient les codes python des test unitaires fait avec pytest
  - Site_Web : contient un exemple minimal d'un site web gérer avec flask
      * static : contient les images du site web
          + Documentation : contient la documentation autogénéré par python
      * templates : contients les templates utilisée par flask

# Générer la documentation
Exécuter le script generer_documentation.sh pour que python génère une série de pages web utilisable reprenant toute la documentation du code.
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
