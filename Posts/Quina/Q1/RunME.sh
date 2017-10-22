#!/bin/bash

python criar_BD_quina.py
./BaixarConcursos.sh
clear
python _atualizar_BD.py
python Q1.py
clear
rm *.pyc
echo "Terminado"
