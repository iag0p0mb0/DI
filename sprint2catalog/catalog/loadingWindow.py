import threading
import tkinter as tk

class LoadingWindow():
    #iniciamos el constructor
    def __init__(self, root):
        self.root = root
        #título de la ventana
        self.root.title("Cargando...")
        #dimensiones de la ventan
        self.root.geometry("170x120") #Define el ancho y la altura de la ventana
        #posibilidad de redimensión de la misma
        self.root.resizable(False, False) #Este comando permite indicar si la ventana se puede redimensionar tanto en ancho como en altura

        #creamos etiqueta para mostrar un texto
        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14)) #con font definimos el tipo y tamaño ded letra
        self.label.pack()

        label_bg_color = self.label.cget("bg")
        #cget nos permite obtener el valor de determinada opción pasada al widget, en este caso el fondo con bg
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress=0
        self.draw_progress_circle(self.progress) #dibuja el círculo

        self.update_progress_circle()

        # self.thread = threading.Thread(target=self.fetch_json_data)
        # self.thread.start()

    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")# elimina el objeto con la tag progress
        angle = int(360 * (progress/100))# damos ángulo a la circunferencia

        self.canvas.create_arc(10, 10, 35, 35,
                               start=0, extent=angle, tags="progress", outline="blue", width=4, style=tk.ARC)
        # este método se encarga de dibujar la circunferencia   

    def update_progress_circle(self):# función encargada de controlar el tiempo de vueltas de la circunferencia del proceso de carga
        if self.progress<100:
            self.progress+=14.20
        else:
            self.progress=0

        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)    