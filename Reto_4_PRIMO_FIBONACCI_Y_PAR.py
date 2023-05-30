"""
Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
from math import sqrt

def espar(numero):
    if numero%2 == 0:
        return True
    return False

def esprimo(numero):
    if numero == 1:
        return False
    
    for n in range(2, numero+1):
        if (numero/n) % 2 == 0:
            return False
        
    return True

def esfibonacci(numero):
    cuadrado_positivo = 5 * pow(numero, 2) + 4
    cuadrado_negativo =  5 * pow(numero, 2) - 4

    if (int(sqrt(cuadrado_positivo)) * int(sqrt(cuadrado_positivo))) == cuadrado_positivo:
        return True
    elif (int(sqrt(cuadrado_negativo)) * int(sqrt(cuadrado_negativo))) == cuadrado_negativo:
        return True
    else:
        return False

numero = int(input('Por favor ingrese un número: '))

espar = espar(numero)
esprimo = esprimo(numero)
esfibonacci = esfibonacci(numero)

result = 'es primo, es fibonacci y es impar'

if not esprimo:
    primo = 'no es primo'
else:
    primo = 'es primo'
if not esfibonacci:
    fibonacci = 'no es fibonacci'
else:
    fibonacci = 'fibonacci'
if not espar:
    par = 'es impar'
else:
    par = 'es par'

result = f'{numero} {primo}, {fibonacci} y {par}'

print(espar)
print(esprimo)
print(esfibonacci)
print(result)


