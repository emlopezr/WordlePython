from palabras.palabras import palabraAleatoria # Sacar palabras aleatorias del lemario

class Partida:
    def __init__(self, dificultad):
        # Generar palabra y separar sus carácteres para la lógica
        self.palabraCorrecta = palabraAleatoria(dificultad)

        # Parámetros predeterminados de la partida
        self.dificultad = dificultad
        self.ganado = False
        self.estado = True # True: En curso, False: Acabada
        self.intento = 0 # Intentos realizados hasta ahora (Max 6)

    # Lógica principal del juego
    def hacerIntento(self, palabraUser):
        # Solo jugar si la partida está activa
        if not self.estado: return

        # Separar los carácteres de la palabra para la lógica
        palabraUser = [ i for i in palabraUser ]

        # Lógica del juego (Los aciertos se guardan en esta lista)
        resultadoIntento = ''

        # Para las pistas en amarillo, contar las pistas faltantes para esa letra en específico
        pistasFaltantes = { i: min(self.palabraCorrecta.count(i), palabraUser.count(i)) for i in set(self.palabraCorrecta) }

        # Recorrer la palabra suministrada por el usuario
        for i in range(len(palabraUser)):
            # Poner la letra en una variable para trabajar más comodamente
            letra = palabraUser[i]

            # La letra no está en la palabra
            if letra not in self.palabraCorrecta: resultadoIntento += '⬛'
            
            # La letra está en la posición correcta
            elif letra == self.palabraCorrecta[i]:
                resultadoIntento += '🟩'
                pistasFaltantes[letra] -= 1

            # La letra está en la palabra, pero está en la posición incorrecta
            else:  resultadoIntento += '⬛'

        # Rellenar las pistas en amarillo faltantes
        for i in range(len(palabraUser)):
            # Poner la letra en una variable para trabajar más comodamente
            letra = palabraUser[i]

            # Se mete en un trycatch ya que la letra puede no estar en el diccionario (KeyError)
            try:
                # Reemplazar el ⬛ original por un 🟨 cuando sea necesario
                if pistasFaltantes[letra] > 0 and resultadoIntento[i] != '🟩':
                    resultadoIntento = resultadoIntento[:i] + '🟨' + resultadoIntento[i+1:]
                    pistasFaltantes[letra] -= 1
            except: continue

        # Verificar si se acertó la palabra (Todo el resultado debe de ser 🟩)
        if resultadoIntento == '🟩'*self.dificultad:
            # Dar por terminada la partida
            self.ganado = True
            self.estado = False

        # Sumar intento, y si ya se acabaron los intentos, finalizar la partida
        self.intento += 1
        if self.intento == 6: self.estado = False

        # Retornar resultado para mostralo en pantalla
        return resultadoIntento