
from flask import Flask,jsonify,request,Response,render_template;

from apod import apod;
from exploracionPlanetaria import exploracionPlanetaria;
from marsRoversPhotos import photos;

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

# Para mandar a llamar a los archivos index
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apod')
def apod_route():
    return apod()

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

if __name__ == '__main__':
    app.run(debug=True)