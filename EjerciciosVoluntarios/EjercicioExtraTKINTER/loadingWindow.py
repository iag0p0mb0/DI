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
    width = 320
    height = 240

    ini = -12
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
        self.canvas = tk.Canvas(self.root, background="white", highlightthickness=0, width=self.width, height=self.height)
        self.canvas.pack()
        self.canvas.create_text((self.width/2, 98), text="Cargando las imágenes y palabras...", font=("System", 12), fill="black", anchor="center", tags="texto")
    
        self.canvas.create_rectangle((38, self.height/2-8), (self.width-38, self.height/2+8), width=2, outline="black")#dibujamos la barra de carga:
        self.update_bar()

        #comprobamos la descarga del json
        self.check_thread()

        #hilo secundario de descarga
        self.thread = threading.Thread(target=self.fetch_json_data).start()

        self.root.mainloop()

    def draw_bar(self):
        self.canvas.create_line((42+self.ini, self.height/2), (42+self.fin, self.height/2), fill="black", width=8, tags="linea")

    def update_bar(self):
        #actualizamosinicio y fin para cada cuadrado de la barra:
        if self.ini < 228:
            self.ini += 10
            self.fin = self.ini + 8

        self.draw_bar()
        self.root.after(500, self.update_bar)
    
    def check_thread(self):
        #hace que si las descargas se acabaron, esta ventana se cierra
        if self.palabrasFinish & self.imagesFinish:
            self.root.destroy()
        else:
            #esta comprobación espera a que acabe la barra de carga:
            self.root.after(5000, self.check_thread)
    
    def fetch_json_data(self):
        #descarga de palabras.json:
        response_palabras = requests.get("https://raw.githubusercontent.com/iag0p0mb0/DI/main/EjerciciosVoluntarios/EjercicioExtraTKINTER/resources/palabras.json")
        if response_palabras.status_code == 200:
            self.palabras_json = response_palabras.json()
            self.palabras_finish = True
        #descargar y guardar imágenes en lista de Objetos Image:
        response_images = requests.get("https://raw.githubusercontent.com/iag0p0mb0/DI/main/EjerciciosVoluntarios/EjercicioExtraTKINTER/resources/ahorcado.json")
        if response_palabras.status_code == 200:
            for i in range(7):
                self.gameImages.append(ImageDownloader(response_images.json().get(f"{int(i)}")))
            self.images_finish = True