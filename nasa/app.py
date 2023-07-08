
from flask import Flask,jsonify,Request,Response,render_template;
#from config import API_KEY;
from apod import apod;
from exploracionPlanetaria import exploracionPlanetaria;
from marsRoversPhotos import photos;

# Darle un nombre a la variable y que se llamara en el main
app = Flask(__name__)

# Para mandar a llamar a los archivos index
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apod')
def apod_route():
    return apod()

@app.route('/exploracionPlanetaria')
def explP_route():
    return exploracionPlanetaria()

@app.route('/MarsRover')
def MarsRover_route():
    return photos()

if __name__ == '__main__':
    app.run(debug=True,port=5001)