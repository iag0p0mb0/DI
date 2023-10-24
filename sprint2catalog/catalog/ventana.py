from tkinter import ttk
from tkinter import messagebox
import tkinter as tk #importamos toda la libreria de tkinter
from cell import Cell
from detail_window import detailWindow


class MainWindow():
        
    def onButtonClickedDetailWindow(self, cell):
        detailWindow(cell)

    def onButtonClickedAcercaDe(self):
        messagebox.showinfo("Acerca del desarrollador", "Nombre: Iago Pombo\nEdad: 19")  

    def __init__(self, root, json_data):
        root.title("MainWindow")

        self.root = root

        self.cells =[]

        for animales in json_data:
            # Extraemos los valores 'name', 'description' y 'image_url' del catálogo actual
            name = animales.get("name")
            description = animales.get("description")
            image_url = animales.get("image_url")
            # Creamos un nuevo hilo que ejecutará la función self.load_image_url
            #guardar en una celda los datos del json
            cell = Cell(name,image_url,description)
            #añadimos la celda a la lista 
            self.cells.append(cell)

        # ancho y alto iguales para hacer la ventana cuadrada:
        size = 200
        self.root.geometry(f"{int(size)}x{int(size)}")
        # si implementamos este código, ancho y alto de la ventana serán números accesibles por winfo:
        self.root.config(width=size, height=size)
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight())/2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        # Crear una barra de menús
        barra_menus = tk.Menu()
        menu_ayuda = tk.Menu(barra_menus, tearoff=False)
        # Agregarlo a la barra
        menu_ayuda.add_command(
        label="Ayuda",
        command=self.onButtonClickedAcercaDe
        )
        barra_menus.add_cascade(menu=menu_ayuda, label="Ayuda")
        root.config(menu=barra_menus)  

        # implementación scrollbar:
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview, width=15)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        #recorremos la lista de celdas para que se muestran en la ventana principal
        for i, cell in enumerate (self.cells):
            frame = tk.Frame(self.scrollable_frame)
            frame.pack(pady=10)

            label = ttk.Label(frame, image = cell.img, text = cell.name, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("<Button-1>", lambda event, cell = cell: self.onButtonClickedDetailWindow(cell))


        self.canvas.grid(row = 0, column = 0, sticky="nsew")
        self.scrollbar.grid(row = 0, column = 1, sticky="ns")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)