import numpy as np
from funcoes_e_etc import *

# ---------- Inicializacao --------------------
loto = Loterias('Lotofacil')
n_concursos = loto.n_concursos + 1

acertos_referencia = np.array(())
acertos_estudado = np.array(())
bolao = np.zeros((6,15))



print('Trabalhando')
for game_id in range(2,n_concursos):
    concurso_anterior = loto.concursos[game_id-1]
    bolao_estudado = fazer_bolao(concurso_anterior)

    resposta = loto.concursos[game_id]
    acertos_estudado = np.concatenate(  (acertos_estudado, Contar_Acertos(bolao_estudado,resposta)) )

    # --------- curva de referencia ----------------
    bolao_referencia = loto.criar_bolao_aleatorio(6)
    acertos_referencia = np.concatenate(  (acertos_referencia,Contar_Acertos(bolao_referencia, resposta)) )
    # print('%.2f' %  (100.0*(game_id+1)/(n_concursos-1)) )


HistogramaComparacao(acertos_referencia, acertos_estudado,loto.nome_loteria,'L1.png')
print('Terminado')
