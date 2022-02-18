#!/usr/bin/python3
"""Module of the APP configuration"""

from flask import render_template, Flask, jsonify
import requests
import json
app = Flask(__name__)


@app.route('/')
@app.route("/index", methods=["GET"], strict_slashes=False)
def index():
    return "hola sandra"


@app.errorhandler(404)
def error(err):
    """Return error for this page"""
    return jsonify({"error": "Not found"}), 404


@app.route('/search/<city>')
def search(city):
    # city = "cali"
    # country = "co"

    weather_key = "e38dee21365bc28fe6e0d042d0de40ec"
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
        city, weather_key)

    req = requests.get(url).json()
    if req.status_code == 200:
        # get main weather dict from request
        weather_dict = req.get('main')
        # get temperature and feels like temperature
        dict_return = {'news': [], 'weather': {}}
        dict_return['weather']['name'] = req.get('name')
        dict_return['weather']['country'] = req.get('sys').get('country')
        dict_return['weather']['temperature'] = weather_dict.get('temp') - 276.15
        dict_return['weather']['feels_like'] = weather_dict.get(
            'feels_like') - 276.15
        dict_return['weather']['humidity'] = weather_dict.get('humidity')
        dict_return['weather']['pressure'] = weather_dict.get('pressure')
        dict_return['weather']['visibility'] = req.get('visibility') / 1000
        dict_return['weather']['weather_description'] = req.get('weather')[0].get('description')
    else:
        {'error':'city not found'}
        # print(temperature)


    # new
    # title
    # url image
    # published at
    # description
    # url noticia
    with open("info.json", "w") as jsonfile:
        json.dump(dict_return, jsonfile)
    return dict_return


if __name__ == '__main__':

    app.run(port='5000', debug=True)
