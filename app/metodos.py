import os
from PIL import Image

from app import app


def convertir_imagen(imagen, extension): # metodo convetir imagen que recibe como parameto la imagen que se desea convertir y a la extencion que se quiere convertir
    img = Image.open(imagen) # se crea una variable img que a traves del metodo open de modulo image guarda la imagen como fichero 
    lista_temp = imagen.filename.split(".") ## [nombre, extension] se parte el nombre de la imagen para poder conceguir un arreglo que contenga el nombre de la imagen y su extension 
    nueva_imagen = lista_temp[0] # se crea una nueva variable en este caso se asigna el nombre de la variable que se desea convertir 
    nueva_imagen = nueva_imagen+"."+extension # se le concatena la nueva extension para poder definir el nuevo nombre de la nueva imagen
    img.save(os.path.join(app.config["IMAGE_CONVERTED"], nueva_imagen))# se utiliza el metodo save para generar una nueva imagen en base a la imagen anterior en una ruta preedefinia con el nuevo nombre que se creeo anteriormente , 
    return nueva_imagen # se retorna el nombre de la imagen ya canvertida para su porterior busqueda 