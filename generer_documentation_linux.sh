# Genere automatiquement la documentation est la met dans le repertoire doc du jeu
rm Site_Web/static/Documentation/*
cd Code_jeu
for fic in *.py; do
    module="${fic%.py}"
    python3 -m pydoc -w $module
done
echo "Documentation Générée"
#sed 's#&nbsp;# #g'  -i *.html
#sed 's#<font.*>##g' -i *.html
#sed 's#.*=.*\">*##g' -i *.html
mv *.html ../Site_Web/static/Documentation/
