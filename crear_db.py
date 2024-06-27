import sqlite3

db_name = 'mediciones.db'
conn = sqlite3.connect(db_name)
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS mediciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Aperes REAL,
    voltaje REAL,
    velocidad REAL,
    tiempo REAL
)
''')

conn.commit()
conn.close()

