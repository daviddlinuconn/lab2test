import requests

import requests
from flask import Flask, request
from flask_cors import CORS, cross_origin
#
# pip3 install flask, requests, flask_cors
#
#

#
#
url = 'http://localhost:8080/joke'


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#
# 
# curl http://localhost:5000/get
#
@app.route("/get")
def hello_world():
    response = requests.get(url,headers={'Content-type': "application/json"}, stream=True)
    data =response.raw.read()
    print(data,response)
    return data

# curl http://localhost:5000/joke
@app.route("/joke")
def joke():
    response = requests.get(url,headers={'Content-type': "application/json"}, stream=True)
    data = response.raw.read()
    print(data,response)
    return data
if __name__=="__main__":
    app.run(port=5000, debug=True)
