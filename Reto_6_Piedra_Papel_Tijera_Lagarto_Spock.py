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

jugadas  = [("piedra","tijera"),("tijera","piedra"),("papel","tijera")]
#jugadas  = [("tijera","tijera"),("piedra","piedra")]

ganador = {
    "tijera": ["papel","lagarto"],
    "piedra": ["tijera","lagarto"],
    "papel": ["spock","piedra"],
    "lagarto": ["piedra","papel"],
    "spock": ["tijera","piedra"]
}

for jugada in jugadas:

    if jugada[0] in ganador[jugada[1]]:
        puntosJugador2 += 1
    elif jugada[1] in ganador[jugada[0]]:
        puntosJugador1 += 1

if puntosJugador1 > puntosJugador2:
    print("Player 1")
elif puntosJugador2 > puntosJugador1:
    print("Player 2")
else:
    print("Tie")