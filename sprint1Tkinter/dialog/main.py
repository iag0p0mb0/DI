from tkinter import Tk
from window import MainWindow

if __name__ == "__main__":
    root = Tk() #En esta línea se crea una ventana vacía
    app = MainWindow(root)
    root.mainloop()