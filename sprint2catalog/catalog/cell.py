from PIL import ImageTk, Image
import requests
from io import BytesIO

class Cell:
    def __init__(self,name,url,desc): 
        self.name = name 
        self.desc = desc
        self.url = url
        #con esto descargamos la imagen y la guardamos en Image_Tk
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        self.img = ImageTk.PhotoImage(img_data)