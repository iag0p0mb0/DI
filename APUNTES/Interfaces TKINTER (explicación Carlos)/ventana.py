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
            Cell("Tigre", "C:\\Users\\iagop\\OneDrive\\Imágenes\\Saved Pictures\\photo-1533450718592-29d45635f0a9.jpeg"),
            Cell("El nano", "C:\\Users\\iagop\\OneDrive\\Imágenes\\Saved Pictures\\Fernando_Alonso_2006_United_States_GP_(178149823).jpg"),
            Cell("Minions", "C:\\Users\\iagop\\OneDrive\\Imágenes\\Saved Pictures\\minion.webp")
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