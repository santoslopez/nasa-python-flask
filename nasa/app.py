import requests as request;

from flask import Flask,jsonify,Request,Response,render_template;

# Darle un nombre a la variable y que se llamara en el main
app = Flask(__name__)

# Para mandar a llamar a los archivos index
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/apod')
def apod():
    url = 'https://api.nasa.gov/planetary/apod';
    parametros = {'api_key':'jW2fwtlHdLabxdxlOxd1fHedTF8DNGADhWumWqlu'}
    response = request.get(url, params=parametros)
    
    try:
        if response.status_code == 200:
            datos = response.json()
            date = datos['date']
            explanation = datos['explanation']
            titleImage = datos['title']
            urlAPOD = datos['url']
            copyright = datos['copyright']        
            return render_template('apod.html',explanation=explanation,titleImage=titleImage,urlAPOD=urlAPOD,copyright=copyright,date=date)   
        else:
            return render_template('apod.html',errorAPI="Error en la API")
        # en caso que se coloque un dato que no existe en la API mostrarlo
    except KeyError as e:
        mensaje_error = f"La clave '{e.args[0]}' no existe en el diccionario."
        return jsonify({'error': mensaje_error}), 400

if __name__ == '__main__':
    app.run(debug=True)