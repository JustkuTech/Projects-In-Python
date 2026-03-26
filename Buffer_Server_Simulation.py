#ESTUDIANTES: Javier Paez Torres - Kevin Medina
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import time

BUFFER_SIZE = 5
NUM_OPERACIONES = 10

class Logger:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self._init_tags()

    def _init_tags(self):
        self.text_widget.tag_config("servidor", foreground="blue")
        self.text_widget.tag_config("jugador", foreground="green")

    def log(self, message, tag=None):
        print(message)
        self.text_widget.after(0, self._append_text, message, tag)

    def _append_text(self, message, tag):
        self.text_widget.insert(tk.END, message + "\n", tag)
        self.text_widget.see(tk.END)

class GameServerBuffer:
    def __init__(self, capacidad, gui_log, buffer_label):
        self.buffer = []
        self.capacidad = capacidad
        self.cond = threading.Condition()
        self.log = gui_log
        self.buffer_label = buffer_label

    def actualizar_gui(self):
        self.buffer_label.after(0, lambda: self.buffer_label.config(text=f'Partidas activas: {self.buffer}'))

    def crear_partida(self, partida):
        with self.cond:
            while len(self.buffer) >= self.capacidad:
                self.cond.wait()
            assert len(self.buffer) < self.capacidad, "¡Buffer sobrecargado!"
            self.buffer.append(partida)
            self.log.log(f'Servidor creó partida: {partida}', "servidor")
            self.actualizar_gui()
            self.cond.notify()

    def entrar_partida(self):
        with self.cond:
            while not self.buffer:
                self.cond.wait()
            assert len(self.buffer) > 0, "¡Consumo desde buffer vacío!"
            partida = self.buffer.pop(0)
            self.log.log(f'Jugador se unió a: {partida}', "jugador")
            self.actualizar_gui()
            self.cond.notify()
            return partida

class Servidor(threading.Thread):
    def __init__(self, buffer, num_items):
        super().__init__()
        self.buffer = buffer
        self.num_items = num_items

    def run(self):
        for i in range(self.num_items):
            partida = f'Partida-{i+1}'
            time.sleep(0.5)
            self.buffer.crear_partida(partida)

class Jugador(threading.Thread):
    def __init__(self, buffer, num_items):
        super().__init__()
        self.buffer = buffer
        self.num_items = num_items

    def run(self):
        for _ in range(self.num_items):
            time.sleep(0.9)
            self.buffer.entrar_partida()

def iniciar_simulacion(log_widget, buffer_label):
    logger = Logger(log_widget)
    buffer = GameServerBuffer(BUFFER_SIZE, logger, buffer_label)
    servidor = Servidor(buffer, NUM_OPERACIONES)
    jugador = Jugador(buffer, NUM_OPERACIONES)
    servidor.start()
    jugador.start()

# GUI Principal
root = tk.Tk()
root.title("Servidor de Videojuegos - Productor y Consumidor (Verificación)")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

buffer_label = tk.Label(frame, text="Partidas activas: []", font=("Arial", 12))
buffer_label.pack()

log_text = ScrolledText(frame, height=15, width=50, font=("Courier", 10))
log_text.pack(pady=10)

btn_iniciar = tk.Button(frame, text="Iniciar Simulación", command=lambda: iniciar_simulacion(log_text, buffer_label))
btn_iniciar.pack()

root.mainloop()
