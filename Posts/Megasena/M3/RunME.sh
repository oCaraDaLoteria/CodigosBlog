#!/bin/bash

python criar_BD_megasena.py
./BaixarConcursos.sh
clear
python _atualizar_BD.py
python M3_01_probabilidade_linha.py
python M3_02_probabilidade_linha_NAO_sorteada.py
python M3_03_bolao_aleatorios.py
python M3_04_jogos_anteriores_com_fechamento.py
clear
rm *.pyc
echo "Terminado"
