from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()
root.title("Ejemplo de imagen")

imagen = ImageTk.PhotoImage(file = "C:\\Users\\iagop\\OneDrive\\Imágenes\\Saved Pictures\\photo-1533450718592-29d45635f0a9.jpeg")
label = Label(root, image = imagen)
label.pack()

root.mainloop()