from funcoes_e_etc import *

## --------------------- LEIA-ME ----------------------------------
## --------------------- LEIA-ME ----------------------------------
# O programa busca por 2 arquivos do tipo ".csv"

# O primeiro arquivo deve conter a tabela de fechamento.
# -> Cada linha deve ser uma cartela de bolao
# --> Baseado na quantidade de colunas dessa tabela sera indentifcado o tipo de
# loteria que esta sendo trabalhada. Por exemplo, para a aposta minima da Mega
# sao 6 dezenas, portanto DEVEM existir 6 colunas (nada a mais, nada a menos).

# O segundo arquivo contem os numeros fixos no qual o fechamento sera aplicado.
# -> Deve conter UMA (1) linha com a quantidade de colunas igual a quantidade de
# dezenas para o fechamento
# -> Por padrao: Os valores dentro do arquivo 'numeros_fechamento.csv' serao
# aplicados em TODOS os concursos ja realizados. Vide DEMOS para alterar essa
# implementacao

## --------------------- LEIA-ME ----------------------------------
## --------------------- LEIA-ME ----------------------------------

# Crio objetos contendo o bolao de fechamento
# FCMT = Fechamento("tabela_fechamento.csv","numeros_fechamento.csv")
FCMT = Fechamento("tabela_fechamento.csv") # funciona, mas nao eh recomendado
n_cartelas = FCMT.n_cartelas
bolao_estudado = FCMT.bolao


# -------------------------------- DEMOS --------------------------------
# # Para demonstracao do metodo criar_bolao()
# print(FCMT.numeros_fechamento)
# FCMT.criar_bolao()
# print(FCMT.numeros_fechamento)
# -------------------------------- DEMOS --------------------------------

# Crio objeto da loteria correspondente
lotoria = Loterias(FCMT.nome_loteria)
n_concursos = lotoria.n_concursos

# Crio variaveis que contabilizam os acertos
acertos_referencia = np.zeros((n_concursos+1,n_cartelas))
acertos_estudado = np.zeros((n_concursos+1,n_cartelas))


# Simulacao
for game_id in range(1,n_concursos+1):
# ---------- pego o resultado do concurso --------------------
    concurso = lotoria.concursos[game_id]

# -------- crio jogos aleatorios para comparacao -----------------
    bolao_referencia = lotoria.criar_bolao_aleatorio(n_cartelas)
    acertos_referencia[game_id,:] = Contar_Acertos(bolao_referencia, concurso)

# -------- aplico o mesmo bolao para todos os concursos -----------------
    acertos_estudado[game_id,:] = Contar_Acertos(bolao_estudado,concurso)

# -------------------------------- DEMOS --------------------------------
# -------- NAO aplico o mesmo bolao para todos os concursos -----------------
    # bolao_estudado = FCMT.criar_bolao()
    # novos_numeros_fechamento = FCMT.numeros_fechamento
    # # print(novos_numeros_fechamento)
    # acertos_estudado[game_id,:] = Contar_Acertos(bolao_estudado,concurso)

    # # O usuario pode inserir os novos dados
    # FCMT.numeros_fechamento = np.array((15, 17., 20., 42., 47., 55., 58., 59.))
    # FCMT.update()
    # bolao_estudado = FCMT.bolao
    # acertos_estudado[game_id,:] = Contar_Acertos(bolao_estudado,concurso)
# -------------------------------- DEMOS --------------------------------
    print('%.2f' %  (100.*(game_id)/(n_concursos)) )



# Removo a primeira linha, pois ela nao foi usada na Simulacao
acertos_referencia = acertos_referencia[1:]
acertos_estudado = acertos_estudado[1:]

# Comparo os resultados
HistogramaComparacao(acertos_referencia, acertos_estudado,lotoria.nome_loteria)
