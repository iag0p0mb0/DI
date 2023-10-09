from tkinter import ttk
import tkinter as tk #importamos toda la libreria de tkinter
from cell import Cell
from PIL import Image, ImageTk
from tkinter import messagebox
from detail_window import detailWindow


class MainWindow():

    def onButtonClicked(self, cell):
        #pass
        # message = "Has hecho click en la celda " + cell.title
        # messagebox.showinfo(("Información --> ", message))
        detailWindow(cell)

    def __init__(self, root):

        root.title("MainWindow")

        # self.cells = [
        #     Cell("Tucán", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\6-lugares-donde-puedes-ver-animales-exoticos-6.jpg"),
        #     Cell("Lobo", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\animales-destacada.jpg"),
        #     Cell("Oso perezoso", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\animales-felices-portada-1280x720x80xX.jpg"),
        #     Cell("Perro y gato", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\dia-de-los-animales.jpg"),
        #     Cell("Mapache", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\edited\\proteger-a-los-animales.jpg")
        # ]

        self.cells = [
            Cell("Tucán", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\6-lugares-donde-puedes-ver-animales-exoticos-6.jpg", "El tucán es un ave exótica y colorida que pertenece a la familia Ramphastidae. Son conocidos por su distintivo pico largo y colorido, que puede medir hasta la mitad de la longitud total del ave. Este pico, a menudo de tonos brillantes como el naranja, el amarillo y el verde, es su característica más distintiva y sirve para atraer a las parejas y como herramienta para alcanzar frutas y presas en las copas de los árboles de la selva tropical, donde habitan.\nLos tucanes son aves de tamaño mediano a grande, con cuerpos compactos y plumaje brillante. Tienen patas cortas y fuertes adaptadas para trepar y saltar entre las ramas de los árboles. Aunque su vuelo puede parecer torpe debido a su tamaño y forma, son ágiles en el aire y pueden realizar vuelos cortos y precisos.\nEstas aves son omnívoras y se alimentan principalmente de frutas, pero también consumen insectos, pequeños vertebrados y huevos. Son importantes dispersores de semillas en los bosques tropicales, ya que suelen tragar frutas enteras y luego excretar las semillas en diferentes lugares, ayudando así a la regeneración de la flora.\nLos tucanes son conocidos por su comportamiento social y a menudo se les encuentra en grupos familiares o bandadas. Son un símbolo icónico de las selvas tropicales de América Central y del Sur y son apreciados por su belleza y singularidad en el mundo de las aves."),
            Cell("Lobo", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\animales-destacada.jpg", "El lobo, Canis lupus, es una impresionante criatura que inspira fascinación y respeto en igual medida. Este mamífero carnívoro, miembro de la familia Canidae, se caracteriza por su apariencia majestuosa y su estilo de vida social y organizado.\nLos lobos exhiben un cuerpo musculoso y estilizado, con un pelaje espeso y variado que puede oscilar desde tonos de gris y blanco en las regiones polares hasta marrones y negros en hábitats más cálidos. Sus ojos, generalmente amarillos o dorados, brillan con una intensidad enigmática y están adaptados para una visión nocturna excepcional. Las orejas puntiagudas y las patas fuertes con garras afiladas refuerzan su imagen de depredador supremo.\nEstos animales son conocidos por su vida en manadas, donde la cooperación es fundamental. Establecen jerarquías complejas y trabajan en equipo para cazar presas como ciervos y bisontes. Su capacidad de comunicación incluye aullidos melodiosos, que desempeñan un papel en la cohesión de la manada y en la demarcación de territorios.\nA lo largo de la historia, los lobos han sido objeto de mitos y leyendas, a menudo representados como símbolos de valentía y lealtad. Sin embargo, también han enfrentado amenazas por parte de los humanos, lo que ha llevado a la disminución de sus poblaciones en muchas regiones. A pesar de esto, los lobos siguen siendo una parte integral de los ecosistemas naturales y un recordatorio de la belleza y la importancia de la fauna salvaje en nuestro mundo."),
            Cell("Oso perezoso", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\animales-felices-portada-1280x720x80xX.jpg", "El oso perezoso, cuyo nombre científico es Bradypus, es una criatura extraordinaria que habita en las selvas tropicales de América Central y del Sur. A pesar de su nombre, los osos perezosos no están relacionados con los verdaderos osos y, de hecho, son parientes lejanos de los armadillos y los puercoespines.\nEstos animales son conocidos por su aspecto inusual y su estilo de vida tranquilo. Tienen un pelaje grueso y áspero que varía en tonos de marrón y gris, lo que les proporciona una camuflaje efectivo en el dosel forestal. Su nombre, perezoso, se debe a su movimiento lento y deliberado. Poseen extremidades largas y garras curvadas que les permiten colgarse de las ramas de los árboles y moverse con facilidad entre ellas.\nEl oso perezoso se alimenta principalmente de hojas, brotes y frutas, y su metabolismo es sorprendentemente lento, lo que les permite conservar energía. Pasan la mayor parte de su vida en los árboles, donde pueden dormir hasta 15 horas al día.\nAunque su movimiento lento puede hacerlos vulnerables a los depredadores, su camuflaje y su capacidad para pasar desapercibidos en la densa vegetación los ayudan a mantenerse a salvo. Los osos perezosos son criaturas fascinantes que representan un ejemplo único de adaptación a la vida en la selva tropical y son un tesoro de la biodiversidad de América."),
            Cell("Perro y gato", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\dia-de-los-animales.jpg", "El perro y el gato son dos de los animales de compañía más queridos y populares en todo el mundo, cada uno con características únicas que los hacen especiales.\nEl perro, conocido científicamente como Canis lupus familiaris, es conocido por su lealtad inquebrantable hacia los humanos. Los perros vienen en una variedad de razas, tamaños y personalidades, lo que les permite adaptarse a una amplia gama de hogares y estilos de vida. Son animales sociales por naturaleza y forman fuertes lazos con sus dueños. Los perros son conocidos por su inteligencia y capacidad para aprender comandos y tareas diversas, lo que los convierte en compañeros versátiles y útiles.\nPor otro lado, el gato, cuyo nombre científico es Felis catus, es apreciado por su independencia y elegancia. Los gatos son animales territoriales y pueden ser cariñosos, pero también disfrutan de su espacio personal. Son cazadores naturales y pueden mantener a raya la población de roedores en los hogares. Los gatos son conocidos por su agilidad y destreza, lo que los hace excelentes saltadores y trepadores.\nTanto perros como gatos pueden brindar compañía y afecto a sus dueños, cada uno con su propio estilo único. La elección entre un perro y un gato como mascota depende de la personalidad y el estilo de vida de cada individuo, pero en ambos casos, estos animales pueden enriquecer nuestras vidas de innumerables maneras."),
            Cell("Mapache", "C:\\msys64\\home\\iagop\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\proteger-a-los-animales.jpg", "El mapache, científicamente conocido como Procyon lotor, es un mamífero carnívoro que se encuentra principalmente en América del Norte y América Central. Se caracteriza por su apariencia distintiva y su comportamiento inteligente y adaptable.\nLos mapaches tienen un cuerpo robusto y peludo, con un pelaje denso que varía en colores que van desde el gris hasta el marrón. Sus patas delanteras son hábiles y están equipadas con cinco dedos con garras, que les permiten manipular objetos con destreza, lo que les ha ganado la reputación de ser ladrones por su capacidad para abrir cerraduras y contenedores. También tienen una máscara facial negra en su rostro, que les otorga una apariencia de bandido.\nSon animales nocturnos y omnívoros, lo que significa que se alimentan de una amplia variedad de alimentos, incluyendo frutas, vegetales, insectos, pequeños mamíferos y aves, así como alimentos dejados por los humanos en entornos urbanos. Los mapaches son conocidos por su habilidad para adaptarse a diferentes entornos y su inteligencia, que les permite resolver problemas y encontrar alimentos de manera creativa.\nAdemás de su apariencia única y su comportamiento astuto, los mapaches son parte integral de los ecosistemas en los que habitan y desempeñan un papel importante en la dispersión de semillas y el control de poblaciones de insectos. Son criaturas fascinantes que han sabido coexistir con los humanos en entornos urbanos, lo que ha contribuido a su estatus de animales icónicos en la cultura popular.")
        ]

        for i, cell in enumerate(self.cells):

            # img = Image.open(self.path)#Con esto lo que hacemos es abrir la imagen de la posición en la que estemos, es decir, con este for vamos a pasar por todas las imagenes en el self.cell
            # img1 = img.resize((100, 100), Image.LANCZOS)#Aquí lo que hacemos es reescalar la imagen a 100 x 100
            # self.image_tk = ImageTk.PhotoImage(img1)

            label = tk.Label(root, image = cell.image_tk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("<Button-1>", lambda event, cell = cell : self.onButtonClicked(cell))#escucha eventos sobre los widgets que programamos
                #esto es un controlador de evento para cuando presionemos un botón
        
        # #Marco
        # self.root = root
        # self.frame = ttk.Frame(self.root)
        # self.frame.pack()

        # #Etiqueta
        # self.label = ttk.Label(self.frame, text = "Este mensaje es poco importante")
        # self.label.pack()

        # #Botón
        # self.button = ttk.Button(self.frame, text = "Realizar la acción", command = self.onButtonClicked)
        # self.button.pack()