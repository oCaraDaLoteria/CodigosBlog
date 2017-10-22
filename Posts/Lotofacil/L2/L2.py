import numpy as np
from funcoes_e_etc import *

# ---------- Inicializacao --------------------
loto = Loterias('Lotofacil')
n_concursos = loto.n_concursos + 1
acertos_referencia = np.zeros(n_concursos)
acertos_estudado = np.zeros(n_concursos)


#---------- obtenho as 8 dezenas fixas (numersos impares que mais sairam) ---------------------
HistogramaPizza(loto.concursos,loto.nome_loteria,'histograma.png','sim') # vejo a frequencia geral das dezenas

em_ordem = loto.estatisticas_sorteados
pares = [] # efetivamente nao faco nada com isso, mas esta aqui para futuro debug do codigo
impares = []
for i in range(0,len(em_ordem)): # separo os numeros pares e impares em vetores diferentes
    if (bool(em_ordem[i] & 1)):
        impares.append(em_ordem[i])
    else:
        pares.append(em_ordem[i])
oito_dezenas_impares_fixas = np.array(impares[-8:]) # pego os 8 numeros que mais se repetiram


print('Trabalhando')
for game_id in range(1,n_concursos):
    resposta = loto.concursos[game_id]
    acertos_referencia[game_id] = Contar_Acertos(loto.criar_jogo(), resposta)

    bolao = np.concatenate((sete_dezenas_pares(),oito_dezenas_impares_fixas))
    acertos_estudado[game_id] = Contar_Acertos(bolao, resposta)
    # print('%.2f' %  (100.0*(game_id+1)/(n_concursos-1)) )


# ------  o primeiro item de cada vetor devem ser removidos ---------
acertos_referencia = acertos_referencia[1:]
acertos_estudado = acertos_estudado[1:]

# ------  Exibe resultados ---------
# se desejado, fica a cargo do usuario alterar APENAS o nome da figura
HistogramaComparacao(acertos_referencia, acertos_estudado,loto.nome_loteria,'L2.png')
print('Terminado')
