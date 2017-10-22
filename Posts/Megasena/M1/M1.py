import numpy as np
from funcoes_e_etc import *


mega = Loterias('Megasena')
n_concursos = mega.n_concursos + 1

filtro = np.zeros(n_concursos)
sequencia = np.zeros(6)
acertos_referencia = np.zeros(n_concursos)
acertos_estudado = np.zeros(n_concursos)


for game_id in range(1,n_concursos):
# ---------- pego um resultado anterior --------------------
    concurso = mega.concursos[game_id]

# -------- crio jogos aleatorios para comparacao -----------------
    jogo_aleatorio = mega.criar_jogo()
    acertos_referencia[game_id] = Contar_Acertos(jogo_aleatorio,concurso)

# ------  crio varias sequencias aleatorias, ate o momento que um deles seja aceitavel ---------
    variavel_controle = 0
    while (variavel_controle == 0):
        sequencia_ok = mega.criar_jogo()
        if (filtro_4qdt(sequencia_ok) == 1):
            variavel_controle = 1

    acertos_estudado[game_id] = Contar_Acertos(sequencia_ok,concurso)
    print('%.2f' %  (100.*(game_id)/(n_concursos-1)) )



acertos_estudado = acertos_estudado[1:]
acertos_referencia = acertos_referencia[1:]
HistogramaComparacao(acertos_referencia, acertos_estudado,mega.nome_loteria,'M1.png')
