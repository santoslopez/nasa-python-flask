import requests as request;
from flask import render_template,jsonify;
from config import API_KEY;
from datetime import datetime;

def photos(nombreCamara):
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    #url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos";
    #camar = nombreCamara.lower()
    
    parametros = {'sol':1000,'camera':nombreCamara,'api_key':API_KEY}
    response = request.get(url,params=parametros)
    try:
        if response.status_code == 200:
            datos = response.json()
           
            # https://api.nasa.gov nombres de las camaras

            return datos
        else:
            return render_template('MarsRover/photos.html',errorAPI="Error en la API")
        # en caso que se coloque un dato que no existe en la API mostrarlo
    except KeyError as e:
        mensaje_error = f"La clave '{e.args[0]}' no existe en el diccionario."
        return jsonify({'error': mensaje_error}), 400
