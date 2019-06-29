from flask import Flask
from pymongo import MongoClient
from bson import json_util
import json
app = Flask(__name__)

class User:
    name = ""
    phone = ""
    id = ""

class Response:
    def __init__(self, success):
        self.success = success

@app.route('/example')
def hello():
    return "Hello World!"

@app.route('/register/<name>/<phone>')
def register(name, phone):
    client = MongoClient('mongo', 27017)
    db = client.data
    db.user.insert_one({
        "name": name,
        "phone": phone
        })
    client.close()
    response = Response(True)
    json_projects = json.dumps(response.__dict__, default=lambda o: o.__dict__, indent=4)
    return json_projects

@app.route("/db")
def checkDatabase():
    client = MongoClient('mongo', 27017)
    db = client.data
    collection = db.user
    findUser = collection.find()
    json_projects = []
    for u in findUser:
        user = User()
        user.name = u['name']
        user.phone = u['phone']
        user.id = str(u['_id'])
        json_projects.append(user)
    
    json_projects = json.dumps(json_projects, default=lambda o: o.__dict__, indent=4)
    client.close()
    return json_projects

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)