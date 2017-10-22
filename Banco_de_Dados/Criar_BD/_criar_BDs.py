import sqlite3

## cria todos os BD de uma vez

con = sqlite3.connect("lotofacil.db")
cur = con.cursor()
cur.executescript("""
    CREATE TABLE concursos (
    concurso_id  INTEGER PRIMARY KEY AUTOINCREMENT
                NOT NULL,
    n1  INTEGER NOT NULL,
    n2  INTEGER NOT NULL,
    n3  INTEGER NOT NULL,
    n4  INTEGER NOT NULL,
    n5  INTEGER NOT NULL,
    n6  INTEGER NOT NULL,
    n7  INTEGER NOT NULL,
    n8  INTEGER NOT NULL,
    n9  INTEGER NOT NULL,
    n10 INTEGER NOT NULL,
    n11 INTEGER NOT NULL,
    n12 INTEGER NOT NULL,
    n13 INTEGER NOT NULL,
    n14 INTEGER NOT NULL,
    n15 INTEGER NOT NULL
);

	CREATE TABLE todas_combinacoes (
    game_id  INTEGER PRIMARY KEY AUTOINCREMENT
                NOT NULL,
    n1  INTEGER NOT NULL,
    n2  INTEGER NOT NULL,
    n3  INTEGER NOT NULL,
    n4  INTEGER NOT NULL,
    n5  INTEGER NOT NULL,
    n6  INTEGER NOT NULL,
    n7  INTEGER NOT NULL,
    n8  INTEGER NOT NULL,
    n9  INTEGER NOT NULL,
    n10 INTEGER NOT NULL,
    n11 INTEGER NOT NULL,
    n12 INTEGER NOT NULL,
    n13 INTEGER NOT NULL,
    n14 INTEGER NOT NULL,
    n15 INTEGER NOT NULL
);


    """)
con.close()


con = sqlite3.connect("megasena.db")
cur = con.cursor()
cur.executescript("""
    CREATE TABLE concursos (
    concurso_id  INTEGER PRIMARY KEY AUTOINCREMENT
                NOT NULL,
    n1  INTEGER NOT NULL,
    n2  INTEGER NOT NULL,
    n3  INTEGER NOT NULL,
    n4  INTEGER NOT NULL,
    n5  INTEGER NOT NULL,
    n6  INTEGER NOT NULL
);

	CREATE TABLE todas_combinacoes (
    game_id  INTEGER PRIMARY KEY AUTOINCREMENT
                NOT NULL,
    n1  INTEGER NOT NULL,
    n2  INTEGER NOT NULL,
    n3  INTEGER NOT NULL,
    n4  INTEGER NOT NULL,
    n5  INTEGER NOT NULL,
    n6  INTEGER NOT NULL
);


    """)
con.close()



con = sqlite3.connect("quina.db")
cur = con.cursor()
cur.executescript("""
    CREATE TABLE concursos (
    concurso_id  INTEGER PRIMARY KEY AUTOINCREMENT
                NOT NULL,
    n1  INTEGER NOT NULL,
    n2  INTEGER NOT NULL,
    n3  INTEGER NOT NULL,
    n4  INTEGER NOT NULL,
    n5  INTEGER NOT NULL
);

	CREATE TABLE todas_combinacoes (
    game_id  INTEGER PRIMARY KEY AUTOINCREMENT
                NOT NULL,
    n1  INTEGER NOT NULL,
    n2  INTEGER NOT NULL,
    n3  INTEGER NOT NULL,
    n4  INTEGER NOT NULL,
    n5  INTEGER NOT NULL
);


    """)
con.close()
