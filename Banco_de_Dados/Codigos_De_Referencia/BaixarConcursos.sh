#!/bin/bash
# Atualiza concursos


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
#------------------------------------------------------------------

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
#--------------------------------------------------------------------

wget http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_quina.zip
clear 
echo "Baixou Quina"

unzip D_quina.zip -d D_quina
rm D_quina.zip
python html2csv.py D_quina/D_QUINA.HTM
cut -d, -f1,2,8-42 --complement D_quina/D_QUINA.csv > D_quina/temp.csv
awk -F, 'length>NF+1' D_quina/temp.csv > D_quina/temp2.csv
perl -pe 's/"//g' D_quina/temp2.csv >  D_quina/temp3.csv
rm D_quina/temp.csv
rm D_quina/temp2.csv
rm D_quina/D_QUINA.csv
mv D_quina/temp3.csv D_quina/D_QUINA.csv
mv D_quina/D_QUINA.csv D_QUINA.csv
rm D_quina/*.*
rmdir D_quina/
clear 
echo "Tudo pronto"