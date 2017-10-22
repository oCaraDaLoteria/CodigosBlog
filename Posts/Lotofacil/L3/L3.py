import numpy as np
from funcoes_e_etc import *

# ---------- Inicializacao --------------------
loto = Loterias('Lotofacil')
n_concursos = loto.n_concursos + 1
acertos_referencia = np.array(())
acertos_estudado = np.array(())
# --------- EDITE AQUI---------------
#concurso_anteriores = np.random.randint(1000) # deixe o pc escolher um numero
concurso_anteriores = 5
# --------- EDITE AQUI---------------


print('Trabalhando')
for game_id in range(concurso_anteriores+1,n_concursos-2):
    game_id_inicial = game_id-concurso_anteriores+1
    game_id_final = game_id+1
    game_id_resposta = game_id_final + 1
    #---------- obtenho as 13 dezenas fixas (numersos que mais sairam) ---------
    jogos_anteriores = loto.concursos[game_id_inicial:game_id_final]
    a,b=Histograma(jogos_anteriores,loto.nome_loteria) # a fucao Histograma alem de exibir um grafico (quando desejado), retorna valores de interesse
    em_ordem = sorted(range(len(a)), key=lambda k: a[k]) #ordem crescente de todos oos numeros que ja sorteados
    dezenas_fixas = np.array(em_ordem[-13:]) # pego os 13 numeros que mais se repetiram

    bolao_estudado = fazer_bolao(dezenas_fixas)
    resposta = loto.concursos[game_id_resposta]

    acertos_estudado = np.concatenate(  (acertos_estudado, Contar_Acertos(bolao_estudado,resposta)) )
    acertos_referencia = np.concatenate(  (acertos_referencia, Contar_Acertos(loto.criar_bolao_aleatorio(6), resposta)) )


HistogramaComparacao(acertos_referencia, acertos_estudado,loto.nome_loteria,'L3.png')
print('Terminado')
