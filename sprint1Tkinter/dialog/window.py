from tkinter import ttk
from yes_window import show_yes_window
from no_window import show_no_window

class MainWindow:

    def onButtonClickedYes(self):
        show_yes_window()

    def onButtonClickedNo(self):
        show_no_window()

    def __init__(self, root):

        self.root = root
        
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text = "¿Se lee algo en esta ventana?")
        self.label.pack()
        
        # self.button = ttk.Button(self.frame, text = "Realizar la acción", command = self.onButtonClicked)
        # self.button.pack()
        self.buttonYes = ttk.Button(self.frame, text = "Yes", command = self.onButtonClickedYes)
        self.buttonNo = ttk.Button(self.frame, text = "No", command = self.onButtonClickedNo)
        self.buttonYes.pack(side="left")
        self.buttonNo.pack(side = "right")
    