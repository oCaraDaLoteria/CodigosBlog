from funcoes_e_etc import *

# --- Crio objeto da Lotofacil
loteria = Loterias('Megasena')
n_concursos = loteria.n_concursos
total_linhas = np.zeros((n_concursos+1,6))

# --- Simulacao
for game_id in range(1,n_concursos+1):
# ---------- pego o resultado do concurso --------------------
    concurso = loteria.concursos[game_id]

    T2  = (concurso[(concurso%10)!=0]/10).astype(int) # verifico em qual linha um numero pertence
    T3 = (concurso[(concurso%10)==0]/10).astype(int) - 1 # dezenas {10,20,...,60} devem ser tratados separadamente
    total_linhas[game_id,:] = np.concatenate((T2,T3)) # nao importa a ordem nesse nesse estudo

    progress(game_id,n_concursos+1) # Funcao para exibir o progresso da simulacao


# ------  o primeiro item de cada vetor devem ser removidos ---------
total_linhas = total_linhas[1:]

# Plot do Histograma
M3_Histograma_Linhas(total_linhas.reshape((n_concursos*6,1)), 'M3_prob_linha.png')

print('\n')
print("Terminou")
