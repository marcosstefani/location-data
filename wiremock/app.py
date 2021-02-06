from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/location')
def hello_world():
    data = {"depots": [ {"x": 12.3, "y":1.0, "label": "Voorburg", "size":200 }, {"x": 80.3, "y":-10.0, "label": "Altdorf", "size": 1000}, {"x": -20.3, "y":-70.0, "label": "Marienburg", "size":50, "metadata":"decomissioned" } ],
            "landmarks": [{"x": 10.3, "y":0.0, "label": "Jacob's House"}, {"x": 70.2, "y":-11.0}, {"x": 90.5, "y":11.0, "metadata":"outdated"}]}
    return jsonify(data)
