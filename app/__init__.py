import os
from werkzeug.utils import secure_filename

from flask import Flask

directorio = os.getcwd()

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = directorio + '/app/static/uploads'
app.config["IMAGE_CONVERTED"] = directorio+'/app/static/converted'
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF", "BMP"]
from app import views, metodos
