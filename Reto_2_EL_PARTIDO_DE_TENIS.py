"""
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
  15 - Love
  30 - Love
  30 - 15
  30 - 30
  40 - 30
  Deuce
  Ventaja P1
  Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.   
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""

#Lista de puntos posibles
marcadores = ["love","15", "30", "40"]


#Secuencias de puntajes de partido
secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
#secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

#Cuenta cuantos puntos tiene cada jugador
total1 = secuencia.count("P1")
total2 = secuencia.count("P2")

#Verifica que toda la lista tenga valores validos ("P1" o "P2")
for i in secuencia:
    if i != "P1" and i != "P2":
        raise ValueError('La secuencia tiene errores ya que tiene valores diferentes a "P1" o "P2"')

#Verifica que los puntajes de los jugadores sean posibles
#Si ambos jugadores tienen más de 3 puntos y la diferencia entre ellos es mayor o igual a 3 no debería ser posible
if (total1 > 3 or total2 > 3) and abs(total1 - total2) >= 3:
   raise ValueError('Secuencia erronea. Uno de los jugadores tiene más puntos de los posibles')

#variables que contrala los puntos de los jugadores
puntosP1 = 0
puntosP2 = 0

#recorre la lista de puntos
for i in secuencia:
    #suma un punto al jugadore correspondiente
    if i == "P1":
        puntosP1 += 1
    else:
        puntosP2 += 1

    #Verifica si uno de los jugadores ha ganado
    if (puntosP1 > 3 or puntosP2 > 3) and abs(puntosP1 - puntosP2) >= 2:
      if puntosP1 > puntosP2:
        print("Ha ganado el jugador P1")
      else:
        print("Ha ganado el jugador P2")
    #Verifica si hay un empate entre los jugadores
    elif (puntosP1 >= 3 or puntosP2 >= 3) and puntosP1 == puntosP2:
      print("Deuce")
    #Verifica cual de los jugares tiene ventaja
    elif (puntosP1 > 3 or puntosP2 > 3):
      if puntosP1 > puntosP2:
        print("Ventaja P1")
      else:
        print("Ventaja P2")
    #De lo contrario muestra los puntos correspondiente de cada jugador
    else:
      print(f"{marcadores[puntosP1]} - {marcadores[puntosP2]}")
    
