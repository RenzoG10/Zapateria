import customtkinter as ctk
import db  # Importamos las funciones de la base de datos

class ZapateriaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Stock - Zapatería")
        self.geometry("700x700")  # Ajustamos el tamaño de la ventana para que quepan todos los elementos

        # 📌 Título
        self.label_titulo = ctk.CTkLabel(self, text="Gestión de Stock", font=("Arial", 20))
        self.label_titulo.pack(pady=10)

        # 📌 Campos de entrada para agregar productos
        self.entry_articulo = ctk.CTkEntry(self, placeholder_text="Código del Artículo")
        self.entry_articulo.pack(pady=5)

        self.entry_modelo = ctk.CTkEntry(self, placeholder_text="Modelo")
        self.entry_modelo.pack(pady=5)

        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
        self.entry_nombre.pack(pady=5)

        self.entry_marca = ctk.CTkEntry(self, placeholder_text="Marca")
        self.entry_marca.pack(pady=5)

        self.entry_talle = ctk.CTkEntry(self, placeholder_text="Talle")
        self.entry_talle.pack(pady=5)

        self.entry_color = ctk.CTkEntry(self, placeholder_text="Color")
        self.entry_color.pack(pady=5)
        
        self.entry_genero = ctk.CTkEntry(self, placeholder_text="Género")
        self.entry_genero.pack(pady=5)

        self.entry_fecha = ctk.CTkEntry(self, placeholder_text="Fecha")
        self.entry_fecha.pack(pady=5)

        self.entry_tipo = ctk.CTkEntry(self, placeholder_text="Tipo")
        self.entry_tipo.pack(pady=5)

        self.entry_precio = ctk.CTkEntry(self, placeholder_text="Precio de Venta")
        self.entry_precio.pack(pady=5)
        
        self.entry_stock = ctk.CTkEntry(self, placeholder_text="Stock")
        self.entry_stock.pack(pady=5)

        # 📌 Botón para agregar producto
        self.btn_guardar = ctk.CTkButton(self, text="Agregar Producto", command=self.agregar_producto)
        self.btn_guardar.pack(pady=10)

        # 📌 Lista de productos
        self.lista_productos = ctk.CTkTextbox(self, width=600, height=200)
        self.lista_productos.pack(pady=10)

        # 📌 Campos para registrar ventas
        self.entry_venta_articulo = ctk.CTkEntry(self, placeholder_text="Código del Artículo (Venta)")
        self.entry_venta_articulo.pack(pady=5)

        self.entry_venta_cantidad = ctk.CTkEntry(self, placeholder_text="Cantidad a Vender")
        self.entry_venta_cantidad.pack(pady=5)

        # 📌 Botón para registrar venta
        self.btn_vender = ctk.CTkButton(self, text="Registrar Venta", command=self.registrar_venta)
        self.btn_vender.pack(pady=10)

        # 📌 Campos para eliminar productos
        self.entry_eliminar_articulo = ctk.CTkEntry(self, placeholder_text="Código del Artículo (Eliminar)")
        self.entry_eliminar_articulo.pack(pady=5)

        # 📌 Botón para eliminar producto
        self.btn_eliminar = ctk.CTkButton(self, text="Eliminar Producto", command=self.eliminar_producto)
        self.btn_eliminar.pack(pady=10)

        # Mostrar el stock inicial al iniciar
        self.mostrar_stock()

    # 📌 Función para agregar producto
    def agregar_producto(self):
        articulo = self.entry_articulo.get()
        modelo = self.entry_modelo.get()
        nombre = self.entry_nombre.get()
        marca = self.entry_marca.get()
        talle = self.entry_talle.get()
        color = self.entry_color.get()
        genero = self.entry_genero.get()
        fecha = self.entry_fecha.get()
        tipo = self.entry_tipo.get()
        stock = self.entry_stock.get()
        precio = self.entry_precio.get()

        if all([articulo, modelo, nombre, marca, talle, color, genero, fecha, tipo, stock, precio]):
            db.agregar_calzado(
                articulo, modelo, nombre, marca, float(talle), color,
                genero.upper(), fecha, tipo.lower(), int(stock), float(precio)
            )
            self.mostrar_stock()
        else:
            print("⚠️ Todos los campos son obligatorios.")

    # 📌 Función para mostrar productos
    def mostrar_stock(self):
        productos = db.obtener_productos()
        self.lista_productos.delete("1.0", "end")

        for producto in productos:
            self.lista_productos.insert(
            "end",
            f"{producto[1]} | {producto[2]} | {producto[3]} | Talle: {producto[5]} | Stock: {producto[10]} | ${producto[11]:,.0f}\n"
        )

    # 📌 Función para registrar venta
    def registrar_venta(self):
        articulo = self.entry_venta_articulo.get()
        cantidad = self.entry_venta_cantidad.get()

        if articulo and cantidad:
            db.vender_calzado(articulo, int(cantidad))
            self.mostrar_stock()
        else:
            print("⚠️ Debes ingresar el código del artículo y la cantidad.")

    # 📌 Función para eliminar producto
    def eliminar_producto(self):
        articulo = self.entry_eliminar_articulo.get()

        if articulo:
            db.eliminar_calzado(articulo)
            self.mostrar_stock()
        else:
            print("⚠️ Debes ingresar el código del artículo para eliminar.")

if __name__ == "__main__":
    app = ZapateriaApp()
    app.mainloop()
