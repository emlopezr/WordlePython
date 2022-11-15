from palabras.getPalabras import palabraAleatoria # Sacar palabras aleatorias del lemario

class Partida:
    def __init__(self, dificultad):
        # Generar palabra y separar sus carácteres para la lógica
        self.palabraCorrecta = [ i for i in palabraAleatoria(dificultad) ]

        print(''.join(self.palabraCorrecta))

        # Parámetros predeterminados de la partida
        self.dificultad = dificultad
        self.ganado = False
        self.estado = True
        self.intento = 0

        # Guardar los intentos realizados en la partida
        self.resultados = {}

    def hacerIntento(self, palabraUser):
        # Solo jugar si la partida está activa
        if not self.estado: return

        # Separar los carácteres de la palabra para la lógica
        palabraUser = [ i for i in palabraUser ]

        # Lógica del juego (Los aciertos se guardan en esta lista)
        resultadoIntento = []

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

        # Guardar el resultado del intento
        self.resultados[self.intento] = (''.join(palabraUser), ''.join(resultadoIntento))

        # Verificar si se acertó la palabra (Toda la palabra deben de ser 🟩)
        if ''.join(resultadoIntento) == '🟩'*self.dificultad:
            self.ganado = True
            self.estado = False

        # Restar intento, si ya se acabaron los intentos, acabar la partida
        self.intento += 1

        if self.intento == 6: self.estado = False

        return resultadoIntento