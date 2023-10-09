import tkinter as tk
from PIL import ImageTk, Image

class Cell:
    def __init__(self,title,path, desc):
        self.title = title
        self.path = path
        img = Image.open(self.path)# Con esto lo que hacemos es abrir la imagen de la posición en la que estemos, es decir, con este for vamos a pasar por todas las imagenes en el self.cell
        img1 = img.resize((100, 100), Image.LANCZOS)# Aquí lo que hacemos es reescalar la imagen a 100 x 100
        self.image_tk = ImageTk.PhotoImage(img1)
        self.desc = desc