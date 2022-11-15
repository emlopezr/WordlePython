from clases.partida import Partida

class Juego:
    # Valores predeterminados
    def __init__(self):
        self.partidas = []
        self.partidaActual = None

    # Comprobar si hay una partida en curso
    def checkPartida(self):
        if self.partidaActual == None: return False
        elif not self.partidaActual.estado: return False
        else: return True

    # Jugar una partida por medio del objeto principal
    def jugarPartida(self, dificultad):
        # Si no hay una partida en curso, empezar una
        if self.checkPartida(): return False
        
        partida = Partida(dificultad)
        self.partidas.append(partida)
        self.partidaActual = partida

        return True # Retorna true para avisar a Tkinter

    # Calcular las estadisticas del jugador
    def aciertos(self):
        totales = len(self.partidas)
        aciertos = 0
        
        for partida in self.partidas:
            if partida.ganado == True: aciertos += 1

        fallos = totales - aciertos

        return totales, aciertos, fallos