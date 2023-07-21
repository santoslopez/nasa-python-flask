import requests as request;
from flask import render_template,jsonify;
from config import API_KEY;
from datetime import datetime;

def buscarGaleriaMultimedia(inputBusqueda,tipoBusqueda):
    url ="https://images-api.nasa.gov/search"
    fechaActual = datetime.now().strftime('%Y')
    parametros = {'q':inputBusqueda,'media_type':tipoBusqueda,'year_start':1920,'year_end':fechaActual}
        
    response = request.get(url,params=parametros)
    #try:
    if response.status_code == 200:
        datos = response.json()
                
        # Se envia el diccionario con los datos de la API y en galeriaMultimedia.js se recupera la informacion
        return jsonify(datos)
    elif response.status_code == 400:
        return jsonify({'error':'Parámetro no válido en la API'}), 400
    else:
        return jsonify({'error':'Error en la API'}), 500
        #except KeyError as e:
        #mensaje_error = f"La clave '{e.args[0]}' no existe en el diccionario."
        #return jsonify({'error': mensaje_error}), 400
        #return jsonify({'error':'Parámetro no válido en la API'}), 400
