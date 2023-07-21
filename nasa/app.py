
from flask import Flask,jsonify,request,Response,render_template;

from apod import apod;
from exploracionPlanetaria import exploracionPlanetaria;
from marsRoversPhotos import photos;
from galeriaMultimedia import buscarGaleriaMultimedia;

# Darle un nombre a la variable y que se llamara en el main
app = Flask(__name__)

diccionarioRoverCamaras =  {
    "FHAZ":"Front Hazard Avoidance Camera",
    "RHAZ":"Rear Hazard Avoidance Camera",
    "MAST":"Mast Camera",
    "CHEMCAM":"Chemistry and Camera Complex",
    "MAHLI":"Mars Hand Lens Imager",
    "MARDI":"Mars Descent Imager",
    "NAVCAM":"Navigation Camera",
    "PANCAM":"Panoramic Camera",
    "MINITES":"Miniature Thermal Emission Spectrometer (Mini-TES)"	
}

# Para mandar a llamar al el archivo de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Manda a llamar la página de apod: que muestra la imagen del día
@app.route('/apod')
def apod_route():
    # apod() es la función que se encuentra en el archivo apod.py
    return apod()

# Se utiliza en filtrarImagenes.js
@app.route('/llamar_apod/<string:parametro>',methods=['POST'])
def llamar_apod(parametro):
    resultado = photos(parametro)
    return resultado

@app.route('/exploracionPlanetaria')
def explP_route():
    return exploracionPlanetaria()

@app.route('/MarsRover')
def MarsRover_route():
    return render_template('MarsRover/photos.html',diccionarioRoverCamaras=diccionarioRoverCamaras)

@app.route('/galeriaMultimedia')
def galeryMultimedia():
    return render_template('galeriaMultimedia/galeriaMultimedia.html')

@app.route('/galeriaMultimediaFiltrarBusqueda/<string:parametro1>/<string:parametro2>',methods=['POST'])
def galeryMultimedia_route(parametro1,parametro2):
    return buscarGaleriaMultimedia(parametro1,parametro2)

''' 
    Manejo de errores
'''
@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html',error=error)

if __name__ == '__main__':
    app.run(debug=True)