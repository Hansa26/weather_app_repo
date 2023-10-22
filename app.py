from flask import Flask, render_template, request, jsonify
import requests
import json


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/weather_app", methods=['POST'])
def consume_weather_data():
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    city = request.json["city"]
    units = request.json["units"]
    appid = request.json["appid"]
    
    parameter = {
        'q': city,
        'units': units,
        'appid': appid
    }

    response = requests.get(url=url, params=parameter)

    json_data = response.json()

    return jsonify(f"Data: {json.dumps(json_data)}")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)