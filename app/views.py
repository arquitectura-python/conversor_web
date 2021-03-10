import os

from app import app
from app.metodos import convertir_imagen
from flask import render_template, request, redirect, send_file, abort,send_from_directory, url_for
from werkzeug.utils import secure_filename


@app.route("/") #se define la ruta por defecto 
def index():
    error = ""
    return render_template("index.html", error = request.args.get('error')) # se renderiza el archo index html de nustra carpeta template

def allowed_image(filename):# metodo para saber si la extension del archivo es valida 

    if not "." in filename: # si el archivo no cuenta con un punto en su nombre quiere decir que no es un archivo y retornara falso 
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:# verificamos si la extension del archivo se encuentra en la extensiones permitidas en la aplicacion
        return True # si es asi retornara verdadero y nos dejara seguir 
    else: # en caso contrario no es un archivo permitido y no dejará subirlo 
        return False
"""
se define la ruta /upload-image que utiliza el metodo Http POST  en donde vamos a recibir de nuestro formulario
la imagen que el usuario desea converti y la extension a la que se desea pasar  este evaluar si la imagen evaluara si es valida o no. si lo es
la guardara temporalmente en una carpeta predefinida, luego llamara el metodo de convertir imagen mandano como parametro la imagen que se recibio
y la nueva extension, se convierte de manera exitosa se retornara la nueva imagen a la ruta /download-image pasando como parametro la nueva imagen.

"""
@app.route("/upload-image", methods = ["POST"])
def recibir_imagen():
    if request.method == "POST":
        if request.files:
            extension = request.form.get("extension")
            image = request.files["image"]
            if image.filename == "":
                print("No hay nada seleccionado")
                return redirect(request.url)
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
                print(image.filename)
                print(extension)
                nuevo_nombre =  convertir_imagen(image,extension)
                return redirect(url_for('descargar_imagen',nombre_imagen = nuevo_nombre))
            else:
                return redirect(url_for('index', error = "Archivo no valido"))

@app.route("/download-image/<nombre_imagen>")# se define la ruta /download-image que recibira como parametro una imagen 
def descargar_imagen(nombre_imagen):# recibe el nombre de una imagen como parametro 
    try:
        return send_from_directory(app.config["IMAGE_CONVERTED"], filename=nombre_imagen, as_attachment=True)# si el nombre de imagen se encuentra en la carpeta de imagenes compartidas se retornara esta imagen para su descarga
    except FileNotFoundError: # En dado caso que no se encuentre uma imagen con es nombre se retornara un Error 
        abort(404)
              