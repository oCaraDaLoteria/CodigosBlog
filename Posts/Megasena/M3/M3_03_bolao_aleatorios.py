from funcoes_e_etc import *

mega = Loterias('Megasena')
n_concursos = mega.n_concursos + 1

N_remover = 3 # ----- EDITE AQUI -----
acertos_referencia = np.zeros(n_concursos)
acertos_estudado = np.zeros(n_concursos)

for game_id in range(1,n_concursos):
# ---------- pego um resultado anterior --------------------
    concurso = mega.concursos[game_id]

# -------- crio jogos aleatorios para comparacao -----------------
    jogo_aleatorio = mega.criar_jogo()
    acertos_referencia[game_id] = Contar_Acertos(jogo_aleatorio,concurso)
# -------- remocao de linhas -----------------
    linhas_a_serem_removidas = random.sample([0,1,2,3,4,5],  N_remover)
    intervalo = np.arange(1,61,1)
    intervalo = intervalo.reshape((6,10))
    intervalo = np.delete(intervalo,linhas_a_serem_removidas,0)
    intervalo = intervalo.reshape((1,(6-N_remover)*10))
    N_aleatorios = np.array((random.sample(list(intervalo[0]),  6) ))


    acertos_estudado[game_id] = Contar_Acertos(N_aleatorios,concurso)
    progress(game_id,n_concursos+1) # Funcao para exibir o progresso da simulacao

# ------  o primeiro item de cada vetor devem ser removidos ---------
acertos_estudado = acertos_estudado[1:]
acertos_referencia = acertos_referencia[1:]
HistogramaComparacao(acertos_referencia, acertos_estudado,mega.nome_loteria,'M3_bolao_aleatorio.png')

print('\n')
print("Terminou")
