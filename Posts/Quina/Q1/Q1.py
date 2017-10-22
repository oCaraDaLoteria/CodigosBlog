from funcoes_e_etc import *
from os import listdir
from os.path import isfile, join

# Em linux a barra esta  "certa", no Windows eh barra "invertida"
# Preciso identificar o sistema operacional para poder corrigir o endereco da
# pasta onde estao as tabelas de fechamento
if os.name == 'posix': 
    mypath = os.getcwd()+"/TABELAS"
else:
    mypath = os.getcwd()+"\TABELAS"
tabelas = [f for f in listdir(mypath) if isfile(join(mypath, f))]



for indice,arquivo in enumerate(tabelas):
    FCMT = Fechamento(arquivo) # funciona, mas sempre que puder, use numeros de fechamento conhecidos
    n_cartelas = FCMT.n_cartelas
    bolao_estudado = FCMT.bolao

    # -------------------------------- DEMOS --------------------------------
    # # Para demonstracao do metodo criar_bolao()
    # print(FCMT.numeros_fechamento)
    # FCMT.criar_bolao()
    # print(FCMT.numeros_fechamento)
    # -------------------------------- DEMOS --------------------------------

    # Crio objeto da loteria correspondente
    loteria = Loterias(FCMT.nome_loteria)
    n_concursos = loteria.n_concursos

    # Crio variaveis que contabilizam os acertos
    acertos_referencia = np.zeros((n_concursos+1,n_cartelas))
    acertos_estudado = np.zeros((n_concursos+1,n_cartelas))


    # Simulacao
    print('\n>> Arquivo: '+ arquivo + ' ['+ str(indice+1) + '/'+ str(len(tabelas)) + ']' )
    for game_id in range(1,n_concursos+1):
    # ---------- pego o resultado do concurso --------------------
        concurso = loteria.concursos[game_id]

    # -------- crio jogos aleatorios para comparacao -----------------
        bolao_referencia = loteria.criar_bolao_aleatorio(n_cartelas)
        acertos_referencia[game_id,:] = Contar_Acertos(bolao_referencia, concurso)

    # -------- aplico o mesmo bolao para todos os concursos -----------------
        # acertos_estudado[game_id,:] = Contar_Acertos(bolao_estudado,concurso)

    # -------------------------------- DEMOS --------------------------------
    # -------- NAO aplico o mesmo bolao para todos os concursos -----------------
        bolao_estudado = FCMT.criar_bolao()
        novos_numeros_fechamento = FCMT.numeros_fechamento
        # print(novos_numeros_fechamento)
        acertos_estudado[game_id,:] = Contar_Acertos(bolao_estudado,concurso)

        # # O usuario pode inserir os novos dados
        # FCMT.numeros_fechamento = np.array((15, 17., 20., 42., 47., 55., 58., 59.))
        # FCMT.update()
        # bolao_estudado = FCMT.bolao
        # acertos_estudado[game_id,:] = Contar_Acertos(bolao_estudado,concurso)
    # -------------------------------- DEMOS --------------------------------
        progress(game_id,n_concursos+1) # Funcao para exibir o progresso da simulacao
    # Removo a primeira linha, pois ela nao foi usada na Simulacao
    acertos_referencia = acertos_referencia[1:]
    acertos_estudado = acertos_estudado[1:]
    # Comparo os resultados
    HistogramaComparacao(acertos_referencia, acertos_estudado,loteria.nome_loteria,arquivo[:-4])


print('\n')
print("Terminou")
