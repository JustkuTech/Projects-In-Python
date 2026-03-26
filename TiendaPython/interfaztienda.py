import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image  # Se requiere instalar Pillow para manejar imágenes

class SistemaCompras:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Compras")
        self.root.geometry("800x600")
        self.root.configure(bg="yellow")  # Fondo amarillo

        # Inicialización de productos con sus precios
        self.productos = {
            'Bebidas': {
                'Agua': 1.5,
                'Refresco': 2.0,
                'Jugo de Naranja': 2.5,
                'Té Helado': 1.75,
                'Café': 3.0
            },
            'Comidas': {
                'Hamburguesa': 5.0,
                'Pizza': 7.0,
                'Ensalada César': 4.5,
                'Sándwich de Pollo': 3.5,
                'Pasta Alfredo': 6.0
            },
            'Dulces': {
                'Chocolate': 3.0,
                'Galletas': 2.5,
                'Pastelito': 1.75,
                'Helado de Vainilla': 4.0,
                'Brownie': 2.0
            },
            'Objetos de Aseo': {
                'Papel Higiénico': 1.0,
                'Jabón de Manos': 1.5,
                'Shampoo': 3.0,
                'Dentífrico': 2.0,
                'Toallas de Papel': 1.25
            }
        }

        self.carrito = {}  # Diccionario para almacenar los productos seleccionados

        # Crear componentes de la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Etiqueta de bienvenida en rojo
        self.titulo = tk.Label(self.root, text="Bienvenido al Sistema de Compras", font=("Arial", 16, "bold"), pady=10, fg="red", bg="yellow")
        self.titulo.pack()

        # Contenedor para la imagen y la etiqueta de bienvenida
        contenedor_logo = tk.Frame(self.root, bg="yellow")
        contenedor_logo.pack(pady=10)

        # Cargar y mostrar la imagen sin borde
        imagen_logo = Image.open("OXXO_logo.jpeg")
        imagen_resized = imagen_logo.resize((300, 150), Image.LANCZOS)  # Ajustar tamaño a 300x150 pixels
        self.imagen = ImageTk.PhotoImage(imagen_resized)
        self.label_imagen = tk.Label(contenedor_logo, image=self.imagen, bd=0)  # Sin borde
        self.label_imagen.pack()

        # Botón para mostrar categorías de productos con fondo rojo y letras negras
        self.boton_categorias = tk.Button(self.root, text="Categorías", font=("Arial", 14), bg="red", fg="black", bd=2, relief=tk.RAISED, command=self.mostrar_categorias)
        self.boton_categorias.pack(pady=10)

        # Botón para ver el carrito de compra con fondo rojo y letras negras
        self.boton_carrito = tk.Button(self.root, text="Carrito de Compra", font=("Arial", 14), bg="red", fg="black", bd=2, relief=tk.RAISED, command=self.mostrar_carrito)
        self.boton_carrito.pack(pady=10)

        # Etiqueta para mostrar el total de la compra
        self.etiqueta_total = tk.Label(self.root, text="", font=("Arial", 14), bg="yellow")
        self.etiqueta_total.pack(pady=10)

    def mostrar_categorias(self):
        # Ventana para mostrar las categorías de productos
        self.ventana_categorias = tk.Toplevel(self.root)
        self.ventana_categorias.title("Categorías de Productos")
        self.ventana_categorias.geometry("400x300")
        self.ventana_categorias.configure(bg="yellow")  # Fondo amarillo

        for categoria in self.productos.keys():
            tk.Button(self.ventana_categorias, text=categoria, font=("Arial", 12), bg="red", fg="black", bd=2, relief=tk.RAISED,
                      command=lambda cat=categoria: self.mostrar_productos_categoria(cat)).pack(pady=5)

    def mostrar_productos_categoria(self, categoria):
        # Ventana para mostrar los productos de una categoría específica
        self.ventana_productos = tk.Toplevel(self.ventana_categorias)
        self.ventana_productos.title(f"Productos de {categoria}")
        self.ventana_productos.geometry("600x400")
        self.ventana_productos.configure(bg="yellow")  # Fondo amarillo

        # Mostrar los productos de la categoría seleccionada con opciones de cantidad
        for producto, precio in self.productos[categoria].items():
            frame_producto = tk.Frame(self.ventana_productos, bg="yellow")
            frame_producto.pack(pady=5)

            tk.Label(frame_producto, text=f"{producto} - ${precio:.2f}", font=("Arial", 12), bg="yellow").pack(side=tk.LEFT)

            # Campo de entrada para cantidad
            cantidad = tk.IntVar()
            cantidad.set(0)
            entry_cantidad = tk.Entry(frame_producto, textvariable=cantidad, width=5)
            entry_cantidad.pack(side=tk.LEFT, padx=10)

            # Botón para agregar al carrito
            tk.Button(frame_producto, text="Agregar al Carrito", font=("Arial", 12), bg="red", fg="black", bd=2, relief=tk.RAISED,
                      command=lambda prod=producto, prec=precio, cant=cantidad: self.agregar_producto_carrito(prod, prec, cant.get())).pack(side=tk.LEFT)

    def agregar_producto_carrito(self, producto, precio, cantidad):
        if cantidad > 0:
            if producto in self.carrito:
                self.carrito[producto] += cantidad
            else:
                self.carrito[producto] = cantidad

            messagebox.showinfo("Producto Agregado", f"Se han agregado {cantidad} {producto} al carrito.")
        else:
            messagebox.showwarning("Cantidad Inválida", "La cantidad debe ser mayor que cero.")

    def mostrar_carrito(self):
        # Ventana para mostrar el carrito de compra
        self.ventana_carrito = tk.Toplevel(self.root)
        self.ventana_carrito.title("Carrito de Compra")
        self.ventana_carrito.geometry("600x400")
        self.ventana_carrito.configure(bg="yellow")  # Fondo amarillo

        if not self.carrito:
            tk.Label(self.ventana_carrito, text="El carrito está vacío", font=("Arial", 14), bg="yellow").pack(pady=10)
        else:
            tk.Label(self.ventana_carrito, text="Carrito de Compra", font=("Arial", 16, "bold"), bg="yellow").pack(pady=10)
            total = 0.0
            for producto, cantidad in self.carrito.items():
                precio_unitario = self.productos[self.obtener_categoria(producto)][producto]
                subtotal = precio_unitario * cantidad
                total += subtotal
                tk.Label(self.ventana_carrito, text=f"{producto} x {cantidad} - ${subtotal:.2f}", font=("Arial", 12), bg="yellow").pack()

            tk.Label(self.ventana_carrito, text=f"Total de la Compra: ${total:.2f}", font=("Arial", 14, "bold"), bg="yellow").pack(pady=10)
            tk.Button(self.ventana_carrito, text="Vaciar Carrito", font=("Arial", 12), bg="red", fg="black", bd=2, relief=tk.RAISED, command=self.vaciar_carrito).pack(pady=10)
            tk.Button(self.ventana_carrito, text="Confirmar Compra", font=("Arial", 12), bg="red", fg="black", bd=2, relief=tk.RAISED, command=self.confirmar_compra).pack()

    def vaciar_carrito(self):
        self.carrito.clear()
        self.ventana_carrito.destroy()  # Cerrar la ventana de carrito después de vaciarlo

    def obtener_categoria(self, producto):
        for categoria, productos in self.productos.items():
            if producto in productos:
                return categoria
        return None

    def confirmar_compra(self):
        # Limpiar el carrito después de confirmar la compra
        self.carrito.clear()
        messagebox.showinfo("Compra Confirmada", "¡Gracias por su compra! El carrito ha sido vaciado.")

        # Cerrar ventana de carrito después de confirmar compra
        self.ventana_carrito.destroy()

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaCompras(root)
    root.mainloop()
