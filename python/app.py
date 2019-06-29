from flask import Flask
from pymongo import MongoClient
from bson import json_util
import json
app = Flask(__name__)

class User:
    name = ""
    phone = ""
    id = ""

@app.route('/example')
def hello():
    return "Hello World!"

@app.route("/db")
def checkDatabase():
    client = MongoClient('mongo', 27017)
    db = client.data
    collection = db.user
    findUser = collection.find_one()
    user = User()
    user.name = findUser['name']
    user.phone = findUser['phone']
    user.id = str(findUser['_id'])
    json_projects = []
    json_projects = json.dumps(user.__dict__, default=lambda o: o.__dict__, indent=4)
    client.close()
    return json_projects

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)