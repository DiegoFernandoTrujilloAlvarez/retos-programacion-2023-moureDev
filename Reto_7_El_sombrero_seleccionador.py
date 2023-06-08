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
Puntajes = {
    "PuntosTop": 0,
    "PuntosJg": 0,
    "PuntosMid": 0,
    "PuntosAdc": 0,
    "PuntosSup": 0,
}

Preguntas = [
    {
        "Pregunta": "Te gusta ser el máximo daño del equipo?",
        "Respuestas": [
            {
                "Respuesta": "Si, el máximo daño aunque tenga poca vida",
                "Top": 1,
                "Jg": 2,
                "Mid": 3,
                "Adc": 5,
                "Sup": 0,
            },
        ],
    },
]

for pregunta in Preguntas:
    print(pregunta["Pregunta"])
    count = 1
    for respuesta in pregunta["Respuestas"]:
        print(f"{count}. {str(respuesta['Respuesta'])}")
        count += 1
    respuestaUsuario = int(input("Tu respuesta: "))

    Puntajes["PuntosTop"] += pregunta["Respuestas"][respuestaUsuario - 1]["Top"]
    Puntajes["PuntosJg"]  += pregunta["Respuestas"][respuestaUsuario - 1]["Jg"]
    Puntajes["PuntosMid"]  += pregunta["Respuestas"][respuestaUsuario - 1]["Mid"]
    Puntajes["PuntosAdc"]  += pregunta["Respuestas"][respuestaUsuario - 1]["Adc"]
    Puntajes["PuntosSup"]  += pregunta["Respuestas"][respuestaUsuario - 1]["Sup"]


puntajeMaximo = max(Puntajes, key=Puntajes.get)

if puntajeMaximo == "PuntosAdc":
    print("Tu linea que deberias jugar es: ADC")
else:
    print("WTF ESTO NO DEBERIA PASAR")
