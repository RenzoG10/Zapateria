import sqlite3 as sql

# 📌 Conectar a la base de datos
def conectar_db():
    return sql.connect("zapateria.db")

# 📌 Crear la tabla si no existe
def crear_tabla():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS calzado (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ARTICULO TEXT UNIQUE NOT NULL,
        MODELO TEXT NOT NULL,
        NOMBRE TEXT NOT NULL,
        MARCA TEXT NOT NULL,
        TALLE REAL NOT NULL,
        COLOR TEXT NOT NULL,
        GENERO TEXT NOT NULL,
        FECHA TEXT,
        TIPO TEXT,
        STOCK INTEGER NOT NULL,
        PRECIO_VENTA REAL
    )
    ''')

    conn.commit()
    conn.close()

# 📌 Agregar un nuevo calzado
def agregar_calzado(articulo, modelo, nombre, marca, talle, color, genero, fecha, tipo, stock, precio_venta):
    conn = conectar_db()
    cursor = conn.cursor()

    try:
        cursor.execute(''' 
        INSERT INTO calzado (ARTICULO, MODELO, NOMBRE, MARCA, TALLE, COLOR, GENERO, FECHA, TIPO, STOCK, PRECIO_VENTA)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (articulo, modelo, nombre, marca, talle, color, genero, fecha, tipo, stock, precio_venta))
        conn.commit()
    except sql.IntegrityError:
        print(f"⚠️ El calzado {articulo} ya existe en la base de datos.")
    conn.close()

# 📌 Obtener todos los productos
def obtener_productos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM calzado")
    productos = cursor.fetchall()
    conn.close()
    return productos

# 📌 Registrar una venta y actualizar el stock
def vender_calzado(articulo, cantidad):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT STOCK FROM calzado WHERE ARTICULO = ?", (articulo,))
    stock_actual = cursor.fetchone()

    if stock_actual and stock_actual[0] >= cantidad:
        cursor.execute("UPDATE calzado SET STOCK = STOCK - ? WHERE ARTICULO = ?", (cantidad, articulo))
        conn.commit()
    else:
        print(f"⚠️ No hay suficiente stock para vender {cantidad} unidades de {articulo}.")

    conn.close()

# 📌 Eliminar un producto
def eliminar_calzado(articulo):
    conn = conectar_db()
    cursor = conn.cursor()

    # Verificar si el artículo existe antes de eliminarlo
    cursor.execute("SELECT * FROM calzado WHERE ARTICULO = ?", (articulo,))
    producto = cursor.fetchone()

    if producto:
        cursor.execute("DELETE FROM calzado WHERE ARTICULO = ?", (articulo,))
        conn.commit()
        print(f"✅ El calzado {articulo} ha sido eliminado.")
    else:
        print(f"⚠️ El calzado con código {articulo} no existe.")

    conn.close()

# 📌 Crear la tabla al iniciar
crear_tabla()
