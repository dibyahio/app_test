import flask
import json
import requests 

app = flask.Flask(__name__, template_folder="Templates")
@app.route('/', methods =['POST', 'GET'])
def home():
    return "Hello from Flask"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)