from flask import Flask, render_template
from service.location import LocationService

app = Flask(__name__)

@app.route("/")
def index():
    service = LocationService()
    return render_template('index.html', data=service.getData())
