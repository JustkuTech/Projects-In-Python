import tkinter as tk
from tkinter import ttk, messagebox
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

    # Métodos de ordenamiento
    def sort_by_exchange(self):
        """Ordenación por intercambio (burbuja)"""
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def sort_by_selection(self):
        """Ordenación por selección"""
        current = self.head
        while current:
            min_node = current
            next_node = current.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            current.data, min_node.data = min_node.data, current.data
            current = current.next

    def sort_by_insertion(self):
        """Ordenación por inserción"""
        if not self.head or not self.head.next:
            return

        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
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

    def sort_by_shell(self):
        """Ordenación por Shell"""
        n = self.get_length()
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.get_node_at_index(i).data
                j = i
                while j >= gap and self.get_node_at_index(j - gap).data > temp:
                    self.get_node_at_index(j).data = self.get_node_at_index(j - gap).data
                    j -= gap
                self.get_node_at_index(j).data = temp
            gap //= 2

    def sort_by_quick(self):
        """Ordenación rápida"""
        end = self.head
        while end and end.next:
            end = end.next
        self.quicksort_recursive(self.head, end)

    def quicksort_recursive(self, start, end):
        if start is None or end is None or start == end:
            return

        pivot_prev = self.partition(start, end)
        self.quicksort_recursive(start, pivot_prev)

        if pivot_prev is not None and pivot_prev.next is not None:
            self.quicksort_recursive(pivot_prev.next, end)

    def partition(self, start, end):
        if start == end or start is None or end is None:
            return start

        pivot_prev = start
        current = start
        pivot_value = end.data

        while start != end:
            if start.data < pivot_value:
                pivot_prev = current
                current.data, start.data = start.data, current.data
                current = current.next
            start = start.next

        current.data, end.data = end.data, current.data
        return pivot_prev

    # Métodos auxiliares
    def get_length(self):
        """Obtener la longitud de la lista"""
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def get_node_at_index(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def generate_random_data(self, n, min_val=1, max_val=100):
        """Generar datos aleatorios en la lista"""
        for _ in range(n):
            self.append(random.randint(min_val, max_val))

class LinkedListApp:
    def __init__(self, root):
        self.linked_list = LinkedList()
        self.root = root
        self.root.title("Lista Enlazada - Métodos de Ordenamiento")

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

        # Selección del método de ordenamiento
        self.sorting_method_label = tk.Label(root, text="Método de Ordenamiento:")
        self.sorting_method_label.pack()
        self.sorting_method = ttk.Combobox(root, values=["Intercambio", "Selección", "Inserción", "Shell", "Quicksort"])
        self.sorting_method.pack()
        self.sorting_method.current(0)

        # Botones
        self.generate_button = tk.Button(root, text="Generar Lista Aleatoria", command=self.generate_random_list)
        self.generate_button.pack()

        self.display_button = tk.Button(root, text="Mostrar Lista Actual", command=self.display_list)
        self.display_button.pack()

        self.sort_button = tk.Button(root, text="Ordenar Lista", command=self.sort_list)
        self.sort_button.pack()

        # Área de texto para mostrar la lista
        self.result_label = tk.Label(root, text="Resultado:")
        self.result_label.pack()
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

        # Label para mostrar el tiempo de ejecución
        self.execution_time_label = tk.Label(root, text="Tiempo de ejecución: ---")
        self.execution_time_label.pack()

    def generate_random_list(self):
        """Generar y mostrar la lista en la interfaz"""
        try:
            n = int(self.num_elements_entry.get())
            min_val = int(self.min_val_entry.get())
            max_val = int(self.max_val_entry.get())
            self.linked_list = LinkedList()  # Reiniciar la lista
            self.linked_list.generate_random_data(n, min_val, max_val)
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
        """lista según el método seleccionado y mostrar el resultado"""
        method = self.sorting_method.get()
        self.linked_list = LinkedList()
        for data in map(int, self.unsorted_display.split(" -> ")):
            self.linked_list.append(data)

        start_time = time.time()

        if method == "Intercambio":
            self.linked_list.sort_by_exchange()
        elif method == "Selección":
            self.linked_list.sort_by_selection()
        elif method == "Inserción":
            self.linked_list.sort_by_insertion()
        elif method == "Shell":
            self.linked_list.sort_by_shell()
        elif method == "Quicksort":
            self.linked_list.sort_by_quick()

        end_time = time.time()
        elapsed_time = end_time - start_time

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Lista ordenada por {method}:\n{self.linked_list.display()}\n")
        self.execution_time_label.config(text=f"Tiempo de ejecución: {elapsed_time:.6f} segundos")

# Configuración de la ventana principal
root = tk.Tk()
app = LinkedListApp(root)
root.mainloop()