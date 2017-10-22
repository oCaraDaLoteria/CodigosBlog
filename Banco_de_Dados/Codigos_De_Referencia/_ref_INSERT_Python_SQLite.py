# ref: https://docs.python.org/2/library/sqlite3.html

import sqlite3
conn = sqlite3.connect('lotofacil.db')
cur = conn.cursor()
sql = ''' INSERT INTO concursos(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
numeros = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16);
cur.execute(sql, numeros)
conn.commit()
conn.close()


conn = sqlite3.connect('megasena.db')
cur = conn.cursor()
sql = ''' INSERT INTO concursos(n1,n2,n3,n4,n5,n6)
              VALUES(?,?,?,?,?,?) '''
numeros = (2,3,4,5,6,7);
cur.execute(sql, numeros)
conn.commit()
conn.close()


conn = sqlite3.connect('quina.db')
cur = conn.cursor()
sql = ''' INSERT INTO concursos(n1,n2,n3,n4,n5)
              VALUES(?,?,?,?,?) '''
numeros = (2,3,4,5,6);
cur.execute(sql, numeros)
conn.commit()
conn.close()


