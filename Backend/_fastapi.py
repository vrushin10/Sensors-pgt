# from flask import Flask, request, json, Response
import json
from bson import ObjectId
from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.responses import Response
import uvicorn 
from pydantic import BaseModel
import model

app = FastAPI()


   

# Configuration (You can move this to a config file or use environment variables)
MONGO_URI = "mongodb+srv://Back_end:Back_end@cluster0.uismmhb.mongodb.net/?retryWrites=true&w=majority"
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

    def read_filter(self, filter):
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


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/mongodb")
def db_read():
    obj1 = MongoAPI()
    response = obj1.read()
    return Response(content=json.dumps(response))

@app.get("/mongodb")
def mongo_read_id(body:model.dbGet_id):
    obj1 = MongoAPI()
    filter_data = {"_id": ObjectId(body._id)}
    response = obj1.read_filter(filter_data)
    if len(response) > 1:
        raise RuntimeError()
    return response[0]
    
  

@app.post("/mongodb")
def mongo_write(body:model.dbPost):
    if body.values == {} or body.values == None:
          return Response(response=json.dumps({"Error": "Invalid input data"}), status=400, mimetype="application/json")
    obj1 = MongoAPI()
    response = obj1.write(body.values)
    return Response(response=json.dumps(response), status=200, mimetype="application/json")



@app.put("/mongodb/filter")
def mongo_update_filter(body:model.dbUpdate):
    if body.filter == {} or body.filter == None or body.filter == "":
        return Response(response=json.dumps({"Error": "Invalid filter"}), status=400, mimetype="application/json")
    obj1 = MongoAPI()
    response = obj1.update(filter_data=body.filter,update_data=body.updateValues)
    return Response(response=json.dumps(response[0]), status=200, mimetype="application/json")
    
@app.put("/mongodb/id")
def mongo_update_filter(body:model.dbUpdate_id):
    if body._id == None or body._id == "":
        return Response(response=json.dumps({"Error": "Invalid filter"}), status=400, mimetype="application/json")
    filter = {"_id": ObjectId(id)}
    obj1 = MongoAPI()
    response = obj1.update(filter_data=filter,update_data=body.updateValues)
    return Response(response=json.dumps(response[0]), status=200, mimetype="application/json")
    


@app.delete("/mongodb/filter")
def mongo_update_filter(body:model.dbDelete):
    if body.filter == {} or body.filter == None or body.filter == "":
        return Response(response=json.dumps({"Error": "Invalid filter"}), status=400, mimetype="application/json")
    obj1 = MongoAPI()
    response = obj1.delete(filter_data=body.filter)
    return Response(response=json.dumps(response[0]), status=200, mimetype="application/json")
    
@app.delete("/mongodb/id")
def mongo_update_filter(body:model.dbDelete_id):
    if body._id == None or body._id == "":
        return Response(response=json.dumps({"Error": "Invalid filter"}), status=400, mimetype="application/json")
    filter = {"_id": ObjectId(id)}
    obj1 = MongoAPI()
    response = obj1.delete(filter_data=filter)
    return Response(response=json.dumps(response[0]), status=200, mimetype="application/json")
    

