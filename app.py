from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.router("/api/hello")
def hello( ):
    return jsonify(message="Hay from Flask")