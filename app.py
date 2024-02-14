import flask
import json
import requests 
import postgres

app = flask.Flask(__name__, template_folder="Templates")
@app.route('/', methods =['POST', 'GET'])
def home():
    return "Hello from Flask"

@app.route('/postgres_sm', methods =['POST', 'GET'])
def small_query():
    sql ="""
    select * from ecommerce.subscription_products
"""
    if flask.request.method == 'POST':
        res,err=postgres.postgres_connect(sql,commit=0)
        print(res)
        return flask.jsonify({'msg':res}),200
    else:
        return flask.jsonify({'msg':"error"}),400

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)