import requests as request;
from flask import render_template,jsonify;
from config import API_KEY;

def exploracionPlanetaria():
    return render_template('exoplanetArchive.html')