#https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?
import requests as request;
from flask import render_template,jsonify;
from config import API_KEY;
from datetime import datetime;

def photos():
    #url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos";
    parametros = {'api_key':API_KEY}
    response = request.get(url,params=parametros)
    try:
        if response.status_code == 200:
            datos = response.json()
            # necesario para almacenar las imagenes
            imagenes = []
            nombreCamaras=  []
            # latest_photos corresponde al nombre que está en la API
            for foto in datos['latest_photos']:
                #imagenes.append(foto['img_src'])
                arreglo_imagenes = {
                    'img_src': foto['img_src'],
                    'titulo': foto['camera']['full_name'],
                    'earth_date': foto['earth_date'],
                    'fecha':datetime.strptime(foto['earth_date'],'%Y-%m-%d').strftime('%d/%m/%Y'),
                }
                imagenes.append(arreglo_imagenes)
                nombreCamaras.append(foto['camera']['full_name'])
            return render_template('MarsRover/photos.html',imagenes=imagenes,nombreCamaras=nombreCamaras)
        else:
            return render_template('MarsRover/photos.html',errorAPI="Error en la API")
        # en caso que se coloque un dato que no existe en la API mostrarlo
    except KeyError as e:
        mensaje_error = f"La clave '{e.args[0]}' no existe en el diccionario."
        return jsonify({'error': mensaje_error}), 400
