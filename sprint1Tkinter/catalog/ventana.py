from tkinter import ttk
import tkinter as tk #importamos toda la libreria de tkinter
from cell import Cell
from PIL import Image, ImageTk
from tkinter import messagebox
from detail_window import detailWindow


class MainWindow():

    def onButtonClicked(self, cell):
        #pass
        # message = "Has hecho click en la celda " + cell.title
        # messagebox.showinfo(("Información --> ", message))
        detailWindow(cell)

    def __init__(self, root):

        root.title("MainWindow")

        # self.cells = [
        #     Cell("Tucán", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\6-lugares-donde-puedes-ver-animales-exoticos-6.jpg"),
        #     Cell("Lobo", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\animales-destacada.jpg"),
        #     Cell("Oso perezoso", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\animales-felices-portada-1280x720x80xX.jpg"),
        #     Cell("Perro y gato", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\dia-de-los-animales.jpg"),
        #     Cell("Mapache", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\proteger-a-los-animales.jpg")
        # ]

        self.cells = [
            Cell("Tucán", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\6-lugares-donde-puedes-ver-animales-exoticos-6.jpg", "El tucán es un ave tropical con pico largo y colorido."),
            Cell("Lobo", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\animales-destacada.jpg", "El lobo es un carnívoro social de pelaje variado, con mirada intensa y aullidos melódicos."),
            Cell("Oso perezoso", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\animales-felices-portada-1280x720x80xX.jpg", "El oso perezoso es un mamífero tranquilo de pelaje áspero que vive en los árboles."),
            Cell("Perro y gato", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\dia-de-los-animales.jpg", "El perro es leal y versátil; el gato es independiente y ágil. Ambos son queridos como mascotas en todo el mundo."),
            Cell("Mapache", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\proteger-a-los-animales.jpg", "El mapache es un mamífero nocturno con máscara facial y habilidades astutas.")
        ]

        for i, cell in enumerate(self.cells):

            # img = Image.open(self.path)#Con esto lo que hacemos es abrir la imagen de la posición en la que estemos, es decir, con este for vamos a pasar por todas las imagenes en el self.cell
            # img1 = img.resize((100, 100), Image.LANCZOS)#Aquí lo que hacemos es reescalar la imagen a 100 x 100
            # self.image_tk = ImageTk.PhotoImage(img1)

            label = tk.Label(root, image = cell.image_tk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("<Button-1>", lambda event, cell = cell : self.onButtonClicked(cell))#escucha eventos sobre los widgets que programamos
                #esto es un controlador de evento para cuando presionemos un botón
        
        # #Marco
        # self.root = root
        # self.frame = ttk.Frame(self.root)
        # self.frame.pack()

        # #Etiqueta
        # self.label = ttk.Label(self.frame, text = "Este mensaje es poco importante")
        # self.label.pack()

        # #Botón
        # self.button = ttk.Button(self.frame, text = "Realizar la acción", command = self.onButtonClicked)
        # self.button.pack()