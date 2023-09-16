from flask import Flask, request, json, Response
from bson import ObjectId
from pymongo import MongoClient
    
app = Flask(__name__)

# Configuration (You can move this to a config file or use environment variables)
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "Sensor_project"
COLLECTION_NAME = "water_quality"


class MongoAPI:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def read(self):
        documents = self.collection.find()
        output = [{**data, "_id": str(data["_id"])} for data in documents]
        return output

    def read(self, filter):
        documents = self.collection.find(filter=filter)
        output = [{**data, "_id": str(data["_id"])} for data in documents]
        return output

    def write(self, data):
        new_document = data["Document"]
        response = self.collection.insert_one(new_document)
        output = {
            "Status": "Successfully Inserted",
            "Document_ID": str(response.inserted_id),
        }
        return output

    def update(self, filter_data, update_data):
        response = self.collection.update_one(
            filter_data, {"$set": update_data})
        output = {
            "Status": "Successfully Updated"
            if response.modified_count > 0
            else "Nothing was updated."
        }
        return output

    def delete(self, filter_data):
        response = self.collection.delete_one(filter_data)
        output = {
            "Status": "Successfully Deleted"
            if response.deleted_count > 0
            else "Document not found."
        }
        return output


@app.route("/")
def base():
    return Response(response=json.dumps({"Status": "UP"}), status=200, mimetype="application/json")


@app.route("/mongodb", methods=["GET"])
def mongo_read():
    obj1 = MongoAPI()
    response = obj1.read()
    return Response(response=json.dumps(response), status=200, mimetype="application/json")


@app.route("/mongodb/<id>", methods=["GET"])
def mongo_read_id(id):
    obj1 = MongoAPI()
    filter_data = {"_id": ObjectId(id)}
    response = obj1.read(filter_data)[0]
    if len(response) > 1:
        raise RuntimeError()
    return Response(response=json.dumps(response), status=200, mimetype="application/json")


@app.route("/mongodb", methods=["POST"])
def mongo_write():
    data = request.json
    if data is None or data == {} or "Document" not in data:
        return Response(response=json.dumps({"Error": "Invalid input data"}), status=400, mimetype="application/json")
    obj1 = MongoAPI()
    response = obj1.write(data)
    return Response(response=json.dumps(response), status=200, mimetype="application/json")


@app.route("/mongodb/<id>", methods=["PUT"])
def mongo_update(id):
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Invalid input data"}), status=400, mimetype="application/json")
    filter_data = {"_id": ObjectId(id)}
    obj1 = MongoAPI()
    response = obj1.update(filter_data, data)
    return Response(response=json.dumps(response), status=200, mimetype="application/json")


@app.route("/mongodb/<id>", methods=["DELETE"])
def mongo_delete(id):
    filter_data = {"_id": ObjectId(id)}
    obj1 = MongoAPI()
    response = obj1.delete(filter_data)
    return Response(response=json.dumps(response), status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0")
