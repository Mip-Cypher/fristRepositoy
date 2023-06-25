import os
import time as tm
import random 
import threading
import curses
import menu

diccionario_palabras = {
    'palabras_1': ['Gato', 'Perro', 'Casa', 'Mesa', 'Sol', 'Coche', 'Libro', 'Juego', 'Pelota', 'Árbol', 'Manzana', 'Niño', 'Feliz', 'Rápido', 'Azul'],
    'palabras_2': ['Elefante', 'Tigre', 'Hogar', 'Silla', 'Estrella', 'Automóvil', 'Biblioteca', 'Deporte', 'Baloncesto', 'Elefante', 'Papaya', 'Familia', 'Alegre', 'Veloz', 'Celeste'],
    'palabras_3': ['Computadora', 'Televisión', 'Apartamento', 'Escritorio', 'Constelación', 'Helicóptero', 'Diccionario', 'Aventura', 'Extraterrestre', 'Computadora', 'Sandía', 'Amistad', 'Exitoso', 'Rápidamente', 'Violeta'],
    'palabras_4': ['Mariposa', 'Cocodrilo', 'Residencia', 'Comedor', 'Galaxia', 'Motocicleta', 'Enciclopedia', 'Competencia', 'Natación', 'Mariposa', 'Naranja', 'Amoroso', 'Triunfante', 'Habilidosamente', 'Esmeralda'],
    'palabras_5': ['Hipopótamo', 'Rinoceronte', 'Arquitectura', 'Entretenimiento', 'Universo', 'Paracaidismo', 'Extraordinario', 'Superficialmente', 'Voleibol', 'Hipopótamo', 'Plátano', 'Maravilloso', 'Exitosamente', 'Amarillo']
}
vidas = 5
damage = 1
time = 120

puntos = 0 
acierto = 0

def agregar_punto():
    global puntos
    puntos = puntos + acierto

def restar_vida():
    global vidas
    vidas = vidas - damage
    
def cuenta_regresiva(stdscr, tiempo):
    for i in range(tiempo, 0, -1):
        stdscr.addstr(0, 0, "====================================")
        stdscr.addstr(1, 0, f"{i}\tVidas: {vidas}\tPuntos: {puntos}")
        stdscr.addstr(2, 0, "====================================")
        stdscr.refresh()
        tm.sleep(1)

        if vidas == 0 or puntos == 50:
            break
        
def mr(stdscr):
    curses.curs_set(0)  # Oculta el cursor
    curses.cbreak()
    
    tiempo_juego = 120
    thread = threading.Thread(target=cuenta_regresiva, args=(stdscr, tiempo_juego))
    
    
    thread.start()
    while True:
    
        stdscr.keypad(True)
        palabra = random.choice(diccionario_palabras['palabras_1'])
        stdscr.clear()
        stdscr.addstr(4, 0, f"Palabra: {palabra}")
        stdscr.refresh()
        respuesta = stdscr.getstr().decode('utf-8')  # Lee la entrada como una cadena
        
        if respuesta == palabra:
            stdscr.addstr(6, 0, "Acertada")
            stdscr.refresh()
            agregar_punto()
        else:
            stdscr.addstr(6, 0, "Error")
            stdscr.refresh()
            restar_vida()

        if puntos == 10 or vidas == 0:
            stdscr.addstr(8, 0, "Game Over")
            stdscr.refresh()
            curses.wrapper(menu.loss)


        tm.sleep(1)

def Play(stdscr):  # Función adicional para ejecutar el juego
    curses.wrapper(mr)  # Ejecuta la función mr del juego
    
#curses.wrapper(mr) #ejecucion de pruebas