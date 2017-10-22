#!/bin/bash
# Atualiza concursos da Lotofacil no Banco De Dados

wget http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip
clear
echo "Baixou Lotofacil"

unzip D_lotfac.zip -d D_lotfac
rm D_lotfac.zip

python html2csv.py D_lotfac/D_LOTFAC.HTM
cut -d, -f1,2,18-42 --complement D_lotfac/D_LOTFAC.csv > D_lotfac/temp.csv
awk -F, 'length>NF+1' D_lotfac/temp.csv > D_lotfac/temp2.csv
perl -pe 's/"//g' D_lotfac/temp2.csv >  D_lotfac/temp3.csv
rm D_lotfac/temp.csv
rm D_lotfac/temp2.csv
rm D_lotfac/D_LOTFAC.csv
mv D_lotfac/temp3.csv D_lotfac/D_LOTFAC.csv
mv D_lotfac/D_LOTFAC.csv D_LOTFAC.csv
rm D_lotfac/*.*
rmdir D_lotfac
clear
echo "Pronto"
