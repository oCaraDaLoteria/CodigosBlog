import numpy as np

## ---------------- CRIACAO DE OBJETOS ----------------------------------
## ---------------- CRIACAO DE OBJETOS ----------------------------------
def transfomar_em_matriz(todos_jogos,loteria):
    # (Input) todos_jogos: todos os concursos dentro do banco de dados
    # (Input) loteria: o tipo da loteria {'Megasena','Lotofacil'}
    # (Output) jogos_limpos: uma matriz contendo os resultados
        # A matriz 'jogos_limpos' visa facilitar a experiencia do programador.
        # Cada resultado em 'todos_jogos' possui uma coluna adicional que advem
        # da chave primaria do banco de dados, e ela eh removida.

        # Outro aspecto a ser mencionado, eh que a linha indice '0 (zero)'
        # nao sera utilizada, assim evita confusao de indices que eh gerado pelo
        # pois o concurso 'x' na vida real corresponde ao indice 'x-1' num array
        # do python. Com a primeira linha sendo descartada, essa discrepancia eh
        # eliminada

        # Portanto : o concurso numero 1 da vida real esta na linha numero 1 da
        # matriz 'jogos_limpos'

        # Para avisar ao programador que algo esta errado, um valor (debug)
        # absurdo para o contexto de loteria eh adicionado na linha 'zero'
    n_jogos = len(todos_jogos)
    if loteria=='Megasena':
        # preciso saber qual o tipo de loteria para poder criar a matriz Output
        # com as dimensoes corretas
        jogos_limpos = np.zeros((n_jogos+1,6))
    if loteria=='Lotofacil':
        jogos_limpos = np.zeros((n_jogos+1,15))

    jogos_limpos[0,:] = -5000 # valor de debug
    for idx in range(1,n_jogos+1):
        jogo = todos_jogos[idx-1]
        jogos_limpos[idx,:] = jogo[1:] # remove o indice 'concurso_id' do jogo
    return jogos_limpos

def obter_resultados_concursos_BD(loteria):
    # (Input) loteria: o tipo da loteria {'Megasena','Lotofacil'}
    # (Output) jogos_limpos: uma matriz contendo os concursos presentes do BD
        # Output da funcao 'transfomar_em_matriz()'
    # #---------- conexao com banco de dados ---------------------
    import sqlite3
    if loteria=='Megasena':
        conn = sqlite3.connect('megasena.db')
    if loteria=='Lotofacil':
        conn = sqlite3.connect('lotofacil.db')
    cur = conn.cursor()
    # #---------- pego todos os dados no BD ---------------------
    cur.execute("""
    SELECT * FROM concursos;
    """)
    todos_jogos = cur.fetchall()
    cur.close()
    return transfomar_em_matriz(todos_jogos,loteria)

def obter_sorteados(resultados,loteria):
    # (Input) resultados: conjunto de jogos que desejo saber a frequencia que
        # cada numero ocorreu
    # (Input) loteria: o tipo da loteria {'Megasena','Lotofacil'}
    # (Output) em_ordem: um vetor que possui o numeros em ordem crescente de
        # ocorrencia, isto eh, o primeiro numero foi o que menos foi sorteado, e
        # o ultimo numero foi o mais sorteado
    if loteria=='Megasena':
        qtd_numeros = 60
    if loteria=='Lotofacil':
        qtd_numeros = 25
    bins = range(0,qtd_numeros+2)
    hist_numeros, bins = np.histogram(resultados, bins=bins) # a contagem de frequencia eh obtida fazendo um histograma
    em_ordem = sorted(range(len(hist_numeros)), key=lambda k: hist_numeros[k]) #ordem crescente de todos oos numeros que ja sorteados
    return em_ordem[1:] # o primeiro item eh o valor zero,e deve ser removido



