 # PYTHON_APP WEB

_Aplicación que nos permite convertir el formato de imagenes  JPG, PNG y GIF.)_ 

## Dependencias   📋
```list
-flask
-python3
-pillow
```
## Librerias Importadas :bookmark_tabs:

***Pillow, la biblioteca Python para tratamiento de imágenes***

bashPillow es una biblioteca para el tratamiento y edición de imágenes que hereda de PIL. Pillow soporta gran cantidad de formatos de imagen, entre ellos, los más comunes: JPG, PNG y GIF.

```bash
pip install pillow
```

Se ejecuta este comando en Python para importar la libreria de Pillow, antes de ejecutar la aplicación.

## Crear entorno 🚀
para crear nuestro entorno virtual primero debemos tener instalado virtualenv en nuestro sistema, dejare un ejemplo de como instalarlo en python

```bash
pip install virtualenv
```

Luego en la carpeta en donde se va a clonar el proyecto creamos nuestro entorno

```bash
virtualenv nombre_entorno -p python3
```

se activa de la siguiente manera 
```bash
source nombre_entorno/bin/activate
```

## Instalar requerimientos :arrow_down: 

Una vez tenemos nuestro entorno activo debemos instalar los requerimientos

```bash
pip install -r requirements.txt
```
En caso de tener error en el comando anterior, intentar intalando las dependencias de la siguiente manera

```bash
pip install flask
```
```bash
pip install Pillow
```
```bash
pip install uwsgi
```

## Ejecutar aplicacion :eject_button:

Cuando se tengan todas las dependencias instaladas hay que ejecutar el proyecto para eso ejecuctamos el siguinte comando 
```python
  flask run
```

también se puede ejecutar de la siguiente manera
```python
 python run.py
```


## Comentarios Código Aplicación Web Lenguaje Python :left_speech_bubble:

**from PIL import Image** Se está importando la libreria. El módulo (Image) proporciona una clase con el mismo nombre que se utiliza para representar una imagen PIL. El módulo también proporciona una serie de funciones de fábrica, incluidas funciones para cargar imágenes desde archivos y crear nuevas imágenes.
                      
**import os** El módulo nos permite acceder a funcionalidades dependientes del Sistema Operativo, sobre todo, aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular la estructura de directorios (para leer y escribir archivos).
          
**import sys** Este módulo provee acceso a algunas variables usadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete.

**Flask** es un marco web de Python pequeño y ligero que proporciona herramientas y funciones útiles que hacen que crear aplicaciones web en Python sea más fácil. Ofrece a los desarrolladores flexibilidad y un marco más accesible para los nuevos desarrolladores ya que puede crear una aplicación web rápidamente usando únicamente un archivo Python. Flask también es extensible y no fuerza una estructura de directorio concreta ni requiere código estándar complicado antes de iniciarse.

          
  ## Construido con 🛠️

_Este proyecto fue construido en_

* [Visual Studio Code ](https://code.visualstudio.com/) - Edición de código Redefinido. 


## Despliegue 📦

Se utilizo marquina vitual de google con Sistema Operativo Ubuntu 18 server que cuenta con un servidor web Nginx, direccion IP http://35.224.41.245/


## Autores ✒️

* **Danilo Quintero** - *Desarrollador Backend* - [Danilo23](https://github.com/Danilo23)
* **Angel Mondragón** - *Desarrollador Backend* - [amondrave](https://github.com/amondrave)
* **Jhonatan Calderon** - *Desarrollador frontend* - [JhonatanCalderon12](https://github.com/JhonatanCalderon12)
* **Angela Acevedo** - *Desarrollador frontend* - [Angela2400](https://github.com/Angela2400)
* **Adriana Quijano** - *Documentador* - [adriana05](https://github.com/adriana05)
 :heartpulse:

