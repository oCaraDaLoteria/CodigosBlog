from funcoes_e_etc import *


N_jogos_anteriores = 10 # ----- EDITE AQUI -----
N_remover = 3 # ----- EDITE AQUI -----


mega = Loterias('Megasena')
n_concursos = mega.n_concursos + 1

# Fechamentos-Exclusivo-Aposta-Esperta-Mega-Sena-09-06-05
FCMT = Fechamento("tabela_fechamento.csv") # funciona, mas nao eh recomendado
n_cartelas = FCMT.n_cartelas


acertos_referencia = np.zeros((n_concursos,n_cartelas))
acertos_estudado = np.zeros((n_concursos,n_cartelas))

for game_id in range(N_jogos_anteriores+1, n_concursos):
# ---------- pego um resultado anterior --------------------
    concurso = mega.concursos[game_id]

# -------- crio jogos aleatorios para comparacao -----------------
    bolao_aleatorio = mega.criar_bolao_aleatorio(n_cartelas)
    acertos_referencia[game_id] = Contar_Acertos(bolao_aleatorio, concurso)

# -------- remocao de linhas -----------------
    # armazeno os concurso anteriores
    inicio = game_id - N_jogos_anteriores
    fim = game_id
    concursos_anteriores = mega.concursos[inicio:fim]

    # pego o numero da linha de cada dezena e descubro quais as linhas foram
    # menos sorteadas
    n_linhas = numero_da_linha_da_dezena(concursos_anteriores)
    frequecia_linhas, bins_dummy = np.histogram(n_linhas, bins=range(0,7))
    frequencia_em_ordem_crescente = np.argsort(frequecia_linhas)
    linhas_a_serem_removidas = frequencia_em_ordem_crescente[0:N_remover]

    # crio o "volante efetivo" de onde serao sorteados as dezenas
    intervalo = np.arange(1,61,1)
    intervalo = intervalo.reshape((6,10))
    intervalo = np.delete(intervalo, linhas_a_serem_removidas,0)
    intervalo = intervalo.reshape((1,(6-N_remover)*10))

    ## Posso escolher apenas um volante com 6 numeros, mais isso nao tem
    ## resultados. Caso queira testar, basta usar a linha abaixo
    # N_aleatorios = np.array((random.sample(list(intervalo[0]),  6) ))
    # acertos_estudado[game_id] = Contar_Acertos(N_aleatorios,concurso)

    ## Farei um bolao usando uma tabela de fechamento
    bolao_estudado = FCMT.criar_bolao()
    acertos_estudado[game_id,:] = Contar_Acertos(bolao_estudado,concurso)

    progress(game_id,n_concursos+1) # Funcao para exibir o progresso da simulacao

# ------  o primeiro item de cada vetor devem ser removidos ---------
acertos_estudado = acertos_estudado[1:]
acertos_referencia = acertos_referencia[1:]
HistogramaComparacao(acertos_referencia, acertos_estudado,mega.nome_loteria,'M3_fechamento.png')

print('\n')
print("Terminou")
