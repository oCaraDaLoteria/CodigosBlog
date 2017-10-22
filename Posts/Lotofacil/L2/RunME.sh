#!/bin/bash

python criar_BD_lotofacil.py
./BaixarConcursos.sh
clear
python _atualizar_BD.py
python L2.py
clear
rm *.pyc
echo "Terminado"
