import tkinter as tk

def detailWindow(cell):

    root = tk.Toplevel() # con el comando TopLevel lo que hacemos es generar una ventana nueva sin cerrar de la que venimos
    root.title("DetailWindow")
    # label1 = tk.Label(root1, image = cell.image_tk)
    # label2 = tk.Label(root1, text = cell.name)
    label1 = tk.Label(root, image=cell.img)
    label2 = tk.Label(root, text=cell.name)
    label3 = tk.Label(root, text = cell.desc) 
    label1.pack()
    label2.pack()
    label3.pack()

    # Creamos las etiquetas para cada cosa que queremos mostrar y posteriormente las empaquetamos para poder mostrarlas

    root.mainloop()
        