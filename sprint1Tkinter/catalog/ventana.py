from tkinter import ttk
import tkinter as tk #importamos toda la libreria de tkinter
from cell import Cell
from tkinter import messagebox


class MainWindow():

    def onButtonClicked(self, cell):
        #pass
        message = "Has hecho click en la celda " + cell.title
        messagebox.showinfo(("Información --> ", message))

    def __init__(self, root):
        
        root.title("MainWindow")

        self.cells = [
            Cell("Tucán", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\6-lugares-donde-puedes-ver-animales-exoticos-6.jpg"),
            Cell("Lobo", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\animales-destacada.jpg"),
            Cell("Oso perezoso", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\animales-felices-portada-1280x720x80xX.jpg"),
            Cell("Perro y gato", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\dia-de-los-animales.jpg"),
            Cell("Mapache", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\proteger-a-los-animales.jpg")
        ]

        for i, cell in enumerate(self.cells):
            label = tk.Label(root, image = cell.image_tk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("Button-1", lambda event, cell = cell: self.onButtonClicked(cell))#escucha eventos sobre los widgets que programamos
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