import tkinter as tk

class Difficulty:
    # Dimensiones pantalla carga:
    width = 320
    height = 165

    # Variable elección:
    choice = ""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ahorcado")

        # Establecimiento dimensiones:
        self.root.geometry(f"{int(self.width)}x{int(self.height)}")
        self.root.resizable(False, False)
        self.root.config(width=self.width, height=self.height, bg="navy")
        self.root.geometry(f"+{int((self.root.winfo_screenwidth()-self.width)/2)}+{int((self.root.winfo_screenheight()-self.height)/2)}")

        label = tk.Label(self.root, text="SELECCIONE NIVEL DE DIFICULTAD:", fg="lightgray", font="System", background="navy")
        label.pack()

        # Botones opciones:
        button1 = tk.Button(
            self.root,
            width=6,
            text="FÁCIL",
            fg="white",
            background="red",
            font=("Arial",14),
            activeforeground="black",
            activebackground="orange",
            name="facil",
            command=lambda:self.buttonClick(button1.cget("text"))
        )
        button2 = tk.Button(
            self.root,
            width=6,
            text="MEDIO",
            fg="white",
            background="red",
            font=("Arial",14),
            activeforeground="black",
            activebackground="orange",
            name="normal",
            command=lambda:self.buttonClick(button2.cget("text"))
        )
        button3 = tk.Button(
            self.root,
            width=6,
            text="DIFÍCIL",
            fg="white",
            background="red",
            font=("Arial",14),
            activeforeground="black",
            activebackground="orange",
            name="dificil",
            command=lambda:self.buttonClick(button3.cget("text"))
        )
        button4 = tk.Button(
            self.root,
            text="SALIR",
            fg="white",
            background="red",
            font=("Arial",14),
            activeforeground="black",
            activebackground="orange",
            name="salir",
            command=lambda:self.buttonClick(button4.cget("text"))
        )

        button1.pack(anchor="n", pady=5)
        button2.pack(anchor="n")
        button3.pack(anchor="n", pady=5)
        button4.pack(side="bottom", anchor="e", pady=(15,5), padx=(5))
        
        self.root.mainloop()

    #click del botón
    def buttonClick(self, button_name):
        if button_name == "DIFÍCIL":
            self.choice = "Difícil"
        elif button_name == "MEDIO":
            self.choice = "Normal"
        elif button_name == "FÁCIL":
            self.choice = "Fácil"
        else:
            self.choice = "salir"
        self.root.destroy()