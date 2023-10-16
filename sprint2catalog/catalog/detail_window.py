import tkinter as tk

def detailWindow(cell):

    root1 = tk.Toplevel() # con el comando TopLevel lo que hacemos es generar una ventana nueva sin cerrar de la que venimos
    root1.title("DetailWindow")
    label1 = tk.Label(root1, image = cell.image_tk)
    label2 = tk.Label(root1, text = cell.title)
    label3 = tk.Label(root1, text = cell.desc) 
    label1.pack()
    label2.pack()
    label3.pack()

    # Creamos las etiquetas para cada cosa que queremos mostrar y posteriormente las empaquetamos para podedr mostrarlas

    root1.mainloop()
        