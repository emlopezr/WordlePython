# pip install unidecode
import unidecode as ud

# Diccionario que tiene conjuntos de palabras de igual longitud
palabras = { x: set() for x in range(4, 9) }

# Leer el archivo txt que contiene las palabras más comunes en español
# Tomado de: https://github.com/mazyvan/most-common-spanish-words
with open('lemario.txt', encoding = 'utf8') as lemario:
    for palabra in lemario:
        # Normalizar palabra. Poner en minúscula y quitar tildes
        normalizada = ud.unidecode(palabra.strip().lower())
        longitud = len(normalizada)

        # Añadir la palabra a su conjunto correspondiente
        if longitud in palabras: palabras[longitud].add(normalizada)