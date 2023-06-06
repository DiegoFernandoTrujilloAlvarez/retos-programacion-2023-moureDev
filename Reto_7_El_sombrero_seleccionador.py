"""
Crea un programa que simule el comportamiento del sombrero selccionador del
universo mágico de Harry Potter.
- De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
- Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
- En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
  coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
- Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
  Por ejemplo, en Slytherin se premia la ambición y la astucia.

Edit:
Se cambia la prueba a elegir que linea del juego League Of Leguends debería jugar
  
"""

PuntosTop = 0
PuntosJg = 0
PuntosMid = 0
PuntosAdc = 0
PuntosSup = 0


Preguntas = [
    {"Pregunta": "Te gusta ser el máximo daño del equipo?",
     "Respuestas": [{"Si, el máximo daño aunque tenga poca vida": {"Top": 1,"Jg": 2,"Mid": 3, "Adc": 5 , "Sup": 0}},
                    ]
     },
]

print(Preguntas[0])