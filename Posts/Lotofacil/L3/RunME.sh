#!/bin/bash

python criar_BD_lotofacil.py
./BaixarConcursos.sh
clear
python _atualizar_BD.py
python L3.py
clear
rm *.pyc
echo "Terminado"