class Loterias:
    # Cria um bjeto que contem todas os concursos ja realizados para determinada
    # loteria. E exibe estatisti basicas
    # Os possiveis nomes atualmente disponiveis sao
    # -> 'Megasena'
    # -> 'Lotofacil'
    #
    def __init__(self,nome):
        if (nome == 'loto') or (nome == 'lotofacil') or (nome == 'Lotofacil') or (nome == 'facil'):
            self.nome_loteria = 'Lotofacil'
        if (nome == 'mega') or (nome == 'Mega') or (nome == 'megasena') or (nome == 'Megasena'):
            self.nome_loteria = 'Megasena'
        # self.nome_loteria = nome
        self.concursos = obter_resultados_concursos_BD(self.nome_loteria)
        self.n_concursos = len(self.concursos)-1 # o "-1" advem do fato que a matriz de concursos possui uma linha adicional, de indice zero, que nao eh utilizada
        self.estatisticas_sorteados = obter_sorteados(self.concursos,self.nome_loteria)

    def info(self):
        print('Loteria:',self.nome_loteria)
        print('Num. Concursos Cadastrados:',self.n_concursos)
        print('Menos Sorteado --> Mais Sorteado',self.estatisticas_sorteados)

    def criar_jogo(self):
    # (Input) intervalo : vetor entre 1-X (x=60 : megasena, x=25 : lotofacil, etc)
    # (Input) qtd_numeros : numero que diz qual o tamanho da aposta (6 : megasena, 15 : lotofacil, etc)
    # (Output) item : um vetor com 'qtd_numeros' numeros diferentes dentro do intervalo especificado
        import random
        if self.nome_loteria=='Megasena':
            intervalo = np.arange(1,61,1)
            qtd_numeros = 6
        if self.nome_loteria=='Lotofacil':
            intervalo = np.arange(1,26,1)
            qtd_numeros = 15
        item = np.zeros(qtd_numeros)
        for qq in range(0,qtd_numeros):
            item[qq] = intervalo[random.randint(0,len(intervalo)-1)] # seleciono um numero do 'intervalo' disponivel
            intervalo = np.delete(intervalo,np.argwhere(intervalo==item[qq])) # removo o numero que foi sorteado do 'intervalo'
        return np.sort(item)

    def criar_bolao_aleatorio(self, qtd_jogos):
    # (Input) intervalo : vetor entre 1-X (x=60 : megasena, x=25 : lotofacil, etc)
    # (Input) qtd_numeros : numero que diz qual o tamanho da aposta (6 : megasena, 15 : lotofacil, etc)
    # (Input) qtd_jogos : tamanho do bolao, ('qtd_jogos=10' significa que havera 10 jogos diferentes)
    # (Output) bolao : retorna uma matriz (convencional) ou list (usando processamento paralelo)
        import random
        if self.nome_loteria=='Megasena':
            intervalo = np.arange(1,61,1)
            qtd_numeros = 6
        if self.nome_loteria=='Lotofacil':
            intervalo = np.arange(1,26,1)
            qtd_numeros = 15

        bolao =  np.zeros((qtd_jogos,qtd_numeros))
        for bb in range(0, qtd_jogos):
            bolao[bb,:] = self.criar_jogo()
        return bolao
## ---------------- CRIACAO DE OBJETOS ----------------------------------
## ---------------- CRIACAO DE OBJETOS ----------------------------------






















