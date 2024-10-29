from flask import request, Flask
import json, socket
import computeEngine 

#import hashlib,random


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is backend  ! ' + str(socket.gethostname()) + ' \n'

@app.route("/joke", methods=["GET"])
def joke():
    hostName = socket.gethostname()

    bc = computeEngine.BackendCompute(hostName)
    random_joke = bc.get_a_joke()

    returnDictionary = {}
    returnDictionary["hostname"] = hostName
    returnDictionary["randomjoke"] = random_joke
    
    return json.dumps(returnDictionary)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
