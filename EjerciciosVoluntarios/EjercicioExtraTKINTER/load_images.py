from PIL import Image
from io import BytesIO
import requests

#creamos una clase para descargar las imagenes como Objetos image

class ImageDownloader:
    def __init__(self, url):
        response_images = requests.get(url)
        self.img = Image.open(BytesIO(response_images.content))