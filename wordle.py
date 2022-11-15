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


def displayIntento(frame, size, palabraUser):   
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

        celda = tk.Label(frame, text = palabraUser[i], width = gridSize, height = 5, bg = colorBg, fg='white', font=('Helvetica', 12))
        celda.grid(row = juego.partidaActual.intento, column = i, padx = 2, pady = 2)

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

        

        btnInput = tk.Button(ventanaPartida, text = 'Intentar', font = ('Helvetica', 12, 'bold'), bg='blue', fg='white',
        command = lambda: displayIntento(frameIntentos, dificultadSeleccionada, inputUser.get()))
        btnInput.pack(pady = 10)

        frameIntentos = tk.Frame(ventanaPartida, width = 400)
        frameIntentos.pack(pady = 10)


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

botonJugar = tk.Button(ventana, text = 'Jugar partida', font = ('Helvetica', 12, 'bold'), bg='blue', fg='white', command = crearPartida)
botonJugar.pack(pady = 10)

textoEstadisticas = tk.Label(ventana, text = 'Estadísticas:', font = ('Helvetica', 16, 'bold'))
textoTotales = tk.Label(ventana, text = f'Partidas totales: {juego.aciertos()[0]}', font = ('Helvetica', 12))
textoAciertos = tk.Label(ventana, text = f'Aciertos: {juego.aciertos()[1]}', font = ('Helvetica', 12))
textoFallos = tk.Label(ventana, text = f'Fallos: {juego.aciertos()[2]}', font = ('Helvetica', 12))
textoEstadisticas.pack(pady = 10)
textoTotales.pack()
textoAciertos.pack()
textoFallos.pack()

ventana.mainloop()