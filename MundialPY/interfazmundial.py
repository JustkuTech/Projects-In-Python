import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class MundialFutbol:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Mundial de Fútbol")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.equipos = {
            'Argentina': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Brasil': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Francia': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Alemania': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'España': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Italia': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Inglaterra': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Portugal': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Paises Bajos': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0},
            'Belgica': {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0}
        }
        self.estadios = {}
        self.partidos = []

        # Lista de jugadores por equipo
        self.jugadores_por_equipo = {
            'Argentina': [
                "Emiliano Martínez - 31 años - Portero",
                "Nahuel Molina - 26 años - Lateral derecho",
                "Cristian Romero - 26 años - Defensa central",
                "Nicolás Otamendi - 36 años - Defensa central",
                "Nicolás Tagliafico - 31 años - Lateral izquierdo",
                "Rodrigo De Paul - 30 años - Centrocampista",
                "Leandro Paredes - 29 años - Centrocampista",
                "Giovani Lo Celso - 28 años - Centrocampista",
                "Lionel Messi - 36 años - Delantero",
                "Lautaro Martínez - 26 años - Delantero",
                "Ángel Di María - 36 años - Delantero"
            ],
            'Brasil': [
                "Alisson Becker - 31 años - Portero",
                "Danilo Luiz da Silva - 32 años - Lateral derecho",
                "Marquinhos - 30 años - Defensa central",
                "Thiago Silva - 39 años - Defensa central",
                "Alex Sandro - 33 años - Lateral izquierdo",
                "Casemiro - 32 años - Centrocampista",
                "Lucas Paquetá - 26 años - Centrocampista",
                "Bruno Guimarães - 26 años - Centrocampista",
                "Neymar Jr. - 32 años - Delantero",
                "Vinícius Júnior - 23 años - Delantero",
                "Richarlison - 27 años - Delantero"
            ],
            'Francia':[
                "Mike Maignan - 28 años - Portero",
                "Benjamin Pavard - 28 años - Lateral derecho",
                "Raphaël Varane - 31 años - Defensa central",
                "Jules Koundé - 25 años - Defensa central",
                "Théo Hernandez - 26 años - Lateral izquierdo",
                "Aurélien Tchouaméni - 24 años - Centrocampista",
                "Adrien Rabiot - 29 años - Centrocampista",
                "Antoine Griezmann - 33 años - Centrocampista ofensivo",
                "Kylian Mbappé - 25 años - Delantero",
                "Ousmane Dembélé - 27 años - Delantero",
                "Olivier Giroud - 37 años - Delantero",
            ],
            'Alemania':[
                "Manuel Neuer - 38 años - Portero",
                "Joshua Kimmich - 29 años - Lateral derecho",
                "Antonio Rüdiger - 31 años - Defensa central",
                "Niklas Süle - 28 años - Defensa central",
                "David Raum - 26 años - Lateral izquierdo",
                "Ilkay Gündogan - 33 años - Centrocampista",
                "Leon Goretzka - 29 años - Centrocampista",
                "Jamal Musiala - 21 años - Centrocampista ofensivo",
                "Thomas Müller - 34 años - Delantero",
                "Kai Havertz - 25 años - Delantero",
                "Serge Gnabry - 28 años - Delantero",
            ],
            'España':[
                "Unai Simón - 27 años - Portero",
                "Dani Carvajal - 32 años - Lateral derecho",
                "Aymeric Laporte - 30 años - Defensa central",
                "Pau Torres - 27 años - Defensa central",
                "Jordi Alba - 35 años - Lateral izquierdo",
                "Rodri Hernández - 27 años - Centrocampista",
                "Gavi Páez - 19 años - Centrocampista",
                "Pedri González - 21 años - Centrocampista",
                "Ferran Torres - 24 años - Delantero",
                "Álvaro Morata - 31 años - Delantero",
                "Mikel Oyarzabal - 27 años - Delantero",
            ],
            'Italia':[
                "Gianluigi Donnarumma - 25 años - Portero",
                "Giovanni Di Lorenzo - 30 años - Lateral derecho",
                "Francesco Acerbi - 36 años - Defensa central",
                "Alessandro Bastoni - 25 años - Defensa central",
                "Leonardo Spinazzola - 31 años - Lateral izquierdo",
                "Jorginho Frello - 32 años - Centrocampista",
                "Nicolo Barella - 27 años - Centrocampista",
                "Marco Verratti - 31 años - Centrocampista",
                "Federico Chiesa - 26 años - Delantero",
                "Ciro Immobile - 34 años - Delantero",
                "Lorenzo Insigne - 33 años - Delantero",
            ],
            'Inglaterra':[
                "Jordan Pickford - 30 años - Portero",
                "Kyle Walker - 34 años - Lateral derecho",
                "John Stones - 30 años - Defensa central",
                "Harry Maguire - 31 años - Defensa central",
                "Luke Shaw - 28 años - Lateral izquierdo",
                "Declan Rice - 25 años - Centrocampista",
                "Jude Bellingham - 20 años - Centrocampista",
                "Mason Mount - 25 años - Centrocampista ofensivo",
                "Harry Kane - 30 años - Delantero",
                "Raheem Sterling - 29 años - Delantero",
                "Marcus Rashford - 26 años - Delantero",
            ],
            'Portugal':[
                "Diogo Costa - 24 años - Portero",
                "João Cancelo - 30 años - Lateral derecho",
                "Rúben Dias - 27 años - Defensa central",
                "Pepe Ferreira - 41 años - Defensa central",
                "Raphael Guerreiro - 30 años - Lateral izquierdo",
                "João Palhinha - 28 años - Centrocampista",
                "Bruno Fernandes - 29 años - Centrocampista",
                "Bernardo Silva - 29 años - Centrocampista ofensivo",
                "João Félix - 24 años - Delantero",
                "Cristiano Ronaldo - 39 años - Delantero",
                "Diogo Jota - 27 años - Delantero",
            ],
            'Paises Bajos':[
                "Andries Noppert - 29 años - Portero",
                "Denzel Dumfries - 28 años - Lateral derecho",
                "Virgil van Dijk - 32 años - Defensa central",
                "Matthijs de Ligt - 24 años - Defensa central",
                "Nathan Aké - 29 años - Lateral izquierdo",
                "Frenkie de Jong - 27 años - Centrocampista",
                "Marten de Roon - 33 años - Centrocampista",
                "Georginio Wijnaldum - 33 años - Centrocampista",
                "Memphis Depay - 30 años - Delantero",
                "Cody Gakpo - 25 años - Delantero",
                "Steven Bergwijn - 26 años - Delanterov",
            ],
            'Belgica':[
                "Thibaut Courtois - 32 años - Portero",
                "Thomas Meunier - 32 años - Lateral derecho",
                "Toby Alderweireld - 35 años - Defensa central", 
                "Jan Vertonghen - 37 años - Defensa central",
                "Timothy Castagne - 28 años - Lateral izquierdo",
                "Youri Tielemans - 27 años - Centrocampista",
                "Kevin De Bruyne - 32 años - Centrocampista",
                "Axel Witsel - 35 años - Centrocampista",
                "Eden Hazard - 33 años - Delantero",
                "Romelu Lukaku - 31 años - Delantero",
                "Dries Mertens - 37 años - Delantero",
            ],
        }

        self.crear_interfaz()
        self.cargar_imagen_inicial()
    
    def cargar_imagen_inicial(self):
        try:
            imagen_original = Image.open("icon.gif")
            imagen_resized = imagen_original.resize((500, 250), Image.LANCZOS)  # Utilizamos LANCZOS para redimensionar
            self.imagen_fondo = ImageTk.PhotoImage(imagen_resized)

            # Mostrar la imagen en un label
            self.label_imagen = tk.Label(self.root, image=self.imagen_fondo)
            self.label_imagen.pack()

        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo de imagen 'icon.gif' no encontrado.")
            self.root.destroy()
        

    def crear_interfaz(self):
        self.menu_principal = tk.Menu(self.root)
        self.root.config(menu=self.menu_principal)

        self.menu_equipos = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Gestión de Equipos", menu=self.menu_equipos)
        self.menu_equipos.add_command(label="Agregar Equipo", command=self.agregar_equipo)

        self.menu_partidos = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Gestión de Partidos", menu=self.menu_partidos)
        self.menu_partidos.add_command(label="Registrar Partido", command=self.registrar_partido)

        self.menu_estadios = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Gestión de Estadios", menu=self.menu_estadios)
        self.menu_estadios.add_command(label="Agregar Estadio", command=self.agregar_estadio)

        self.menu_clasificacion = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Ver Clasificación", menu=self.menu_clasificacion)
        self.menu_clasificacion.add_command(label="Ver Tabla", command=self.ver_clasificacion)

        self.menu_ver_jugadores = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Jugadores", menu=self.menu_ver_jugadores)
        
        # Agregar opciones para cada equipo en el menú de Jugadores
        for equipo in self.equipos:
            self.menu_ver_jugadores.add_command(label=equipo, command=lambda eq=equipo: self.ver_jugadores(eq))

        self.contenido_frame = tk.Frame(self.root, bg="grey")
        self.contenido_frame.pack(fill=tk.BOTH, expand=True)

    def agregar_equipo(self):
        self.limpiar_contenido()
        self.titulo_contenido = tk.Label(self.contenido_frame, text="Agregar Equipo", font=("Arial", 16), pady=10, bg="grey")
        self.titulo_contenido.pack()

        tk.Label(self.contenido_frame, text="Nombre del Equipo:", font=("Arial", 12), bg="grey").pack(pady=5)
        self.nombre_equipo = tk.Entry(self.contenido_frame, font=("Arial", 12))
        self.nombre_equipo.pack(pady=5)

        tk.Button(self.contenido_frame, text="Agregar", command=self.guardar_equipo, bg="red", fg="black").pack(pady=10)

    def guardar_equipo(self):
        nombre = self.nombre_equipo.get().strip()
        if nombre:
            if nombre in self.equipos:
                messagebox.showwarning("Advertencia", "El equipo ya está registrado.")
            else:
                self.equipos[nombre] = {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "Pts": 0}
                messagebox.showinfo("Éxito", f"Equipo '{nombre}' agregado correctamente.")
                self.nombre_equipo.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El nombre del equipo no puede estar vacío.")

    def agregar_estadio(self):
        self.limpiar_contenido()
        self.titulo_contenido = tk.Label(self.contenido_frame, text="Agregar Estadio", font=("Arial", 16), pady=10, bg="grey")
        self.titulo_contenido.pack()

        tk.Label(self.contenido_frame, text="Nombre del Estadio:", font=("Arial", 12), bg="grey").pack(pady=5)
        self.nombre_estadio = tk.Entry(self.contenido_frame, font=("Arial", 12))
        self.nombre_estadio.pack(pady=5)

        tk.Label(self.contenido_frame, text="Capacidad:", font=("Arial", 12), bg="grey").pack(pady=5)
        self.capacidad_estadio = tk.Entry(self.contenido_frame, font=("Arial", 12))
        self.capacidad_estadio.pack(pady=5)

        tk.Button(self.contenido_frame, text="Agregar", command=self.guardar_estadio, bg="red", fg="black").pack(pady=10)

    def guardar_estadio(self):
        nombre = self.nombre_estadio.get().strip()
        capacidad = self.capacidad_estadio.get().strip()
        if nombre and capacidad.isdigit():
            if nombre in self.estadios:
                messagebox.showwarning("Advertencia", "El estadio ya está registrado.")
            else:
                self.estadios[nombre] = {"Capacidad": int(capacidad)}
                messagebox.showinfo("Éxito", f"Estadio '{nombre}' agregado correctamente.")
                self.nombre_estadio.delete(0, tk.END)
                self.capacidad_estadio.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El nombre del estadio no puede estar vacío y la capacidad debe ser un número.")

    def registrar_partido(self):
        self.limpiar_contenido()
        self.titulo_contenido = tk.Label(self.contenido_frame, text="Registrar Partido", font=("Arial", 16), pady=10, bg="grey")
        self.titulo_contenido.pack()

        tk.Label(self.contenido_frame, text="Equipo Local:", font=("Arial", 12), bg="grey").pack(pady=5)
        self.equipo_local = ttk.Combobox(self.contenido_frame, values=list(self.equipos.keys()), font=("Arial", 12))
        self.equipo_local.pack(pady=5)

        tk.Label(self.contenido_frame, text="Goles Local:", font=("Arial", 12), bg="grey").pack(pady=5)
        self.goles_local = tk.Entry(self.contenido_frame, font=("Arial", 12))
        self.goles_local.pack(pady=5)

        tk.Label(self.contenido_frame, text="Equipo Visitante:", font=("Arial", 12), bg="grey").pack(pady=5)
        self.equipo_visitante = ttk.Combobox(self.contenido_frame, values=list(self.equipos.keys()), font=("Arial", 12))
        self.equipo_visitante.pack(pady=5)

        tk.Label(self.contenido_frame, text="Goles Visitante:", font=("Arial", 12), bg="grey").pack(pady=5)
        self.goles_visitante = tk.Entry(self.contenido_frame, font=("Arial", 12))
        self.goles_visitante.pack(pady=5)

        tk.Label(self.contenido_frame, text="Estadio:", font=("Arial", 12), bg="grey").pack(pady=5)
        self.estadio = ttk.Combobox(self.contenido_frame, values=list(self.estadios.keys()), font=("Arial", 12))
        self.estadio.pack(pady=5)

        tk.Button(self.contenido_frame, text="Registrar", command=self.guardar_partido, bg="red", fg="black").pack(pady=10)

    def guardar_partido(self):
        equipo_local = self.equipo_local.get()
        goles_local = self.goles_local.get()
        equipo_visitante = self.equipo_visitante.get()
        goles_visitante = self.goles_visitante.get()
        estadio = self.estadio.get()

        if equipo_local and equipo_visitante and goles_local.isdigit() and goles_visitante.isdigit() and estadio:
            goles_local = int(goles_local)
            goles_visitante = int(goles_visitante)
            self.partidos.append((equipo_local, goles_local, equipo_visitante, goles_visitante, estadio))
            messagebox.showinfo("Éxito", "Partido registrado correctamente.")
            self.actualizar_estadisticas(equipo_local, goles_local, equipo_visitante, goles_visitante)
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos con información válida.")

    def actualizar_estadisticas(self, equipo_local, goles_local, equipo_visitante, goles_visitante):
        self.equipos[equipo_local]["PJ"] += 1
        self.equipos[equipo_visitante]["PJ"] += 1
        self.equipos[equipo_local]["GF"] += goles_local
        self.equipos[equipo_local]["GC"] += goles_visitante
        self.equipos[equipo_visitante]["GF"] += goles_visitante
        self.equipos[equipo_visitante]["GC"] += goles_local

        if goles_local > goles_visitante:
            self.equipos[equipo_local]["G"] += 1
            self.equipos[equipo_visitante]["P"] += 1
            self.equipos[equipo_local]["Pts"] += 3
        elif goles_local < goles_visitante:
            self.equipos[equipo_visitante]["G"] += 1
            self.equipos[equipo_local]["P"] += 1
            self.equipos[equipo_visitante]["Pts"] += 3
        else:
            self.equipos[equipo_local]["E"] += 1
            self.equipos[equipo_visitante]["E"] += 1
            self.equipos[equipo_local]["Pts"] += 1
            self.equipos[equipo_visitante]["Pts"] += 1

    def ver_clasificacion(self):
        self.limpiar_contenido()
        self.titulo_contenido = tk.Label(self.contenido_frame, text="Tabla de Clasificación", font=("Arial", 16), pady=10, bg="grey")
        self.titulo_contenido.pack()

        equipos_ordenados = sorted(self.equipos.items(), key=lambda x: x[1]["Pts"], reverse=True)

        self.frame_clasificacion = tk.Frame(self.contenido_frame, bg="grey")
        self.frame_clasificacion.pack(pady=10)

        columnas = ["Equipo", "PJ", "G", "E", "P", "GF", "GC", "Pts"]
        for i, col in enumerate(columnas):
            label = tk.Label(self.frame_clasificacion, text=col, font=("Arial", 12, "bold"), bg="grey", padx=10, pady=5)
            label.grid(row=0, column=i)

        for i, (equipo, stats) in enumerate(equipos_ordenados, start=1):
            tk.Label(self.frame_clasificacion, text=equipo, font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=0)
            tk.Label(self.frame_clasificacion, text=stats["PJ"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=1)
            tk.Label(self.frame_clasificacion, text=stats["G"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=2)
            tk.Label(self.frame_clasificacion, text=stats["E"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=3)
            tk.Label(self.frame_clasificacion, text=stats["P"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=4)
            tk.Label(self.frame_clasificacion, text=stats["GF"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=5)
            tk.Label(self.frame_clasificacion, text=stats["GC"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=6)
            tk.Label(self.frame_clasificacion, text=stats["Pts"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=7)

    def ver_equipos(self):
        self.limpiar_contenido()
        self.titulo_contenido = tk.Label(self.contenido_frame, text="Equipos", font=("Arial", 16), pady=10, bg="grey")
        self.titulo_contenido.pack()

        self.frame_equipos = tk.Frame(self.contenido_frame, bg="grey")
        self.frame_equipos.pack(pady=10)

        columnas = ["Equipo", "PJ", "G", "E", "P", "GF", "GC", "Pts"]
        for i, col in enumerate(columnas):
            label = tk.Label(self.frame_equipos, text=col, font=("Arial", 12, "bold"), bg="grey", padx=10, pady=5)
            label.grid(row=0, column=i)

        for i, (equipo, stats) in enumerate(self.equipos.items(), start=1):
            tk.Label(self.frame_equipos, text=equipo, font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=0)
            tk.Label(self.frame_equipos, text=stats["PJ"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=1)
            tk.Label(self.frame_equipos, text=stats["G"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=2)
            tk.Label(self.frame_equipos, text=stats["E"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=3)
            tk.Label(self.frame_equipos, text=stats["P"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=4)
            tk.Label(self.frame_equipos, text=stats["GF"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=5)
            tk.Label(self.frame_equipos, text=stats["GC"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=6)
            tk.Label(self.frame_equipos, text=stats["Pts"], font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=7)
    def ver_jugadores(self, equipo):
        self.limpiar_contenido()
        self.titulo_contenido = tk.Label(self.contenido_frame, text=f"Jugadores de {equipo}", font=("Arial", 16), pady=10, bg="grey")
        self.titulo_contenido.pack()

        self.frame_jugadores = tk.Frame(self.contenido_frame, bg="grey")
        self.frame_jugadores.pack(pady=10)

        columnas = ["Nombre", "Edad", "Posición"]
        for i, col in enumerate(columnas):
            label = tk.Label(self.frame_jugadores, text=col, font=("Arial", 12, "bold"), bg="grey", padx=10, pady=5)
            label.grid(row=0, column=i)

        # Obtener la lista de jugadores del equipo seleccionado
        jugadores = self.jugadores_por_equipo.get(equipo, [])

        for i, jugador in enumerate(jugadores, start=1):
            nombre, edad, posicion = jugador.split(" - ")
            tk.Label(self.frame_jugadores, text=nombre, font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=0)
            tk.Label(self.frame_jugadores, text=edad, font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=1)
            tk.Label(self.frame_jugadores, text=posicion, font=("Arial", 12), bg="grey", padx=10, pady=5).grid(row=i, column=2)

    def limpiar_contenido(self):
        for widget in self.contenido_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MundialFutbol(root)
    root.mainloop()
