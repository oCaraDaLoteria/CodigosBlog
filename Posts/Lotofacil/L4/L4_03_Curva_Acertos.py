from funcoes_e_etc import *

# Crio objeto da Lotofacil
loteria = Loterias('lotofacil')
n_concursos = loteria.n_concursos
N_maximo = 15
n_fixos = np.arange(N_maximo)
acertos = np.zeros(N_maximo)
erros = np.zeros(N_maximo)
# Simulacao
for ind_ae in range(0,N_maximo):
    AcertosErros = np.zeros(n_concursos+1)
    for game_id in range(1,n_concursos+1):
    # ---------- pego o resultado do concurso --------------------
        concurso = loteria.concursos[game_id]

    # ---------- crio qtd_fixos de numeros e verifico se eu acertei eles  --------------------
        aleatorios_fixos = Dezenas_Aleatorias_Da_Loteria(n_fixos[ind_ae]+1, loteria.nome_loteria);

        AcertosErros[game_id] = Comparar_Vetores(aleatorios_fixos, concurso)


    progress(ind_ae,N_maximo-1) # Funcao para exibir o progresso da simulacao

    # Removo o primeiro valor, pois ela nao foi usada na Simulacao
    AcertosErros = AcertosErros[1:]

    acertos[ind_ae] = 100.0*sum(AcertosErros==1)/(len(AcertosErros)*1.0)
    erros[ind_ae] = 100.0*sum(AcertosErros==0)/(len(AcertosErros)*1.0)






# Plot dos resultados
fig, ax = plt.subplots(figsize=(10,5))
x = np.arange(N_maximo)+1
ax.set_axisbelow(True)
ax.grid(True, ls='-')
ax.plot(x,acertos,'-o',ms=10,lw=2, alpha=0.5, label="Acertos" )
for i,j in zip(x,acertos):
    ax.annotate('%.1f'%float(j),xy=(i,j))

ax.plot(x,erros,'-s',ms=10,lw=2, alpha=0.5, label="Erros")
for i,j in zip(x,erros):
    ax.annotate('%.1f'%float(j),xy=(i,j))

ax.set_xticks(x)
ax.set_xlabel('Qtd dezenas fixas')
ax.set_ylabel('Probabilidade (%)')
plt.legend()
plt.savefig("RESULTADOS/Curva_AcertoErros")
plt.show()

print('\n')
print("Terminou")
