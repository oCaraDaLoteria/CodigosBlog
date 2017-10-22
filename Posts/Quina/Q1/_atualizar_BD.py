import sqlite3
import numpy as np

## ------------- QUINA -------------
my_data = np.genfromtxt('D_QUINA.csv', delimiter=',')

conn = sqlite3.connect('quina.db')
cur = conn.cursor()
sql = ''' INSERT INTO concursos(concurso_id,n1,n2,n3,n4,n5)
              VALUES(?,?,?,?,?,?) '''

cur.execute("""
SELECT count(*) FROM concursos;
""")
qtd_registrado = cur.fetchall()
qtd_registrado = qtd_registrado[0]
qtd_registrado = qtd_registrado[0]
print('Quina (old):',qtd_registrado)
for n in range(qtd_registrado,len(my_data)+1):
    try:
        numeros = np.concatenate((np.array((1.0*n+1,)),my_data[n]))
        cur.execute(sql, numeros)
    except:
        pass

cur.execute("""
SELECT count(*) FROM concursos;
""")
qtd_registrado = cur.fetchall()
qtd_registrado = qtd_registrado[0]
qtd_registrado = qtd_registrado[0]
print('Quina (new):',qtd_registrado)
conn.commit()
