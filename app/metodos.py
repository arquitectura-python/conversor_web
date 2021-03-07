import os
from PIL import Image

from app import app


def convertir_imagen(imagen, extension):
    img = Image.open(imagen)
    lista_temp = imagen.filename.split(".") ## [nombre, extension]
    nueva_imagen = lista_temp[0]
    nueva_imagen = nueva_imagen+"."+extension
    img.save(os.path.join(app.config["IMAGE_CONVERTED"], nueva_imagen))
    return nueva_imagen