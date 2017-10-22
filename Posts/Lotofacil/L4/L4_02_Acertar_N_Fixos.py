from funcoes_e_etc import *

# Crio objeto da Lotofacil
loteria = Loterias('lotofacil')
n_concursos = loteria.n_concursos

AcertosErros = np.zeros((n_concursos+1,1))
n_fixos = 5

# Simulacao
for game_id in range(1,n_concursos+1):
# ---------- pego o resultado do concurso --------------------
    concurso = loteria.concursos[game_id]

# ---------- crio qtd_fixos de numeros e verifico se eu acertei eles  --------------------
    aleatorios_fixos = Dezenas_Aleatorias_Da_Loteria(n_fixos, loteria.nome_loteria);
    AcertosErros[game_id] = Comparar_Vetores(aleatorios_fixos, concurso)

# ---------- Para verificacao visual do programa  se necessario --------------------
    # print(aleatorios_fixos)
    # print(np.sort(concurso))
    # print(AcertosErros[game_id])
    # print("****************")

    progress(game_id,n_concursos+1) # Funcao para exibir o progresso da simulacao


# Removo o primeiro valor, pois ela nao foi usada na Simulacao
AcertosErros = AcertosErros[1:]

# Comparo os resultados
HistogramaAcertosErros(AcertosErros)

print('\n')
print("Terminou")
