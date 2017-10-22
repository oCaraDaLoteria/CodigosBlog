import numpy as np
import sys
import os.path
import pandas as pd
import matplotlib.pyplot as plt
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
    if loteria=='Quina':
        jogos_limpos = np.zeros((n_jogos+1,5))

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
    import os.path
    if loteria=='Megasena':
        if os.path.exists("megasena.db"):
            conn = sqlite3.connect('megasena.db')
        else:
            print("Erro Fatal: Nao foi possivel encontrar o arquivo `megasena.db`")
            sys.exit()
    if loteria=='Lotofacil':
        if os.path.exists("lotofacil.db"):
            conn = sqlite3.connect('lotofacil.db')
        else:
            print("Erro Fatal: Nao foi possivel encontrar o arquivo `lotofacil.db`")
            sys.exit()
    if loteria=='Quina':
        if os.path.exists("quina.db"):
            conn = sqlite3.connect('quina.db')
        else:
            print("Erro Fatal: Nao foi possivel encontrar o arquivo `quina.db`")
            sys.exit()


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
    if loteria=='Quina':
        qtd_numeros = 80
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
        if (nome == 'loto') or (nome == 'lotofacil') or (nome == 'Lotofacil') or (nome == 'facil') or (nome == 15):
            self.nome_loteria = 'Lotofacil'
        if (nome == 'mega') or (nome == 'Mega') or (nome == 'megasena') or (nome == 'Megasena') or (nome == 6):
            self.nome_loteria = 'Megasena'
        if (nome == 'quina') or (nome == 'Quina') or (nome == 5):
            self.nome_loteria = 'Quina'
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
        if self.nome_loteria=='Quina':
            intervalo = np.arange(1,81,1)
            qtd_numeros = 5
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
        if self.nome_loteria=='Quina':
            intervalo = np.arange(1,81,1)
            qtd_numeros = 5
        bolao =  np.zeros((qtd_jogos,qtd_numeros))
        for bb in range(0, qtd_jogos):
            bolao[bb,:] = self.criar_jogo()
        return bolao






class Fechamento:
    def __init__(self,nome_tabela_fechamento, *args):
        if os.path.exists(nome_tabela_fechamento) or os.path.exists("TABELAS/" + nome_tabela_fechamento) :
            try:
                self.tabela_fechamento = pd.read_csv(nome_tabela_fechamento,header=None);
            except:
                self.tabela_fechamento = pd.read_csv("TABELAS/" + nome_tabela_fechamento,header=None);

            # converte as tabelas do tipo dataframe para numpy e armazena algumas estatisticas
            self.tabela_fechamento = self.tabela_fechamento.as_matrix()
            self.n_cartelas,self.n_dezenas = self.tabela_fechamento.shape
            self.nome_arquivo = nome_tabela_fechamento

            if (self.n_dezenas == 15):
                self.nome_loteria = 'Lotofacil'
            elif (self.n_dezenas == 6):
                self.nome_loteria = 'Megasena'
            elif (self.n_dezenas == 5):
                self.nome_loteria = 'Quina'
            else:
                print("Erro Fatal: O numero de dezenas na tabela esta errada")
                print("Fim de programa")
                sys.exit()

            if len(args) == 0:
                print("Warning: Numeros utilizados no fechamento sao aleatorios")
                print("Isso pode gerar resultados nao esperados")
                self.qtd_numeros = np.max(self.tabela_fechamento) # adivinho a qtd de numeros necessario para fazer o fechamento
                self.numeros_fechamento = self.criar_jogo()
            else:
                try:
                    self.numeros_fechamento = pd.read_csv(args[0],header=None);
                    self.numeros_fechamento = self.numeros_fechamento.as_matrix()
                    self.numeros_fechamento = self.numeros_fechamento[0] # como "as_matrix()" retorna um array de array, eu fico apenas com o primeiro (e unico) item para facilitar a sintaxe do programa depois
                    self.qtd_numeros, = self.numeros_fechamento.shape
                except:
                    print("Erro Fatal: Numeros de fechamento nao encontrado")
                    print("Fim de programa")
                    sys.exit()
        else:
            print("Erro Fatal: Tabela de fechamento nao encontrado")
            print("Fim de programa")
            sys.exit()

        if self.qtd_numeros == np.max(self.tabela_fechamento):
            self.bolao = self.numeros_fechamento[self.tabela_fechamento-1]
        else:
            print("Erro Fatal: As tabelas nao estao compativeis")
            print("Fim de programa")
            sys.exit()

    def criar_jogo(self):
    # (Input) intervalo : vetor entre 1-X (x=60 : megasena, x=25 : lotofacil, etc)
    # (Input) qtd_numeros : numero que diz qual o tamanho da aposta (6 : megasena, 15 : lotofacil, etc)
    # (Output) item : um vetor com 'qtd_numeros' numeros diferentes dentro do intervalo especificado
        import random
        if self.nome_loteria=='Megasena':
            intervalo = np.arange(1,61,1)
            qtd_numeros = self.qtd_numeros
        if self.nome_loteria=='Lotofacil':
            intervalo = np.arange(1,26,1)
            qtd_numeros = self.qtd_numeros
        if self.nome_loteria=='Quina':
            intervalo = np.arange(1,81,1)
            qtd_numeros = self.qtd_numeros
        item = np.zeros(qtd_numeros)
        for qq in range(0,qtd_numeros):
            item[qq] = intervalo[random.randint(0,len(intervalo)-1)] # seleciono um numero do 'intervalo' disponivel
            intervalo = np.delete(intervalo,np.argwhere(intervalo==item[qq])) # removo o numero que foi sorteado do 'intervalo'
        return np.sort(item)

    def criar_bolao(self):
    # Essa funcao faz um novo bolao, usando a tabela de fechamento conhecida,
    # porem, os numeros do fechamento sao diferentes. Eles sao criados, e os
    # valores anteriores sao apagados (assim, possibilita debug do codigo)
        self.numeros_fechamento = self.criar_jogo()
        self.bolao = self.numeros_fechamento[self.tabela_fechamento-1]
        return self.bolao

    def update(self):
        try:
            self.bolao = self.numeros_fechamento[self.tabela_fechamento-1]
        except:
            print("Erro Fatal: Vc colocou uma qtd de numero incompativel com a tabela de fechamento")
            print("Fim de programa")
            sys.exit()
