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

# Should be access only for ADMIN. So only admin can check in user. Need to send user id as params for check in user
@app.route('/checkin', methods=['POST'])
def checkin():
    return "Checking in User"

# Should be access only for ADMIN. So only admin can check out user.
@app.route('/checkout', methods=['POST'])
def checkout():
    return "Checking out User"

# Should be return all the history for the requested access token
@app.route('/history', methods=['GET'])
def history():
    return "Get all history session of user"

# Should be return user profile if I query with access token. User profile data such as User ID
@app.route('/profile', methods=['GET'])
def profile():
    return "Get user profile such as Profile ID, phone number and name"

# This /register api service should be in POST method. Need to change it!
# should also return access token so web know it is from which user
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

# This /example is for sample purpose. Need to remove in future!
@app.route('/example')
def hello():
    return "Hello World!"

# This /db is for sample purpose. Need to remove in future!
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