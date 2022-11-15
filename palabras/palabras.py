import unidecode as ud # pip install unidecode
import random as rn

# Diccionario que tiene listas de palabras agrupadas por su longitud
palabras = { x: [] for x in range(4, 9) }

# Leer el archivo txt que contiene las palabras más comunes en español
# Tomado de: https://github.com/mazyvan/most-common-spanish-words (v5)
with open('palabras/palabras.txt', encoding = 'utf8') as lemario:
    for palabra in lemario:
        # Normalizar palabra. Poner en mayúscula y quitar tildes
        normalizada = ud.unidecode(palabra.strip().upper())
        longitud = len(normalizada)

        # Añadir la palabra a su lista correspondiente dependiendo de su longitud
        if longitud in palabras: palabras[longitud].append(normalizada)

# Conseguir una palabra aleatoria de una longitud dada
def palabraAleatoria(longitud): return palabras[longitud][rn.randint(0,len(palabras[longitud]))]