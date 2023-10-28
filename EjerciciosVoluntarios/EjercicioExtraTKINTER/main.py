from loadingWindow import LoadingWindow
from difficultyWindow import Difficulty
from show_game_window import ShowGameWindow

if __name__ == "__main__":
    #descarga de imágenes del ahorcado y json de palabras:
    app1 = LoadingWindow()
    while True:
        #ventana para seleccionart la dificultad:
        app2 = Difficulty()
        if app2.choice != "salir":
            #ventana que muestra el juego:
            app3 = ShowGameWindow(app2.choice, app1.gameImages, app1.palabras_json)
        else:
            break