# Wordle - Equipo #1
# Integrantes: 
# - Emmanuel López Rodríguez
# - Maria Paula Duque Muñoz
# - Andrés Felipe Aparicio Mestre

# Se trabaja con Tkinter para la interfaz
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

# Se usa Programación Orientada a Objetos
from clases.juego import Juego

# Objeto de juego que controlará la aplicación 

juego = Juego()


def displayIntento(frame, btn, size, palabraUser):   
    if len(palabraUser) != size:
        messagebox.showinfo(message=f"Usa una palabra de longitud {size}", title="Palabra no válida")
        return
    
    gridSize = 50//size
    
    palabraUser = palabraUser.upper()
    intento = juego.partidaActual.hacerIntento(palabraUser)

    for i in range(size):
        colorBg = 'gray'

        if intento[i] == '🟩': colorBg = 'lime green'
        elif intento[i] == '🟨': colorBg = 'orange'

        celda = tk.Label(frame, text = palabraUser[i], width = gridSize, height = 5, bg = colorBg, fg='white', font=('Helvetica', 12, 'bold'))
        celda.grid(row = juego.partidaActual.intento, column = i, padx = 2, pady = 2)

    # La partida se acabó, deshabilitar botón y avisar al jugador
    if not juego.partidaActual.estado:
        btn.pack_forget()

        if juego.partidaActual.ganado: messagebox.showinfo(message=f"¡¡Ganaste!!", title="Partida terminada")
        else: messagebox.showinfo(message=f"Perdiste :(", title="Partida terminada")

def crearPartida():
    dificultadSeleccionada = 4
    
    if selectDificultad.get() != '':
        dificultadSeleccionada = int(selectDificultad.get().split()[0])

    if juego.jugarPartida(dificultadSeleccionada):
        ventanaPartida = tk.Toplevel(ventana)
        ventanaPartida.title('Partida | Wordle - Equipo #1')
        ventanaPartida.geometry('600x800')
        ventanaPartida.resizable(False, False)

        textoInput = tk.Label(ventanaPartida, text = 'Escribe la palabra:', font = ('Helvetica', 16, 'bold'))
        inputUser = tk.Entry(ventanaPartida, font =('Helvetica', 12))
        textoInput.pack(pady = 20)
        inputUser.pack(fill='x', padx = 50)

        btnInput = tk.Button(ventanaPartida, text = 'Intentar', font = ('Helvetica', 12, 'bold'), bg='dodger blue', fg='white',
        command = lambda: displayIntento(frameIntentos, btnInput, dificultadSeleccionada, inputUser.get()))
        btnInput.pack(pady = 10)

        frameIntentos = tk.Frame(ventanaPartida, width = 400)
        frameIntentos.pack(pady = 10)

        btnSalir = tk.Button(ventanaPartida, text = 'Terminar partida', font = ('Helvetica', 12, 'bold'), bg='red3', fg='white',
        command = lambda: terminarPartida(ventanaPartida, juego.partidaActual))
        btnSalir.pack(pady = 10)
    else:
        messagebox.showinfo(message=f"Ya hay una partida en curso que no se cerró correctamente. Vuelve a intentar", title="Error")
        juego.partidaActual.estado = False

def terminarPartida(window, partida):
    window.destroy()
    partida.estado = False

def actualizarEstadisticas(totales, aciertos, fallos):
    totales['text'] = f'Partidas totales: {juego.aciertos()[0]}'
    aciertos['text'] = f'Aciertos: {juego.aciertos()[1]}'
    fallos['text'] = f'Fallos: {juego.aciertos()[2]}'


# Configuraciones de la ventana principal de Tkinter

ventana = tk.Tk()
ventana.title('Menú | Wordle - Equipo #1')
ventana.geometry('600x400')
ventana.resizable(False, False)

# Elementos gráficos del juego
titulo = tk.Label(ventana, text = 'Wordle - Equipo #1', font = ('Helvetica', 24, 'bold'))
titulo.pack(pady = 20)

dificultad = tk.StringVar()
textoDificultad = tk.Label(ventana, text = 'Selecciona nivel de dificultad:', font = ('Helvetica', 16, 'bold'))
selectDificultad = ttk.Combobox(ventana, textvariable = dificultad, font =('Helvetica', 12))
selectDificultad['values'] = [ f'{i} letras' for i in range(4, 9) ]
selectDificultad['state'] = 'readonly'
textoDificultad.pack(pady = 10)
selectDificultad.pack()

botonJugar = tk.Button(ventana, text = 'Jugar partida', font = ('Helvetica', 12, 'bold'), bg='dodger blue', fg='white', command = crearPartida)
botonJugar.pack(pady = 10)

textoEstadisticas = tk.Label(ventana, text = 'Estadísticas:', font = ('Helvetica', 16, 'bold'))
textoTotales = tk.Label(ventana, text = f'Partidas totales: {juego.aciertos()[0]}', font = ('Helvetica', 12))
textoAciertos = tk.Label(ventana, text = f'Aciertos: {juego.aciertos()[1]}', font = ('Helvetica', 12))
textoFallos = tk.Label(ventana, text = f'Fallos: {juego.aciertos()[2]}', font = ('Helvetica', 12))
textoEstadisticas.pack(pady = 10)
textoTotales.pack()
textoAciertos.pack()
textoFallos.pack()

botonActualizar = tk.Button(ventana, text = 'Actualizar estadísticas', font = ('Helvetica', 12, 'bold'),
bg='green3', fg='white', command = lambda: actualizarEstadisticas(textoTotales, textoAciertos, textoFallos))
botonActualizar.pack(pady = 10)

ventana.mainloop()