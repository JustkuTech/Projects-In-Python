#Gestor de Biblioteca 
#Elaborado por Javier Paez Torres ING. Sistemas

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QMessageBox, QComboBox
import json
import os
from PyQt5.QtGui import QPixmap
import subprocess

print("Directorio actual:", os.getcwd())

# Obtener la ruta del directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta del archivo .qrc
qrc_file = os.path.join(script_dir, "recursos.qrc")

# Ruta de salida del archivo .py
output_py = os.path.join(script_dir, "recursos.py")

# Ruta de pyrcc5
pyrcc5_path = "C:/Users/paezt/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/local-packages/Python311/Scripts/pyrcc5.exe"

# Ejecutar pyrcc5 utilizando subprocess
subprocess.run([pyrcc5_path, qrc_file, "-o", output_py])

class ReturnBookWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Devolver Libro Prestado")
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        layout.addWidget(QLabel("Selecciona el libro a devolver:"))
        self.book_combo_box = QComboBox()
        self.book_combo_box.addItems([title for title, available in parent.borrowed_books.items() if available])
        layout.addWidget(self.book_combo_box)
        return_button = QPushButton("Devolver")
        return_button.clicked.connect(self.return_book)
        layout.addWidget(return_button)

    def return_book(self):
        title = self.book_combo_box.currentText()
        self.parent().return_book(title)
        self.close()

class BorrowBookWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Pedir Libro Prestado")
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        layout.addWidget(QLabel("Selecciona el libro a pedir prestado:"))
        self.book_combo_box = QComboBox()
        self.refresh_books()
        layout.addWidget(self.book_combo_box)
        borrow_button = QPushButton("Pedir prestado")
        borrow_button.clicked.connect(self.borrow_book)
        layout.addWidget(borrow_button)

    def refresh_books(self):
        self.book_combo_box.clear()
        self.book_combo_box.addItems([title for title, (author, borrowed) in self.parent().borrowed_books.items() if not borrowed])

    def borrow_book(self):
        title = self.book_combo_box.currentText()
        self.parent().borrow_book(title)
        self.refresh_books()
        self.close()

class LibraryManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Biblioteca")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # Obtener la ruta del directorio actual del script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Ruta relativa del archivo de imagen
        image_path = "icon.png"

        print("Ruta de la imagen:", image_path)  # Imprime la ruta para verificar

        # Intentar cargar la imagen en un QPixmap
        pixmap = QPixmap(image_path)

        # Verificar si el QPixmap se ha creado correctamente
        if not pixmap.isNull():
            # Agregar la imagen al menú principal
            image_label = QLabel(self)
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label)
        else:
            print("Error: No se pudo cargar la imagen")

        welcome_label = QLabel("Bienvenido al Gestor de Biblioteca")
        layout.addWidget(welcome_label)

        add_book_button = QPushButton("Agregar libro")
        view_books_button = QPushButton("Consultar libros")
        borrow_book_button = QPushButton("Pedir libro prestado")
        return_book_button = QPushButton("Devolver libro prestado")
        layout.addWidget(add_book_button)
        layout.addWidget(view_books_button)
        layout.addWidget(borrow_book_button)
        layout.addWidget(return_book_button)

        
        add_book_button.clicked.connect(self.open_add_book_window)
        view_books_button.clicked.connect(self.open_view_books_window)
        borrow_book_button.clicked.connect(self.open_borrow_book_window)
        return_book_button.clicked.connect(self.open_return_book_window)

        
        self.borrowed_books = {}
        self.load_data()

    def load_data(self):
        try:
            with open("library_data.json", "r") as file:
                self.borrowed_books = json.load(file)
        except FileNotFoundError:
            self.borrowed_books = {}

    def save_data(self):
        with open("library_data.json", "w") as file:
            json.dump(self.borrowed_books, file)

    def open_add_book_window(self):
        add_book_window = AddBookWindow(self)
        add_book_window.exec_()

    def open_view_books_window(self):
        view_books_window = ViewBooksWindow(self)
        view_books_window.exec_()

    def open_borrow_book_window(self):
        borrow_book_window = BorrowBookWindow(self)
        borrow_book_window.exec_()

    def open_return_book_window(self):
        return_book_window = ReturnBookWindow(self)
        return_book_window.exec_()

    def add_book(self, title, author):
        if title and author:
            self.borrowed_books[title] = (author, False) 
            self.save_data()
            QMessageBox.information(self, "Éxito", "Libro agregado correctamente.")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, completa todos los campos.")

    def borrow_book(self, title):
        if title in self.borrowed_books:
            if not self.borrowed_books[title][1]:
                self.borrowed_books[title] = (self.borrowed_books[title][0], True)
                self.save_data()
                QMessageBox.information(self, "Éxito", f"Has pedido prestado el libro '{title}'.")
            else:
                QMessageBox.warning(self, "Advertencia", f"El libro '{title}' ya ha sido prestado.")
        else:
            QMessageBox.warning(self, "Advertencia", f"El libro '{title}' no está disponible en la biblioteca.")

    def return_book(self, title):
        if title in self.borrowed_books:
            if self.borrowed_books[title][1]:
                self.borrowed_books[title] = (self.borrowed_books[title][0], False)
                self.save_data()
                QMessageBox.information(self, "Éxito", f"Has devuelto el libro '{title}'.")
            else:
                QMessageBox.warning(self, "Advertencia", f"El libro '{title}' no ha sido prestado.")
        else:
            QMessageBox.warning(self, "Advertencia", f"El libro '{title}' no está disponible en la biblioteca.")

class AddBookWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Agregar Libro")
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        # Widgets
        layout.addWidget(QLabel("Título:"))
        self.title_input = QLineEdit()
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Autor:"))
        self.author_input = QLineEdit()
        layout.addWidget(self.author_input)
        # Botón para agregar libro
        add_button = QPushButton("Agregar")
        add_button.clicked.connect(self.add_book)
        layout.addWidget(add_button)

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        self.parent().add_book(title, author)
        self.close()

class ViewBooksWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Consultar Libros")
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        layout.addWidget(QLabel("Lista de libros:"))
        for title, (author, borrowed) in parent.borrowed_books.items():
            status = "Disponible" if not borrowed else "Prestado"
            layout.addWidget(QLabel(f"Título: {title}, Autor: {author}, Estado: {status}"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryManager()
    window.show()
    sys.exit(app.exec_())