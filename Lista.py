import tkinter as tk
from tkinter import messagebox

# Definición de la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Referencia al siguiente nodo

# Definición de la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Esto cargara la lista vacia lista para recibir los datos

    # Método para agregar un nodo al final de la lista
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            temp = self.cabeza
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo

    # Método para agregar un nodo al inicio de la lista
    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # Método para retirar un nodo del inicio de la lista
    def retirar_del_inicio(self):
        if not self.cabeza:
            print("La lista está vacía, no hay elementos para retirar.")
        else:
            self.cabeza = self.cabeza.siguiente

    # Método para retirar un nodo del final de la lista
    def retirar_del_final(self):
        if not self.cabeza:
            print("La lista está vacía, no hay elementos para retirar.")
        elif not self.cabeza.siguiente:
            self.cabeza = None  # Solo hay un elemento en la lista
        else:
            temp = self.cabeza
            while temp.siguiente and temp.siguiente.siguiente:
                temp = temp.siguiente
            temp.siguiente = None  # Aca le digo al codigo que elimine el último nodo

    # Método para imprimir los elementos de la lista ya que si no, el programa no devolveria nada
    def imprimir_lista(self):
        if not self.cabeza:
            return "La lista está vacía."
        else:
            elementos = []
            temp = self.cabeza
            while temp:
                elementos.append(str(temp.dato))
                temp = temp.siguiente
            return " -> ".join(elementos)

# Función principal para crear la interfaz gráfica aqui queda definida toda la logica de la parte grafica
def interfaz_grafica():
    lista = ListaEnlazada()
    
    # Funciones para la interfaz que mas adelante se implementaran en los botones
    def agregar_inicio():
        try:
            valor = int(entry.get())
            lista.agregar_al_inicio(valor)
            actualizar_lista()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def agregar_final():
        try:
            valor = int(entry.get())
            lista.agregar_al_final(valor)
            actualizar_lista()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def retirar_inicio():
        lista.retirar_del_inicio()
        actualizar_lista()

    def retirar_final():
        lista.retirar_del_final()
        actualizar_lista()

    def actualizar_lista():
        resultado.set(lista.imprimir_lista())

    # Configuración de la ventana principal practicamente para que cargue
    root = tk.Tk()
    root.title("Lista Enlazada")

    # En esta seccion estan los widgets o los botones junto al comando asignado para que al presionarlos realicen su accion correspondiente
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Valor:")
    label.grid(row=0, column=0, padx=5, pady=5)

    entry = tk.Entry(frame)
    entry.grid(row=0, column=1, padx=5, pady=5)

    boton_agregar_inicio = tk.Button(frame, text="Agregar al Inicio", command=agregar_inicio)
    boton_agregar_inicio.grid(row=1, column=0, padx=5, pady=5)

    boton_agregar_final = tk.Button(frame, text="Agregar al Final", command=agregar_final)
    boton_agregar_final.grid(row=1, column=1, padx=5, pady=5)

    boton_retirar_inicio = tk.Button(frame, text="Retirar del Inicio", command=retirar_inicio)
    boton_retirar_inicio.grid(row=2, column=0, padx=5, pady=5)

    boton_retirar_final = tk.Button(frame, text="Retirar del Final", command=retirar_final)
    boton_retirar_final.grid(row=2, column=1, padx=5, pady=5)

    resultado = tk.StringVar()
    resultado.set("La lista está vacía.")
    label_resultado = tk.Label(root, textvariable=resultado)
    label_resultado.pack(pady=10)

    # Con esto la interfaz se reinicia actualizandola en caso de insertar o quitar un dato
    root.mainloop()

# Aqui se Llama a la función de interfaz gráfica si no, el codigo no la muestra
if __name__ == "__main__":
    interfaz_grafica()