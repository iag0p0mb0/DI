from tkinter import ttk
from tkinter import messagebox
import tkinter as tk #importamos toda la libreria de tkinter
from cell import Cell
from detail_window import detailWindow


class MainWindow():
        
    def onButtonClicked(self):
        #detailWindow(cell)
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
        widthWindow = 200
        heightWindow = 450
        self.root.geometry(f"{int(widthWindow)}x{int(heightWindow)}")
        # si implementamos este código, ancho y alto de la ventana serán números accesibles por winfo:
        self.root.config(width=widthWindow, height=heightWindow)
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight())/2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        #recorremos la lista de celdas para que se muestran en la ventana principal
        for i, cell in enumerate (self.cells):
            label = ttk.Label(root, image = cell.img, text = cell.name, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("<Button-1>", lambda event, cell = cell: self.onButtonClicked(cell))

        # Crear una barra de menús
        barra_menus = tk.Menu()
        menu_ayuda = tk.Menu(barra_menus, tearoff=False)
        # Agregarlo a la barra
        menu_ayuda.add_command(
        label="Acerca de",
        command=self.onButtonClicked
        )
        barra_menus.add_cascade(menu=menu_ayuda, label="Acerca de")
        root.config(menu=barra_menus)  
        root.mainloop()