"Unidad 4 - Ary Toro"
import random
import tkinter as tk
from tkinter import *
from claseObjectEncoder import ObjectEncoder
from gestor_jugadores import GestorJugadores
from claseJugador import Jugador
from datetime import datetime

class JuegoColores():
    def __init__(self):
        self.__ventana = Tk() # Aqui instancio la ventana desde Tk
        self.__ventana.title("Ary Colores")
        self.__ventana.resizable(0,0) # Hago que no pueda ampliar/maximizar la ventana
        self.__ventana.withdraw()  # Oculto la ventana principal inicialmente

        self.__secuencia = []  # Secuencia generada al azar que el usuario deberá marcar
        self.__usuario_secuencia = []  # Secuencia presionada por el jugador
        self.__colores = ["rojo", "verde", "azul", "amarillo"] # Los colores que puede tomar la secuencia

        self.__boton_amarillo=None
        self.__boton_azul=None
        self.__boton_rojo=None
        self.__boton_verde=None
        self.__puntaje_label=None
        self.__label_mensaje=None

        self.__puntaje = 0
        self.__nombre_jugador = ""

        self.__jsonF=ObjectEncoder()
        self.__gestor_jugadores=GestorJugadores()
        diccionario= self.__jsonF.leerJSONArchivo('pysimonpuntajes.json')
        self.__gestor_jugadores= self.__jsonF.decodificarDiccionario(diccionario)

        self.ingreso_jugador()
        self.__ventana.mainloop()

    def ingreso_jugador(self):
        self.__ventana_ingreso_jugador = tk.Toplevel(self.__ventana)
        self.__ventana_ingreso_jugador.title("Nombre del Jugador")

        tk.Label(self.__ventana_ingreso_jugador, text="Datos del Jugador ").grid(row=0, column=0)
        tk.Label(self.__ventana_ingreso_jugador, text="Jugador: ").grid(row=1, column=0)
        self.__nombre_ingresado = tk.Entry(self.__ventana_ingreso_jugador)
        self.__nombre_ingresado.grid(row=1, column=1, columnspan=1)
        self.__nombre_ingresado.focus()
        
        tk.Button(self.__ventana_ingreso_jugador, text="Iniciar Juego", command=self.iniciar_juego).grid(row=2, column=0, columnspan=2)#Aqui llamo al iniciar juego
        self.__ventana_ingreso_jugador.grab_set()  # Hace que la ventana de nombre tenga el foco

    def iniciar_juego(self):
        self.__nombre_jugador = self.__nombre_ingresado.get()
        self.__ventana_ingreso_jugador.destroy()
        self.__ventana.deiconify()  # Muestra la ventana principal

        # Creo el menú en la parte superior de la ventana con los puntajes
        self.crear_menu()

        # Creo los botones y los label de puntaje de la ventana del juego
        self.crear_botones()

        self.siguiente_ronda()

    def crear_botones(self):
        # Creo una etiqueta para mostrar el nombre del jugador y el puntaje
        self.__puntaje_label = tk.Label(self.__ventana, text=f"{self.__nombre_jugador}                      {self.__puntaje}")
        self.__puntaje_label.grid(row=0, column=0, columnspan=2,sticky="ew")

        # Creo botones para cada color
        self.__boton_verde = tk.Canvas(self.__ventana, bg="#008081", width=150, height=200)
        self.__boton_verde.grid(row=1, column=0, sticky="nsew")

        self.__boton_rojo = tk.Canvas(self.__ventana, bg="#fe0000", width=150, height=200)
        self.__boton_rojo.grid(row=1, column=1, sticky="nsew")

        self.__boton_amarillo = tk.Canvas(self.__ventana, bg="#ffff01", width=150, height=200)
        self.__boton_amarillo.grid(row=2, column=0, sticky="nsew")

        self.__boton_azul = tk.Canvas(self.__ventana, bg="#0080ff", width=150, height=200)
        self.__boton_azul.grid(row=2, column=1, sticky="nsew")

        # Creo una etiqueta para mostrar el estado del juego
        self.__label_mensaje = tk.Label(self.__ventana, text="Mira la secuencia", font=("Arial", 16))
        self.__label_mensaje.grid(row=3, column=0, columnspan=2)


    def crear_menu(self):
        # Crea el menú en la parte superior de la ventana
        barra_menu = tk.Menu(self.__ventana)

        # Crea el menú de opciones
        opciones_menu = tk.Menu(barra_menu, tearoff=0)
        opciones_menu.add_command(label="Ver puntajes", command=self.mostrar_puntajes)
        opciones_menu.add_command(label="Salir", command=self.__ventana.destroy)

        barra_menu.add_cascade(label="Opciones", menu=opciones_menu)
        self.__ventana.config(menu=barra_menu)

    def mostrar_puntajes(self):
        # Creo una ventana modal para mostrar los puntajes
        ventana_puntajes = tk.Toplevel(self.__ventana)
        ventana_puntajes.title("Puntajes")

        # Creo encabezados de la tabla
        tk.Label(ventana_puntajes, text="Jugador", font=("Arial", 16, "bold")).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(ventana_puntajes, text="Fecha", font=("Arial", 16, "bold")).grid(row=0, column=1, padx=10, pady=10)
        tk.Label(ventana_puntajes, text="Hora", font=("Arial", 16, "bold")).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(ventana_puntajes, text="Puntaje", font=("Arial", 16, "bold")).grid(row=0, column=3, padx=10, pady=10)

        # Itero sobre los jugadores en self.__gestorJugadores y los muestra en la tabla
        self.__gestor_jugadores.ordenar_jugadores()
        for i in range(self.__gestor_jugadores.get_cantidad_jugadores()):
            jugador=self.__gestor_jugadores.get_jugador(i)
            tk.Label(ventana_puntajes, text=jugador.get_nombre()).grid(row=i+1, column=0, padx=10, pady=5)
            tk.Label(ventana_puntajes, text=jugador.get_fecha()).grid(row=i+1, column=1, padx=10, pady=5)
            tk.Label(ventana_puntajes, text=jugador.get_hora()).grid(row=i+1, column=2, padx=10, pady=5)
            tk.Label(ventana_puntajes, text=jugador.get_puntaje()).grid(row=i+1, column=3, padx=10, pady=5)

        # Botón para cerrar la ventana de puntajes
        tk.Button(ventana_puntajes, text="Cerrar", command=self.__ventana.destroy).grid(row=self.__gestor_jugadores.get_cantidad_jugadores() + 1, column=0, columnspan=4, pady=20)

    def siguiente_ronda(self):
        # Prepara la siguiente ronda del juego
        self.__usuario_secuencia = []
        self.__secuencia.append(random.choice(self.__colores))
        self.__label_mensaje.config(text="Mira la secuencia!")
        self.desactivar_botones()  # Deshabilita los botones durante la secuencia
        self.__ventana.after(500, self.iniciar_secuencia) 

    def iniciar_secuencia(self):
        # Muestra la secuencia de colores al usuario
        for i, color in enumerate(self.__secuencia): #enumerate me devuelve el indice y el color de la secuencia de colores generada
            self.__ventana.after(1000 * i, self.iluminar_boton, color) #cada 1000 segundos (1000 * i) se mostrara el siguiente color de la lista generada
        self.__ventana.after(1000 * len(self.__secuencia), self.activar_botones)# Ya terminada de mostrarse toda la secuencia(1000 * len(secuencia)), se rehabilitan los botones

    def iluminar_boton(self, color):
        # Cambia el color del boton a presionar a blanco
        boton = self.obtener_boton_por_color(color)
        color_original = boton.cget("bg")#Guardo el color del background del boton antes de iluminarlo
        boton.config(bg="white") #Hago que la boton cambie de color a blanco
        self.__ventana.after(500, lambda: boton.config(bg=color_original))# Vuelvo a establecer el background al color original

    def obtener_boton_por_color(self, color):
        # Devuelve el boton correspondiente al color dado
        if color == "rojo":
            return self.__boton_rojo
        elif color == "verde":
            return self.__boton_verde
        elif color == "azul":
            return self.__boton_azul
        elif color == "amarillo":
            return self.__boton_amarillo

    def activar_botones(self):
        # Habilita las acciones de los botones con bind para que el usuario pueda hacer click
        self.__label_mensaje.config(text="Tu turno!")
        self.__boton_rojo.bind("<Button-1>", self.rojo_click)
        self.__boton_verde.bind("<Button-1>", self.verde_click)
        self.__boton_azul.bind("<Button-1>", self.azul_click)
        self.__boton_amarillo.bind("<Button-1>", self.amarillo_click)

    def desactivar_botones(self):
        # Deshabilita los botones para que el usuario no pueda hacer click
        self.__boton_rojo.unbind("<Button-1>")
        self.__boton_verde.unbind("<Button-1>")
        self.__boton_azul.unbind("<Button-1>")
        self.__boton_amarillo.unbind("<Button-1>")

    def rojo_click(self, event):
        self.usuario_click("rojo")

    def verde_click(self, event):
        self.usuario_click("verde")

    def azul_click(self, event):
        self.usuario_click("azul")

    def amarillo_click(self, event):
        self.usuario_click("amarillo")

    def usuario_click(self, color):
        # Maneja el clic del usuario en un boton de color
        self.__usuario_secuencia.append(color)
        self.iluminar_boton(color)
        if self.__usuario_secuencia == self.__secuencia[:len(self.__usuario_secuencia)]:#Hago un corte en la secuencia generada, que va desde 0 hasta la longitud de la longitud de la secuencia apretada por el usuario
            if len(self.__usuario_secuencia) == len(self.__secuencia): #Si son iguales:
                self.__puntaje+=1
                self.__puntaje_label.config(text=f"{self.__nombre_jugador}                      {self.__puntaje}")
                self.__label_mensaje.config(text="Correcto! Siguiente ronda...")
                self.__ventana.after(1000, self.siguiente_ronda)
        else: #Si no son iguales
            self.desactivar_botones()  # Deshabilita los botones durante la secuencia
            fechahora=datetime.now()
            fecha= fechahora.strftime("%d/%m/%Y")
            hora= fechahora.strftime("%H:%M:%S")
            self.__gestor_jugadores.agregarJugador(Jugador(Nombre=self.__nombre_jugador,Puntaje=self.__puntaje,Fecha=fecha,Hora=hora))
            d= self.__gestor_jugadores.toJSON()
            self.__jsonF.guardarJSONArchivo(d,'pysimonpuntajes.json')
            self.__label_mensaje.config(text="Fallaste. Se termino la partida")
            self.game_over()

    def game_over(self):
        # Muestra una ventana modal con el nombre del jugador
        ventana_game_over = tk.Toplevel(self.__ventana)
        ventana_game_over.title("Fin del Juego")

        tk.Label(ventana_game_over, text="GAME OVER", font=("Arial", 16)).grid(row=0, column=0,columnspan=3, padx=10, pady=10)
        tk.Label(ventana_game_over, text=f"Puntaje obtenido: {self.__puntaje}").grid(row=1, column=0,columnspan=3, padx=10, pady=10)

        tk.Button(ventana_game_over, text="Cerrar",command=self.__ventana.destroy).grid(row=2, column=0,columnspan=3, padx=10, pady=10)
if __name__ == "__main__":
    app = JuegoColores()
