#!/bin/bash
# Atualiza concursos da Megasena no Banco De Dados

wget http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip
clear 
echo "Baixou Megasena"

unzip D_megase.zip -d D_megase
rm D_megase.zip 

python html2csv.py D_megase/D_MEGA.HTM
cut -d, -f1,2,9-28 --complement D_megase/D_MEGA.csv > D_megase/temp.csv
awk -F, 'length>NF+1' D_megase/temp.csv > D_megase/temp2.csv
perl -pe 's/"//g' D_megase/temp2.csv >  D_megase/temp3.csv
rm D_megase/temp.csv
rm D_megase/temp2.csv
rm D_megase/D_MEGA.csv
mv D_megase/temp3.csv D_megase/D_MEGA.csv
mv D_megase/D_MEGA.csv D_MEGA.csv
rm D_megase/*.*
rmdir D_megase/
