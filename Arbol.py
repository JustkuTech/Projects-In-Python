import tkinter as tk
from tkinter import messagebox

class ArbolInterfaz:
    def __init__(self, raiz):
        self.raiz = raiz
        self.arbol = ArbolBinario()

        self.frame = tk.Frame(self.raiz)
        self.frame.pack()

        self.valor_label = tk.Label(self.frame, text="Valor:")
        self.valor_label.pack(side=tk.LEFT)

        self.valor_entry = tk.Entry(self.frame)
        self.valor_entry.pack(side=tk.LEFT)

        self.insertar_button = tk.Button(self.frame, text="Insertar", command=self.insertar)
        self.insertar_button.pack(side=tk.LEFT)

        self.borrar_button = tk.Button(self.frame, text="Borrar", command=self.borrar)
        self.borrar_button.pack(side=tk.LEFT)

        self.pertenece_button = tk.Button(self.frame, text="Pertenece", command=self.verificar_pertenencia)
        self.pertenece_button.pack(side=tk.LEFT)

        self.contar_button = tk.Button(self.frame, text="Número de Elementos", command=self.mostrar_num_elementos)
        self.contar_button.pack(side=tk.LEFT)

        #self.visualizar_button = tk.Button(self.frame, text="Visualizar", command=self.visualizar)
        #self.visualizar_button.pack(side=tk.LEFT)

        self.altura_button = tk.Button(self.frame, text="Altura", command=self.mostrar_altura)
        self.altura_button.pack(side=tk.LEFT)

        self.limpiar_button = tk.Button(self.frame, text="Limpiar Árbol", command=self.borrar_todo)
        self.limpiar_button.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self.raiz, width=400, height=300, bg='white')
        self.canvas.pack()

        # Visualización inicial del árbol vacío
        self.visualizar()

    def insertar(self):
        valor = self.valor_entry.get()
        if valor.isdigit():
            self.arbol.insertar(int(valor))
            self.valor_entry.delete(0, tk.END)
            self.visualizar()
        else:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

    def borrar(self):
        valor = self.valor_entry.get()
        if valor.isdigit():
            self.arbol.borrar(int(valor))
            self.valor_entry.delete(0, tk.END)
            self.visualizar()
        else:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

    def verificar_pertenencia(self):
        valor = self.valor_entry.get()
        if valor.isdigit():
            pertenece = self.arbol.pertenece(int(valor))
            mensaje = f"El valor {valor} {'sí' if pertenece else 'no'} pertenece al árbol."
            messagebox.showinfo("Pertenece", mensaje)
        else:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

    def mostrar_num_elementos(self):
        num_elementos = self.arbol.contar_elementos(self.arbol.raiz)
        messagebox.showinfo("Número de Elementos", f"El árbol tiene {num_elementos} elemento(s).")

    def visualizar(self):
        self.canvas.delete("all")
        if self.arbol.es_vacio():
            self.canvas.create_text(
                200, 150, text="El árbol está vacío", 
                font=("Arial", 16), fill="gray"
            )
        else:
            self.dibujar_arbol(self.arbol.raiz, 200, 30, 100)

    def dibujar_arbol(self, nodo, x, y, offset):
        if nodo is not None:
            self.canvas.create_text(x, y, text=str(nodo.valor), font=("Arial", 12))
            if nodo.izquierdo:
                self.canvas.create_line(x, y, x - offset, y + 50)
                self.dibujar_arbol(nodo.izquierdo, x - offset, y + 50, offset // 2)
            if nodo.derecho:
                self.canvas.create_line(x, y, x + offset, y + 50)
                self.dibujar_arbol(nodo.derecho, x + offset, y + 50, offset // 2)

    def mostrar_altura(self):
        if self.arbol.es_vacio():
            self.visualizar()
        else:
            altura = self.arbol.altura(self.arbol.raiz)
            messagebox.showinfo("Altura del árbol", f"La altura del árbol es: {altura}")

    def borrar_todo(self):
        self.arbol.borrar_todo()
        self.visualizar()

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        return self.raiz is None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar(nodo.derecho, valor)

    def pertenece(self, valor):
        return self._pertenece(self.raiz, valor)

    def _pertenece(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._pertenece(nodo.izquierdo, valor)
        else:
            return self._pertenece(nodo.derecho, valor)

    def contar_elementos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_elementos(nodo.izquierdo) + self.contar_elementos(nodo.derecho)

    def borrar(self, valor):
        self.raiz = self._borrar(self.raiz, valor)

    def _borrar(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierdo = self._borrar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._borrar(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            temp = self._minimo_valor_nodo(nodo.derecho)
            nodo.valor = temp.valor
            nodo.derecho = self._borrar(nodo.derecho, temp.valor)
        return nodo

    def _minimo_valor_nodo(self, nodo):
        current = nodo
        while current.izquierdo is not None:
            current = current.izquierdo
        return current

    def altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))

    def borrar_todo(self):
        self.raiz = None

if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.title("Árbol Binario")
    app = ArbolInterfaz(raiz)
    raiz.mainloop()