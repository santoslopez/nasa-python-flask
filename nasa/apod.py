import requests as request;
from flask import render_template,jsonify;
from config import API_KEY;
from datetime import datetime;

def apod():
    url = 'https://api.nasa.gov/planetary/apod';
    # obtener fecha actual de mi servidor, NO de la NASA
    fechaActual = datetime.now().strftime('%Y-%m-%d')
    parametros = {'api_key':API_KEY,'date':fechaActual}
    response = request.get(url, params=parametros)
    
    try:
        if response.status_code == 200:
            datos = response.json()
            urlAPOD = datos['url']        
            explanation = datos['explanation']
            titleImage = datos['title']   
            copyright = datos['copyright']        
            return render_template('apod.html',explanation=explanation,titleImage=titleImage,urlAPOD=urlAPOD,copyright=copyright,date=fechaActual)   
        else:
            return render_template('apod.html',errorAPI="Error en la API")
        # en caso que se coloque un dato que no existe en la API mostrarlo
    except KeyError as e:
        mensaje_error = f"La clave '{e.args[0]}' no existe en el diccionario."
        return jsonify({'error': mensaje_error}), 400
