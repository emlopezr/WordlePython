from clases.partida import Partida

class Juego:
    def __init__(self):
        self.partidas = []
        self.partidaActual = None

    def jugarPartida(self, dificultad):
        partida = Partida(dificultad)
        self.partidas.append(partida)
        self.partidaActual = partida

    def aciertos(self):
        totales = len(self.partidas)
        aciertos = 0
        
        for partida in self.partidas:
            if partida.ganado == True: aciertos += 1

        fallos = totales - aciertos

        return aciertos, fallos