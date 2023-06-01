"""
Crea un programa que calcule quien gana más partidas al piedra,
papel, tijera, lagarto, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
  "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
- Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""

puntosJugador1 = 0
puntosJugador2 = 0

#jugadas  = [("piedra","tijera"),("tijera","piedra"),("papel","tijera")]
jugadas  = [("tijera","tijera"),("piedra","piedra")]

for jugada in jugadas:

    if jugada[0] == "tijera" and jugada[1] == "papel":
        puntosJugador1 += 1
    elif jugada[0] == "tijera" and jugada[1] == "lagarto":
        puntosJugador1 += 1
    elif jugada[0] == "papel" and jugada[1] == "tijera":
        puntosJugador2 += 1
    elif jugada[0] == "lagarto" and jugada[1] == "tijera":
        puntosJugador2 += 1
    elif jugada[0] == "papel" and jugada[1] == "spock":
        puntosJugador1 += 1
    elif jugada[0] == "papel" and jugada[1] == "piedra":
        puntosJugador1 += 1
    elif jugada[0] == "spock" and jugada[1] == "papel":
        puntosJugador2 += 1
    elif jugada[0] == "piedra" and jugada[1] == "papel":
        puntosJugador2 += 1
    elif jugada[0] == "piedra" and jugada[1] == "tijera":
        puntosJugador1 += 1
    elif jugada[0] == "piedra" and jugada[1] == "lagarto":
        puntosJugador1 += 1
    elif jugada[0] == "tijera" and jugada[1] == "piedra":
        puntosJugador2 += 1
    elif jugada[0] == "lagarto" and jugada[1] == "piedra":
        puntosJugador2 += 1
    elif jugada[0] == "lagarto" and jugada[1] == "papel":
        puntosJugador1 += 1
    elif jugada[0] == "lagarto" and jugada[1] == "spock":
        puntosJugador1 += 1
    elif jugada[0] == "papel" and jugada[1] == "lagarto":
        puntosJugador2 += 1
    elif jugada[0] == "spock" and jugada[1] == "lagarto":
        puntosJugador2 += 1
    elif jugada[0] == "spock" and jugada[1] == "tijera":
        puntosJugador1 += 1
    elif jugada[0] == "spock" and jugada[1] == "piedra":
        puntosJugador1 += 1
    elif jugada[0] == "tijera" and jugada[1] == "spock":
        puntosJugador2 += 1
    elif jugada[0] == "piedra" and jugada[1] == "spock":
        puntosJugador2 += 1


print(puntosJugador1)
print(puntosJugador2)
if puntosJugador1 > puntosJugador2:
    print("Player 1")
elif puntosJugador2 > puntosJugador1:
    print("Player 2")
else:
    print("Tie")