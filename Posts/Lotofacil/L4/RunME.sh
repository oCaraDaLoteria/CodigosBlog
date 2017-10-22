#!/bin/bash

mkdir RESULTADOS
python criar_BD_lotofacil.py
./BaixarConcursos.sh
clear
python _atualizar_BD.py
python L4_01_Eficacia.py
clear
python L4_02_Acertar_N_Fixos.py
clear
python L4_03_Curva_Acertos.py
clear
rm *.pyc
echo "Terminado"
