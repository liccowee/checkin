from flask import Flask
from pymongo import MongoClient
from bson import json_util
import json
app = Flask(__name__)


@app.route('/example')
def hello():
    return "Hello World!"

@app.route("/db")
def checkDatabase():
    client = MongoClient('mongo', 27017)
    db = client.data
    collection = db.user
    json_projects = []
    json_projects = json.dumps(collection.find_one(), default=json_util.default)
    client.close()
    return json_projects

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)