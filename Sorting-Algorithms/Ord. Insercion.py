import tkinter as tk
from tkinter import messagebox
import random
import time

class Node:
    """Nodo de una lista enlazada simple"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Lista enlazada simple"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Agregar un nuevo nodo al final de la lista"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """Mostrar los elementos de la lista"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return " -> ".join(map(str, elements))

    def sort_by_insertion(self):
        """Ordenación por inserción en la lista enlazada"""
        if not self.head or not self.head.next:
            return

        sorted_list = None  # Nueva lista para los nodos ordenados
        current = self.head
        while current:
            next_node = current.next
            # Insertar current en sorted_list en la posición correcta
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while sorted_current.next and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node
        self.head = sorted_list

    def generate_random_data(self, n, min_val=1, max_val=100):
        """Generar 'n' datos aleatorios en la lista"""
        for _ in range(n):
            self.append(random.randint(min_val, max_val))

class LinkedListApp:
    def __init__(self, root):
        self.linked_list = LinkedList()
        self.root = root
        self.root.title("Lista Enlazada - Ordenación por Inserción")
        
        # Almacena la lista generada sin ordenar
        self.unsorted_display = ""

        # Entrada para número de elementos
        self.num_elements_label = tk.Label(root, text="Número de elementos:")
        self.num_elements_label.pack()
        self.num_elements_entry = tk.Entry(root)
        self.num_elements_entry.pack()

        # Entrada para valor mínimo y máximo
        self.min_val_label = tk.Label(root, text="Valor mínimo:")
        self.min_val_label.pack()
        self.min_val_entry = tk.Entry(root)
        self.min_val_entry.pack()

        self.max_val_label = tk.Label(root, text="Valor máximo:")
        self.max_val_label.pack()
        self.max_val_entry = tk.Entry(root)
        self.max_val_entry.pack()

        # Botones
        self.generate_button = tk.Button(root, text="Generar Lista Aleatoria", command=self.generate_random_list)
        self.generate_button.pack()

        self.display_button = tk.Button(root, text="Mostrar Lista Actual", command=self.display_list)
        self.display_button.pack()

        self.sort_button = tk.Button(root, text="Ordenar Lista por Inserción", command=self.sort_list)
        self.sort_button.pack()

        # Área de texto para mostrar la lista y el tiempo
        self.result_label = tk.Label(root, text="Resultado:")
        self.result_label.pack()
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def generate_random_list(self):
        """Generar y mostrar lista aleatoria en la interfaz"""
        try:
            n = int(self.num_elements_entry.get())
            min_val = int(self.min_val_entry.get())
            max_val = int(self.max_val_entry.get())
            self.linked_list = LinkedList()  # Reiniciar la lista
            self.linked_list.generate_random_data(n, min_val, max_val)
            # Guardar la visualización de la lista generada
            self.unsorted_display = self.linked_list.display()
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Lista aleatoria generada:\n{self.unsorted_display}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def display_list(self):
        """Mostrar la lista sin ordenar en la interfaz"""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Lista actual (sin ordenar):\n{self.unsorted_display}")

    def sort_list(self):
        """Ordenar la lista por inserción y mostrar el resultado con el tiempo de ejecución"""
        # Reinicializar la lista a su estado sin ordenar
        self.linked_list = LinkedList()
        for data in map(int, self.unsorted_display.split(" -> ")):
            self.linked_list.append(data)

        # Medir el tiempo de ordenación
        start_time = time.time()
        self.linked_list.sort_by_insertion()
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Mostrar el resultado y el tiempo
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Lista ordenada por inserción:\n{self.linked_list.display()}\n")
        self.result_text.insert(tk.END, f"Tiempo de ordenación: {elapsed_time:.6f} segundos")

# Configuración de la ventana principal
root = tk.Tk()
app = LinkedListApp(root)
root.mainloop()