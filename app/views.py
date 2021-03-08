import os

from app import app
from app.metodos import convertir_imagen
from flask import render_template, request, redirect, send_file, abort,send_from_directory, url_for
from werkzeug.utils import secure_filename


@app.route("/")
def index():
    error = ""
    return render_template("index.html", error = request.args.get('error'))

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

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

@app.route("/download-image/<nombre_imagen>")
def descargar_imagen(nombre_imagen):
    try:
        return send_from_directory(app.config["IMAGE_CONVERTED"], filename=nombre_imagen, as_attachment=True)
    except FileNotFoundError:
        abort(404)
              