## ---------------- CRIACAO DE OBJETOS ----------------------------------
## ---------------- CRIACAO DE OBJETOS ----------------------------------






















## ------------------------ HISTOGRAMA ----------------------------------
## ------------------------ HISTOGRAMA ----------------------------------
def Histograma(conjunto_numeros,loteria,nome_figura='histograma.png',salvar='nao'):
# (Input): conjunto_numeros = matriz que desejo saber a frequencia de cada dezena
# (Input): loteria = precisos saber qual tipo de jogo (megasena : qtd_numeros = 6, etc.)
# (Output): hist_acertos, hist_normalizados = valores apresentados no histograma
    if loteria == 'Lotofacil':
        qtd_numeros = 25
    if loteria == 'Quina':
        qtd_numeros = 80
    if loteria == 'Megasena':
        qtd_numeros = 60
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.005*height, '%.1f'%float(height),
                    ha='center', va='bottom',zorder=500)
    bins = range(0,qtd_numeros+2)
    hist_numeros, bins = np.histogram(conjunto_numeros, bins=bins)
    width = np.diff(bins)
    center = (bins[:-1] + bins[1:]) / 2
    hist_normalizado = 100.*hist_numeros/(1.0*sum(hist_numeros))

    fig, ax = plt.subplots(figsize=(15.0,5.0))
    rectshd = ax.bar(center, hist_normalizado, align='center', width=width,edgecolor='k')

    autolabel(rectshd) # coloca valores sobre as barras
    ax.set_xticks(bins)

    ax.set_xlabel('Dezena')
    ax.set_ylabel('Probabilidade (%)')
    ax.set_ylim([0,100])
    ax.set_xlim([0.5,qtd_numeros+0.5])
    if salvar == 'sim':
        plt.savefig(nome_figura)
    # plt.show()
    return hist_numeros, hist_normalizado




def HistogramaComparacao(acertos_referencia, acertos_estudado,loteria,nome_figura='comparacao.png'):

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
    hist_normalizado_referencia = 100.*hist_acertos_referncia/(1.0*sum(hist_acertos_referncia))
    if sys.version_info.major > 2:
        hist_normalizado_referencia = list(hist_normalizado_referencia)
    rectshd1 = ax.bar(center, hist_normalizado_referencia, align='center', width=width, label='Aleatorio',color='none',edgecolor='r',linewidth=2.0,linestyle='dotted')

    hist_acertos_estudado, bins = np.histogram(acertos_estudado, bins=bins)
    hist_normalizado_estudado = 100.*hist_acertos_estudado/(1.0*sum(hist_acertos_estudado))
    if sys.version_info.major > 2:
        hist_normalizado_estudado = list(hist_normalizado_estudado)
    rectshd2 = ax.bar(center, hist_normalizado_estudado, align='center', width=width, label='Teste',alpha = 0.7,edgecolor='k')
    autolabel(rectshd2)
    ax.legend()
    if sys.version_info.major > 2:
        # concerta problema com a posicao dos numeros
        ax.set_xticks(center) # defino a posicao deles
        center = center - 0.5 # converto eles para o valor correto a ser exibido
        ax.set_xticklabels(center.astype(int)) # mostra os valores em forma int() para ficar mais agradavel a leitura
        ax.set_xlim([-0.25,qtd_numeros+1.25])
    else:
        ax.set_xticks(center) # defino a posicao deles
    ax.set_xlabel('Num. de Acertos')
    ax.set_ylabel('Probabilidade (%)')
    ax.set_ylim([0,100])

    plt.title(nome_figura)
    plt.savefig("RESULTADOS/"+nome_figura)
    plt.show()




