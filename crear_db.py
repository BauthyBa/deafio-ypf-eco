import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('ejemplo.db')
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY,
    fecha TEXT,
    producto TEXT,
    cantidad INTEGER,
    precio REAL
)
''')

# Insertar datos de ejemplo
cursor.executemany('''
INSERT INTO ventas (fecha, producto, cantidad, precio) VALUES (?, ?, ?, ?)
''', [
    ('2023-06-01', 'Producto A', 10, 9.99),
    ('2023-06-02', 'Producto B', 5, 19.99),
    ('2023-06-03', 'Producto A', 7, 9.99),
    ('2023-06-04', 'Producto C', 3, 29.99),
    ('2023-06-05', 'Producto B', 4, 19.99)
])

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
