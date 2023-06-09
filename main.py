from flask import Flask, jsonify, request
import os

app = Flask(__name__)


def helloWorld():
    return "Hello World"


@app.route('/')
def index():
    return jsonify({"Choo Choo": helloWorld()})


@app.route('/twillio')
def Send_Text():
    return "Messaging User"


@app.route('/process_location', methods=['POST'])
def Capture_Location():
    data = request.get_json()
    lat = data['latitude']
    lng = data['longitude']
    return "Current Location... Lat:", lat, "\tLong:", lng


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
