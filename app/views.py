import os

from app import app
from flask import render_template, request, redirect, send_file, abort,send_from_directory, url_for


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload-image", methods = ["POST"])
def recibir_imagen():
    if request.method == "POST":
        if request.files:
            extension = request.form.get("extension")
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            print(image)
            print(extension)
            return redirect(url_for('descargar_imagen',nombre_imagen = image.filename))


@app.route("/download-image/<nombre_imagen>")
def descargar_imagen(nombre_imagen):
    try:
        return send_from_directory(app.config["IMAGE_UPLOADS"], filename=nombre_imagen, as_attachment=True)
    except FileNotFoundError:
        abort(404)
              