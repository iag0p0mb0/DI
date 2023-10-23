from tkinter import Tk
# from ventana import MainWindow
from loadingWindow import LoadingWindow

if __name__ == "__main__":
    root = Tk()
    # app = MainWindow(root)
    app = LoadingWindow(root)
    root.mainloop()