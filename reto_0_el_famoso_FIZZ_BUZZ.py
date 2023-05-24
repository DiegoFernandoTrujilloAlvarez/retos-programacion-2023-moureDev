"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

#Se realiza un ciclo que va del 1 al 100 con range
for i in range(1,101):
    #Se revisa la condición si es múltiplo de 3 y de 5
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    #Se revisa la condición si es múltiplo de 3    
    if i % 3 == 0:
        print("fizz")
    #Se revisa la condición si es múltiplo de 5
    elif i % 5 == 0:
        print("buzz")
    #Si no cumplió con ninguna condición se imprime solo el número
    else:
        print(i)