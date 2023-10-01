import random

def cargar_palabras(ruta_archivo):
    niveles = {}
    nivel_actual = None

    with open(ruta_archivo, "r") as archivo:
        for linea in archivo:
            palabra = linea.strip()

            if not palabra:
                continue

            if palabra in ["Facil", "Normal", "Dificil"]:
                nivel_actual = palabra
                niveles[nivel_actual] = []
            else:
                niveles[nivel_actual].append(palabra)

    return niveles

# Proporciona la ruta completa al archivo de palabras
ruta_archivo = r"C:\\msys64\\home\\iagop\\DWES\\sprint0python\\palabrasAhorcado.txt"
lvls = cargar_palabras(ruta_archivo)

repetir = "s"

while repetir == "s":
    print("\nIniciando el ahorcado...")
    dificultad = input("Elige el nivel de dificultad ('Facil', 'Normal', 'Dificil'): ")

    if dificultad in lvls:
        palabra_aleatoria = random.choice(lvls[dificultad])
        longitud_palabra = len(palabra_aleatoria)
        palabra_oculta = "-" * longitud_palabra
        print("\nLa palabra ha sido seleccionada con éxito. Comienza el juego...")
        print(f"La palabra oculta es: {palabra_oculta}")

        intentos = 6  # Número de intentos permitidos

        while intentos > 0 and palabra_oculta != palabra_aleatoria:
            letra = input("\nIntroduzca una letra: ").lower()

            if len(letra) != 1 or not letra.isalpha():
                print("Por favor, introduzca una única letra válida.")
                continue

            if letra in palabra_aleatoria:
                # Actualizamos la palabra oculta con la letra adivinada en todas las posiciones correspondientes
                palabra_oculta = "".join([letra if letra_palabra == letra else oculta for letra_palabra, oculta in zip(palabra_aleatoria, palabra_oculta)])
                print(f"Bien hecho. La palabra oculta es ahora: {palabra_oculta}")
            else:
                intentos -= 1
                print(f"Letra incorrecta. Te quedan {intentos} intentos.")
                print(f"La palabra oculta sigue siendo: {palabra_oculta}")

        if palabra_oculta == palabra_aleatoria:
            print("\n")
            print(f"Enhorabuena! Has adivinado la palabra. La palabra es: {palabra_aleatoria}")
        else:
            print("\n")
            print(f"Se acabaron los intentos. La palabra era: {palabra_aleatoria}. ¡Perdiste!")
    else:
        print("\nNo existe esa dificultad. Por favor, elija entre 'Facil', 'Normal' o 'Dificil'.")

    repetir = input("\n¿Desea volver a jugar? (s/n): ")