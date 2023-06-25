import curses
import juego
COLOR = None

    
def inicio(stdscr):
    global COLOR
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    COLOR = curses.color_pair(1)
    
    stdscr.clear()
    stdscr.addstr(10, 10, "welcome", COLOR | curses.A_BOLD |curses.A_UNDERLINE)
    stdscr.addstr(13, 15, "Press any key to continue", curses.A_UNDERLINE)
    stdscr.getch()

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "========MISTER MIX========\n")

        stdscr.addstr("1. Jugar\n")
        stdscr.addstr("2. Ajustes\n")
        stdscr.addstr("3. Salir\n")

        stdscr.refresh()

        opcion = stdscr.getch() - ord('0')

        if opcion == 1:
            juego.Play(stdscr)

        if opcion == 2:
            ajustes(stdscr)

        if opcion == 3:
            break

def loss(stdscr):
    global COLOR 
    while True:
        stdscr.clear()
        
        stdscr.addstr(0,10,"\n======== PERDISTE ========\n", COLOR | curses.A_BOLD |curses.A_UNDERLINE)

        stdscr.addstr(2,0,"1. Intentar De Nuevo\n")
        stdscr.addstr(3,0,"2. Menu Principal\n")
        stdscr.addstr(4,0,"3. Salir\n")

        stdscr.refresh()

        opcion = stdscr.getch() - ord('0')

        if opcion == 1:
            juego.Play(stdscr)

        if opcion == 2:
            inicio(stdscr)

        if opcion == 3:
            break

def ajustes(stdscr):
    global vidas, damage, time

    
    while True:
        stdscr.clear()
        stdscr.addstr("\n======== AJUSTES ========\n")

        stdscr.addstr("1. vidas\n")
        stdscr.addstr("2. Damage\n")
        stdscr.addstr("3. timer\n")
        stdscr.addstr("4. atras\n")

        stdscr.refresh()

        opcion = stdscr.getch() - ord('0')

        if opcion == 1:
            stdscr.addstr(10, 0, "Numero de vidas: ")
            stdscr.refresh()
            curses.echo()  # Habilitar el eco de caracteres
            vidas = int(stdscr.getstr().decode())
            curses.noecho()  # Deshabilitar el eco de caracteres

        if opcion == 2:
            stdscr.addstr(10, 0, "Numero de daño: ")
            stdscr.refresh()
            curses.echo()  # Habilitar el eco de caracteres
            damage = int(stdscr.getstr().decode())
            curses.noecho()  # Deshabilitar el eco de caracteres

        if opcion == 3:
            stdscr.addstr(10, 0, "Numero de tiempo: ")
            stdscr.refresh()
            curses.echo()  # Habilitar el eco de caracteres
            time = int(stdscr.getstr().decode())
            curses.noecho()  # Deshabilitar el eco de caracteres

        if opcion == 4:
            break

curses.wrapper(inicio)