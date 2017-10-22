#!/bin/bash

python criar_BD_megasena.py
./BaixarConcursos.sh
clear
python _atualizar_BD.py
python M1.py
clear
rm *.pyc
echo "Terminado"
