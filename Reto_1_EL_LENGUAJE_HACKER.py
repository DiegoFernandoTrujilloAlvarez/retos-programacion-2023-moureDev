"""
Escribe un programa que reciba un texto y transforme lenguaje natural a
"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 se caracteriza por sustituir caracteres alfanuméricos.
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
  con el alfabeto y los números en "leet".
  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""
salir = 'y'

while (salir.lower() == 'y'):

    #Diccionario con relación entre lenguaje natura y lenguaje hacker
    alfabeto = {
        'a':'4',
        'b':'I3',
        'c':'[',
        'd':')',
        'e':'3',
        'f':'|=',
        'g':'&',
        'h':'#',
        'i':'1',
        'j':',_|',
        'k':'>|',
        'l':'1',
        'm':'/\/\\',
        'n':'^/',
        'o':'0',
        'p':'|*',
        'q':'(_,)',
        'r':'I2',
        's':'5',
        't':'7',
        'u':'(_)',
        'v':'\/',
        'w':'\/\/',
        'x':'><',
        'y':'j',
        'z':'2',
        '0':'o',
        '1':'L',
        '2':'R',
        '3':'E',
        '4':'A',
        '5':'S',
        '6':'b',
        '7':'T',
        '8':'B',
        '9':'g',
    }

    #Solicita el texto a cambiar
    texto = input('Por favor introduce tu texto para ser traducido a lenguaje hacker: ')

    #Pasa todo el texto a minusculas
    texto_minuscula = texto.lower()

    nuevo_texto = ''

    #Recorre todo el texto introducido
    for i in texto_minuscula:
        #Si el caracter se encuentra dentro de la lista (alfabeto) realizar el cambio de lenguaje
        if i in alfabeto:
            nuevo_texto += alfabeto[i]
        #Si el caracter no se encuentra dentro de la lista (alfabeto) no lo reemplaza
        else:
            nuevo_texto += i

    #Muestra el resultado
    print('El resultado del texto traducido es: ')
    print(nuevo_texto)

    salir = input('Desea seguir seguir tranformando texto? (y/n): ' )