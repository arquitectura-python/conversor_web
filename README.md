 # PYTHON_APP WEB

_Aplicación que nos permite convertir el formato de imagenes_ 

## Requisitos  📋
```list
-flask
-python3
-pillow
```
* **Librerias Importadas** 📋

***Pillow, la biblioteca Python para tratamiento de imágenes***

bashPillow es una biblioteca para el tratamiento y edición de imágenes que hereda de PIL. Pillow soporta gran cantidad de formatos de imagen, entre ellos, los más comunes: JPG, PNG y GIF.

$> pip install pillow

Se ejecuta este comando en Python para importar la libreria de Pillow, antes de ejecutar la aplicación.

## Crear entorno 🚀
para crear nuestro entorno virtual primero debemos tener instalado virtualenv en nuestro sistema, dejare un ejemplo de como instalarlo en python

```bash
pip3 install virtualenv
```

Luego en la carpeta en donde se va a clonar el proyecto creamos nuestro entorno

```bash
virtualenv nombre_entorno -p python3
```

se activa de la siguiente manera 
```bash
source nombre_entorno/bin/activate
```

## Instalar requerimientos

Una vez tenemos nuestro entorno activo debemos instalar los requerimientos

```bash
pip install -r requirements.txt
```

## Ejecutar aplicacion 

Cuando se tengan todas las dependencias instaladas hay que ejecutar el proyecto para eso ejecuctamos el siguinte comando 
```python
  flask run
```

también se puede ejecutar de la siguiente manera
```python
 python run.py
```


* **Comentarios Código Aplicación Web Lenguaje Python** :left_speech_bubble:

    **from PIL import Image** Se está importando la libreria. El módulo (Image) proporciona una clase con el mismo nombre que se utiliza para representar una imagen PIL. El módulo también proporciona una serie de funciones de fábrica, incluidas funciones para cargar imágenes desde archivos y crear nuevas imágenes.
                      
    **import os** El módulo nos permite acceder a funcionalidades dependientes del Sistema Operativo, sobre todo, aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular la estructura de directorios (para leer y escribir archivos).
    **import sys** Este módulo provee acceso a algunas variables usadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete.


          
    ## Construido con 🛠️

_Este proyecto fue construido en _

* [Visual Studio Code ](https://code.visualstudio.com/) - Herramenta Utilazada 
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS


