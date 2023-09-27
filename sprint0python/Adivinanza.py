import random
# 1.-Añade un archivo de código Python llamado adivinanza.py. Este
# programa debe imprimir una adivinanza con tres opciones (a, b, c) para que el
# usuario pueda responder. Luego, el programa debe verificar si la respuesta del
# usuario es correcta o incorrecta.
# 2.- Amplia adivinanza.py para incluir tres adivinanzas en total. Al final del juego,
# imprime la puntuación del usuario. Cada adivinanza correcta suma 10 puntos y
# cada una incorrecta resta 5 puntos.
# 6.-Modifica adivinanza.py para que, en lugar de hacer las tres adivinanzas en orden,
# elija aleatoriamente dos de las tres adivinanzas para hacer al usuario. Asegúrate de
# que no se repitan las adivinanzas.
 
puntuacion = 0

adivinanzas = {
    1: "Adivina adivinanza...¿Qué sube pero nunca baja? ",
    2: "Adivina adivinanza...¿Qué tiene el rey en la panza? ",
    3: "En este banco hay un padre y un hijo, el padre se llama Juan, el nombre del hijo, ya te lo he dicho. ¿Cómo se llama el hijo? "
}
respuestas = {
    1: "a.- Una escalera.   b.- Un ascensor.    c.- La bolsa",
    2: "a.- Yougures.       b.- Jamón.          c.- El ombligo.",
    3: "a.- Esteban.        b.- Juan.           c.- No tiene nombre"
}
respuestasCorrectas = {1: "a", 2: "c", 3: "a"}
#Con esto hemos creado los diccionarios

# print("Primera adivinanza")
# print(adivinanzas[1])
# print(respuestas[1])#Mostramos la adivinanza 1 y la serie de opciones de 1
# respuesta = input('Tu respuesta a la primera adivinanza es: ')
# while (respuesta != 'a') & (respuesta != 'b') & (respuesta != 'c'):
#     respuesta = input('Tu respuesta. Debe ser a o b o c: ')
# if respuesta == respuestasCorrectas[1]:#comprobamos si la respuesta que nos da es igual a la 1 que sale en el diccionario de correctas
#     puntuacion = puntuacion + 10
# else:
#     puntuacion = puntuacion - 5

# print("Segunda adivinanza")
# print(adivinanzas[2])
# print(respuestas[2])
# respuesta = input('Tu respuesta a la segunda adivinanza es: ')
# while (respuesta != 'a') & (respuesta != 'b') & (respuesta != 'c'):
#     respuesta = input('Tu respuesta. Debe ser a o b o c: ')
# if respuesta == respuestasCorrectas[2]:
#     puntuacion = puntuacion + 10
# else:
#     puntuacion = puntuacion - 5

# print("Tercera adivinanza")
# print(adivinanzas[3])
# print(respuestas[3])
# respuesta = input('Tu respuesta a la tercera adivinanza es: ')
# while (respuesta != 'a') & (respuesta != 'b') & (respuesta != 'c'):
#     respuesta = input('Tu respuesta. Debe ser a o b o c: ')
# if respuesta == respuestasCorrectas[3]:
#     puntuacion = puntuacion + 10
# else:
#     puntuacion = puntuacion - 5

# print("Tu puntuación final es: " + str(puntuacion))

#                                           Empleando random.sample()

#convertimos las claves del diccionario adivinanzas para así darle una secuencia al random.sample()
adivinanzas_keys = list(adivinanzas.keys())

#Aquí seleccionamos 2 adivinanzas al azar
adivinanzas_seleccionadas = random.sample(adivinanzas_keys, 2)

for adivinanza_id in adivinanzas_seleccionadas:
    print(adivinanzas[adivinanza_id])
    print(respuestas[adivinanza_id])

    # Preguntamos al usuario por su respuesta y comprobamos que sea alguno de los valores dados como respuesta
    respuesta_usuario = input("Tu respuesta (a/b/c): ")
    while(respuesta_usuario != 'a') & (respuesta_usuario != 'b') & (respuesta_usuario != 'c'):
        respuesta_usuario = input('Tu respuesta. Debe ser a, b o c: ')
    # Verificamos si la respuesta del usuario es correcta
    if respuesta_usuario == respuestasCorrectas[adivinanza_id]:
        print("¡Respuesta correcta!\n")
    else:
        print("Respuesta incorrecta. La respuesta correcta es: " + respuestasCorrectas[adivinanza_id] + "\n")