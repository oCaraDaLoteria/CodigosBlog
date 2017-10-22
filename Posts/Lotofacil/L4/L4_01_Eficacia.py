from funcoes_e_etc import *

FCMT = Fechamento("19_15_13(5)=10.csv")

# --- Crio objeto da Lotofacil
loteria = Loterias('lotofacil')
n_concursos = loteria.n_concursos
acertos_referencia = np.zeros(n_concursos+1)
acertos_estudado = np.zeros( (n_concursos+1,FCMT.n_cartelas) )

# --- Simulacao
for game_id in range(1,n_concursos+1):
# ---------- pego o resultado do concurso --------------------
    concurso = loteria.concursos[game_id]
# ---------- curva de referencia  --------------------
    acertos_referencia[game_id] = Contar_Acertos(loteria.criar_jogo(), concurso)

# ---------- crio 19 numeros como fechamentos  --------------------
    FCMT.numeros_fechamento = Dezenas_Aleatorias_Da_Loteria(19, 'Lotofacil')
    FCMT.update()
    bolao_estudado = FCMT.bolao
    acertos_estudado[game_id,:] = Contar_Acertos(bolao_estudado, concurso)
    progress(game_id,n_concursos+1) # Funcao para exibir o progresso da simulacao


# ------  o primeiro item de cada vetor devem ser removidos ---------
acertos_referencia = acertos_referencia[1:]
acertos_estudado = acertos_estudado[1:]

# Comparo os resultados
HistogramaComparacao(acertos_referencia, acertos_estudado,loteria.nome_loteria,"L4 - 19 dezenas")

print('\n')
print("Terminou")
