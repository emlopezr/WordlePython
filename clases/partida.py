from palabras.palabras import palabraAleatoria # Sacar palabras aleatorias del lemario

class Partida:
    def __init__(self, dificultad):
        # Generar palabra y separar sus carácteres para la lógica
        self.palabraCorrecta = [ i for i in palabraAleatoria(dificultad) ]

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
        resultadoIntento = []

        # Recorrer la palabra suministrada por el usuario
        for i in range(len(palabraUser)):

            # La letra no está en la palabra
            if palabraUser[i] not in self.palabraCorrecta: resultadoIntento.append('⬛')
            
            # La letra está en la posición correcta
            elif palabraUser[i] == self.palabraCorrecta[i]: resultadoIntento.append('🟩')

            # La letra está en la palabra, pero está en la posición incorrecta
            else: 
                repeticionesUser = palabraUser.count(palabraUser[i])
                repeticionesCorrecta = self.palabraCorrecta.count(palabraUser[i])
                
                # La letra efectivamente está en la posición incorrecta
                if repeticionesUser <= repeticionesCorrecta: resultadoIntento.append('🟨')
                
                # Esta letra sobra (El usuario indicó la letra más veces de las que debería)
                else: resultadoIntento.append('⬛')

        # Verificar si se acertó la palabra (Todo el resultado debe de ser 🟩)
        if ''.join(resultadoIntento) == '🟩'*self.dificultad:
            # Dar por terminada la partida
            self.ganado = True
            self.estado = False

        # Sumar intento, y si ya se acabaron los intentos, finalizar la partida
        self.intento += 1
        if self.intento == 6: self.estado = False

        # Retornar resultado para mostralo en pantalla
        return resultadoIntento