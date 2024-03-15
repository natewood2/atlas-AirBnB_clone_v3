#!/usr/bin/python3
"""Module containing API engine"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

if 'HBNB_API_HOST' in os.environ:
    host = getenv('HBNB_API_HOST')
else:
    host = '0.0.0.0'
if 'HBNB_API_PORT' in os.environ:
    port = getenv('HBNB_API_PORT')
else:
    port = 5000

app = Flask(__name__)
app.register_blueprint(app_views)


@app.route('/status', strict_slashes=False)
def status():
    return response


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)