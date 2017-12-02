import sqlite3

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
