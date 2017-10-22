import sqlite3
import numpy as np

## ------------- MEGASENA -------------
my_data = np.genfromtxt('D_MEGA.csv', delimiter=',')

conn = sqlite3.connect('megasena.db')
cur = conn.cursor()
sql = ''' INSERT INTO concursos(concurso_id,n1,n2,n3,n4,n5,n6)
              VALUES(?,?,?,?,?,?,?) '''

cur.execute("""
SELECT count(*) FROM concursos;
""")
qtd_registrado = cur.fetchall()
qtd_registrado = qtd_registrado[0]
qtd_registrado = qtd_registrado[0]
print('Megasena (old):',qtd_registrado)
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
print('Megasena (new):',qtd_registrado)

conn.commit()