## ------------------------ HISTOGRAMA ----------------------------------
## ------------------------ HISTOGRAMA ----------------------------------
#--> THERE IS A KNOW ISSUE WITH PYTHON3 AND ALIGN=CENTER IN XLABEL <--
#--> USE PYTHON2 <--
def HistogramaPizza(conjunto_numeros,loteria,nome_figura='histograma.png',salvar='nao'):
# (Input): conjunto_numeros = matriz que desejo saber a frequencia de cada dezena
# (Input): loteria = precisos saber qual tipo de jogo (megasena : qtd_numeros = 6, etc.)
# (Output): hist_acertos, hist_normalizados = valores apresentados no histograma
    import matplotlib.pyplot as plt
    import seaborn as sns
    from cycler import cycler

    if loteria == 'Lotofacil':
        qtd_numeros = 25
    if loteria == 'Quina':
        qtd_numeros = 80
    if loteria == 'Megasena':
        qtd_numeros = 60
    bins = range(0,qtd_numeros+2)
    hist_numeros, bins = np.histogram(conjunto_numeros, bins=bins)
    width = np.diff(bins)
    center = (bins[:-1] + bins[1:]) / 2
    hist_normalizado = 100.*hist_numeros/(1.0*sum(hist_numeros))

    fig, ax = plt.subplots(figsize=(10.0,10.0))
    labels = np.arange(1,qtd_numeros+1)
    explode = np.zeros(qtd_numeros+1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    colors = [plt.cm.spectral(i) for i in np.linspace(0, 1, qtd_numeros+1)]
    ax.set_prop_cycle(color=sns.color_palette("coolwarm_r",qtd_numeros+1))
    #ax.set_prop_cycle(color=colors)
    ax.pie(hist_normalizado[1:], labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    if salvar == 'sim':
        plt.savefig(nome_figura)
    plt.show()

    return hist_numeros, hist_normalizado




def HistogramaComparacao(acertos_referencia, acertos_estudado,loteria,nome_figura='comparacao.png'):
    import matplotlib.pyplot as plt
    import sys

    if loteria == 'Lotofacil':
        qtd_numeros = 15
    if loteria == 'Quina':
        qtd_numeros = 5
    if loteria == 'Megasena':
        qtd_numeros = 6
    fig, ax = plt.subplots(figsize=(8,5))
    # manter essa definicao aqui dentro para funcionar adequadamente
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.005*height, '%.1f'%float(height),
                    ha='center', va='bottom',zorder=500)

    bins = range(0,qtd_numeros+2)
    hist_acertos_referncia, bins = np.histogram(acertos_referencia, bins=bins)
    width = np.diff(bins)
    center = (bins[:-1] + bins[1:]) / 2
    hist_normalizado_referencia = map(lambda x: (100.0)*x/(len(acertos_referencia)*1.0), hist_acertos_referncia)
    if sys.version_info.major > 2:
        hist_normalizado_referencia = list(hist_normalizado_referencia)
    rectshd1 = ax.bar(center, hist_normalizado_referencia, align='center', width=width, label='Aleatorio',color='none',edgecolor='r',linewidth=2.0,linestyle='dotted')

    hist_acertos_estudado, bins = np.histogram(acertos_estudado, bins=bins)
    hist_normalizado_estudado = map(lambda x: (100.0)*x/(len(acertos_estudado)*1.0), hist_acertos_estudado)
    if sys.version_info.major > 2:
        hist_normalizado_estudado = list(hist_normalizado_estudado)
    rectshd2 = ax.bar(center, hist_normalizado_estudado, align='center', width=width, label='Teste',alpha = 0.5,edgecolor='k')
    autolabel(rectshd2)
    ax.legend()
    ax.set_xlabel('Num. de Acertos')
    ax.set_ylabel('Probabilidade (%)')
    ax.set_ylim([0,100])
    ax.set_xlim([-0.5,qtd_numeros+0.5])
    plt.savefig(nome_figura)
    plt.show()

## ------------------------ HISTOGRAMA ----------------------------------
## ------------------------ HISTOGRAMA ----------------------------------


















## ------------------------ CONTAR ACERTOS ----------------------------------
## ------------------------ CONTAR ACERTOS ----------------------------------
def Contar_Acertos(bolao, resposta):
    # (Input): bolao = matriz no qual cada linha eh um jogo
    # (Input): resposta = sequencia de numeros que aconteceu na vida real
    # (Output) : acertos = vetor que diz a quantidade de acertos de cada "linha"
        # em comparacao com a 'resposta'
    # Eh formado um novo vetor que possui todos os valores de cada linha e a
    # resposta. Em seguida, esse vetor eh ordenado. Isso faz com que numeros
    # iguais fiquem juntos.
    # Ao aplicar o comando 'diff()' os numeros iguai irao gerar Zeros no vetor
    # final (ex: diff(1,2,2,4,6) = (1,0,2,2))
    # Contando a qunatidade de zeros  indica a quantidade de acertos

    if resposta.size != len(resposta): # if para concertar provavel problema
        resposta  = resposta[0]

    acertos = np.zeros(len(bolao))
    if bolao.size == resposta.size: # caso o usuario coloque apenas 1 jogo como bolao
        if bolao.size != len(bolao): # if para concertar provavel problema
            bolao  = bolao[0]
        acertos=(np.diff(np.sort(np.concatenate((bolao,resposta))))==0).sum()
    else:
        for n in range(0,len(bolao)):
            acertos[n]=(np.diff(np.sort(np.concatenate((bolao[n,:],resposta))))==0).sum()
    return acertos
## ------------------------ CONTAR ACERTOS ----------------------------------
## ------------------------ CONTAR ACERTOS ----------------------------------


















## ------------------------  PERSONALIZADO --------------------------------
## ------------------------  PERSONALIZADO --------------------------------
def sete_dezenas_pares():
    # O nome da funcao eh sugestivo, ela retorna 7 numeros pares diferentes e
        # aleatorios
    import random
    jogo = [1] # serve apenas como temporario para poder concatenar numeros no vetor
    disponivel = np.arange(2,26,2)
    for qq in range(0,7):
        escolhido = disponivel[random.randint(0,len(disponivel)-1)]
        jogo.append(escolhido)
        disponivel = np.delete(disponivel,np.argwhere(disponivel==escolhido))
    jogo =  np.array(jogo)
    jogo = jogo[1:]
    return jogo
## ------------------------  PERSONALIZADO --------------------------------
## ------------------------  PERSONALIZADO --------------------------------
