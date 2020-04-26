# Genere automatiquement la documentation est la met dans le repertoire doc du jeu
rm Site_Web/static/Documentation/*
cd Code_jeu
pwd
for fic in *.py; do
    module="${fic%.py}"
    py -m pydoc -w $module
done

mv *.html ../Site_Web/static/Documentation/
