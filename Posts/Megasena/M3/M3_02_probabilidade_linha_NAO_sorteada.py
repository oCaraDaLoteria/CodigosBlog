from funcoes_e_etc import *

# --- Crio objeto da Lotofacil
loteria = Loterias('Megasena')
n_concursos = loteria.n_concursos
linha_nao_sorteada = np.array(())

# --- Simulacao
for game_id in range(1,n_concursos+1):
# ---------- pego o resultado do concurso --------------------
    concurso = loteria.concursos[game_id]

    T2  = (concurso[(concurso%10)!=0]/10).astype(int) # verifico em qual linha um numero pertence
    T3 = (concurso[(concurso%10)==0]/10).astype(int) - 1 # dezenas {10,20,...,60} devem ser tratados separadamente
    total_linhas = np.concatenate((T2,T3)) # nao importa a ordem nesse nesse estudo

    # a seguir irei contar ('len()') quantas linhas NAO foram sorteadas
    linha_nao_sorteada = np.concatenate( (linha_nao_sorteada,  [len(np.setdiff1d([0, 1, 2, 3, 4, 5], total_linhas))]  ))

    progress(game_id,n_concursos+1) # Funcao para exibir o progresso da simulacao


M3_Histograma_Linhas(linha_nao_sorteada, 'M3_linha_nao_sorteada.png')
print('\n')
print("Terminou")
