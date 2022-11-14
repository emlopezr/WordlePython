# Wordle - Equipo #1
# Integrantes: 
# - Emmanuel López Rodríguez
# - Maria Paula Duque Muñoz
# - Andrés Felipe Aparicio Mestre

# Se trabaja con Tkinter para la interfaz
import tkinter as tk 
from tkinter import ttk

# Se usa Programación Orientada a Objetos
from clases.juego import Juego
from clases.partida import Partida

# Configuraciones de la ventana de Tkinter

WIDTH = 560
HEIGHT = 672
COLUMNS = 10
GRIDSIZE = WIDTH/COLUMNS

ventana = tk.Tk()
ventana.title('Wordle - Equipo #1')
ventana.geometry(f'{WIDTH}x{HEIGHT}')
ventana.resizable(False, False)

for i in range(12):
    for j in range(10):
        marco = tk.Frame(ventana, highlightbackground="black", highlightthickness=1)
        marco.grid(row=i, column=j)
        marco.config(width=GRIDSIZE, height=GRIDSIZE)


# Grid del Tkinter

# # Elementos gráficos del juego
# titulo = tk.Label(ventana, text = 'Wordle - Equipo #1', font = ('Helvetica', 24, 'bold'))
# titulo.grid(row = 0, column = 0, columnspan = 10, pady = 20)

# dificultad = tk.StringVar()
# selectDificultad = ttk.Combobox(ventana, textvariable = dificultad, font =('Helvetica', 12))
# selectDificultad['values'] = [ f'{i} letras' for i in range(4, 9) ]
# selectDificultad['state'] = 'readonly'
# selectDificultad.grid(row = 1, column = 2, pady = 20)

ventana.mainloop()