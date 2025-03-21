'''
ID (primary key                     '1')
ARTICULO (CODIGO                    'DS45A4') 
MODELO (TIPO DE CALZADO/ESTILO      'Zapatilla')
NOMBRE (CALZADO                     'New bilori')
MARCA (CALZADO                      'Hush puppies')
TALLE (CALZADO                      '35')
COLOR (CALZADO                      'Negro')
STOCK (CANTIDAD                     '25')
'''

import sqlite3 as sql

# Función para crear la tabla si no existe
def crear_tabla():
    conn = sql.connect('zapateria.db')
    cursor = conn.cursor()
    
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS calzado (
        ID INTEGER PRIMARY KEY,
        ARTICULO TEXT,
        MODELO TEXT,
        NOMBRE TEXT,
        MARCA TEXT,
        TALLE INTEGER,
        COLOR TEXT,
        STOCK INTEGER
    )
    ''')
    
    # Confirmar los cambios
    conn.commit()
    conn.close()

# Función para agregar un nuevo calzado
def agregar_calzado(articulo, modelo, nombre, marca, talle, color, stock):
    conn = sql.connect('zapateria.db')
    cursor = conn.cursor()
    
    # Verificar si el calzado ya existe en la base de datos
    cursor.execute('''SELECT * FROM calzado WHERE ARTICULO = ?''', (articulo,))
    resultado = cursor.fetchone()
    
    # Si no existe, se agrega el calzado, de lo contrario no se hace nada
    if resultado is None:
        cursor.execute('''
        INSERT INTO calzado (ARTICULO, MODELO, NOMBRE, MARCA, TALLE, COLOR, STOCK)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (articulo, modelo, nombre, marca, talle, color, stock))
        
        print(f"Calzado {articulo} agregado correctamente.")
    else:
        print(f"El calzado {articulo} ya existe en la base de datos.")
    
    # Confirmar los cambios
    conn.commit()
    conn.close()

# Crear la tabla si no existe
crear_tabla()

# Ejemplo de cómo agregar calzado, solo si no existe previamente
agregar_calzado('DS45B3', 'Bota', 'New walk', 'Nike', 42, 'Azul', 30)
agregar_calzado('DS45C2', 'Sandalia', 'Summer feet', 'Adidas', 38, 'Rojo', 15)
agregar_calzado('DS45D1', 'Bota', 'Winter king', 'Puma', 40, 'Negro', 50)

# Intentar agregar un calzado repetido
agregar_calzado('REJ321', 'Zapatilla', 'New bilori', 'Hush Puppies', 35, 'Negro', 50)
agregar_calzado('DS45B3', 'Bota', 'New walk', 'Nike', 42, 'Azul', 30)  # Este no se agregará porque ya existe
