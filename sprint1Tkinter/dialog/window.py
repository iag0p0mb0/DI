from tkinter import ttk

class MainWindow:

    def onButtonClicked():
        pass

    def __init__(self, root):

        self.root = root
        
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text = "Este mensaje es poco importante")
        self.label.pack()
        
        self.button = ttk.Button(self.frame, text = "Realizar la acción", command = self.onButtonClicked)
        self.button.pack()
    