def HistogramaAcertosErros(AcertosErros,nome_figura='AcertosErros.png'):
    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.005*height, '%.1f'%float(height),
                    ha='center', va='bottom')

    qtd_acertos = 100.0*sum(AcertosErros==1)/(len(AcertosErros)*1.0)
    qtd_erros = 100.0*sum(AcertosErros==0)/(len(AcertosErros)*1.0)
    estatistica  = (qtd_erros, qtd_acertos)

    fig, ax = plt.subplots(figsize=(5,5))

    ind = np.arange(2)
    width = 0.35
    ax.set_axisbelow(True)
    ax.grid(True, ls='--')
    rects = ax.bar(ind, estatistica, width)
    autolabel(rects)
    plt.xticks(ind, ('Erros', 'Acertos'))
    ax.set_ylim([0,100])
    plt.savefig("RESULTADOS/"+nome_figura)
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




def Comparar_Vetores(item, concurso):
    # (Input) item : vetor com qtd de dezenas menores que o concurso
    # (Input) concurso : resultado de um concurso de qualquer loteria
    n = len(item)
    acertos  = np.zeros(n);
    for nn in range(0,n):
        if item[nn] in concurso:
            acertos[nn] = 1

    if sum(acertos)==len(concurso) or sum(acertos)==n:
        return 1
    else:
        return 0
## ------------------------ CONTAR ACERTOS ----------------------------------
## ------------------------ CONTAR ACERTOS ----------------------------------


















## ------------------------  PERSONALIZADO --------------------------------
## ------------------------  PERSONALIZADO --------------------------------
def limpeza(vetor, itens_deletar):
# (Input) vetor: um numpy array no qual deseja-se eliminar certos numeros
# (Input) itens_deletar: numeros contidos em `vetor` que desejam ser eliminados.
#       Note que deve-ser inseridos os numeros que estao presentes em `vetor`, e NAO seus indices em `vetor`
# (Output) vetor: sequencia com itens removidos
    tam_vet = len(vetor)
    tam_del = len(itens_deletar)
    if tam_del > tam_vet:
        print('Vc quer deletar mais coisas q o possivel')
        return 0

    for ii in range(0,tam_del):
        vetor = np.delete(vetor,np.argwhere(vetor==itens_deletar[ii]))
    return vetor

def Dezenas_Aleatorias_Da_Loteria(qtd_retonar, loteria):
# (Input) qtd_numeros : qtd de numeros a ser retornado
# (Input) loteria : {'Megasena','Lotofacil','Quina'}
# (Output) : retorna "qtd_numeros" numeros diferntes no intervalo disponivel da
# respectiva loteria

# Essa funcao retorna  um numero maior de dezenas de uma loteria, por exemplo:
# -> AleatorioDaLoteria(9, 'Megasena')
# -> Retorna "9" numeros diferntes entre 1-60 (intervalo de dezenas da megasena)

    import random
    if loteria == 'Lotofacil':
        intervalo = np.arange(1,26,1)
        qtd_numeros = 25
    if loteria == 'Quina':
        intervalo = np.arange(1,81,1)
        qtd_numeros = 80
    if loteria == 'Megasena':
        intervalo = np.arange(1,61,1)
        qtd_numeros = 60
    if qtd_retonar > qtd_numeros:
        print('[Dezenas_Aleatorias_Da_Loteria] Vc deseja mais numeros que o possivel')
        print("Fim de programa")
        sys.exit()
    if qtd_retonar < 1:
        print('[Dezenas_Aleatorias_Da_Loteria] Numero a ser retornado esta negativo ou nulo')
        print("Fim de programa")
        sys.exit()
    item = np.zeros(qtd_retonar)

    for qq in range(0,qtd_retonar):
        item[qq] = intervalo[random.randint(0,len(intervalo)-1)] # seleciono um numero do 'intervalo' disponivel
        intervalo = np.delete(intervalo,np.argwhere(intervalo==item[qq])) # removo o numero que foi sorteado do 'intervalo'
    return item


def progress(count, total, suffix=''):
# FUNCAO APENAS PARA VIZUALIZAR O PROGRESSO DA SIMULACAO
# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben
## ------------------------  PERSONALIZADO --------------------------------
## ------------------------  PERSONALIZADO --------------------------------
