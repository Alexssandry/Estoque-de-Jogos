# coding: utf-8
from flask import Flask
from api import BlueP_API

app = Flask(__name__)
app.register_blueprint(BlueP_API)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8083", use_reloader=True)
