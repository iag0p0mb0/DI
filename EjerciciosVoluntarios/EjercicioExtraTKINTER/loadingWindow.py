import tkinter as tk
import threading
import requests
from load_images import ImageDownloader

class LoadingWindow:
    #instanciam,os el JSON de las palabras que van a tener le juego
    palabras_json = {}
    #instanciamos el array de imágenes objeto
    gameImages = []
    #creamos unos booleanos de control de descarga de datos
    palabrasFinish = False
    imagesFinish = False

    #seleccionamos las dimensiones de la pantalla de carga
    width = 300
    height = 300

    ini = -10
    fin = 0

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cargando ahorcado...")

        #establecemos dimensiones
        self.root.geometry(f"{int(self.width)}x{int(self.height)}")
        self.root.resizable(False, False)
        self.root.config(width=self.width, height=self.height)
        self.root.geometry(f"+{int((self.root.winfo_screenwidth()-self.width)/2)}+{int((self.root.winfo_screenheight()-self.height)/2)}")

        #creamos un canvas con texto y barra de carga
        self.canvas = tk.Canvas(self.root, background="navy", highlightthickness=0, width=self.width, height=self.height)
        self.canvas.pack()
        self.canvas.create_text((self.width/2, 98), text="Cargando las imágenes y palabras...", font=("System", 12), fill="lightgray", anchor="center", tags="texto")
        #dibujamos la barra de carga:
        self.update_bar()

        #comprobamos la descarga del json
        self.check_thread()

        #hilo secundario de descarga
        self.thread = threading.Thread(target=self.fetch_json_data).start()

        self.root.mainloop()

