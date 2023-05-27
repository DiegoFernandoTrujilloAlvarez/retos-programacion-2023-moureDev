"""
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
 """

import random
import string


longitud = int(input('Digite la longitud de la contraseña (entre 8 y 16): '))

mayusculas = input('Desea que tenga letras mayúsculas (y/n): ')
mayusculas = mayusculas.lower()

numeros = input('Desea que tenga números (y/n): ')
numeros = numeros.lower()

simbolos = input('Desea que tenga símbolos (y/n): ')
simbolos = simbolos.lower()


caracteres = []

caracteres += list(string.ascii_lowercase)
if numeros == 'y':
    caracteres += list(string.digits)
if mayusculas == 'y':
    caracteres += list(string.ascii_uppercase)
if simbolos == 'y':
    caracteres += list(string.punctuation)

contrasena = "".join(random.choices(caracteres, k=longitud))

print(f"Su contraseña es: {contrasena}")



