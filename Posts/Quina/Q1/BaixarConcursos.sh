#!/bin/bash
# Atualiza concursos da Quina no Banco De Dados

wget http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_quina.zip
clear
echo "Baixou Quina"

unzip D_quina.zip -d D_quina
rm D_quina.zip

python html2csv.py D_quina/D_QUINA.HTM
cut -d, -f1,2,8-22 --complement D_quina/D_QUINA.csv > D_quina/temp.csv
cut -d, -f6-13 --complement D_quina/temp.csv > D_quina/temp2.csv
awk -F, 'length>NF+1' D_quina/temp2.csv > D_quina/temp3.csv
perl -pe 's/"//g' D_quina/temp3.csv >  D_quina/temp4.csv
rm D_quina/D_QUINA.csv
mv D_quina/temp4.csv D_quina/D_QUINA.csv
mv D_quina/D_QUINA.csv D_QUINA.csv
rm D_quina/*.*
rmdir D_quina/


python _atualizar_BD.py
