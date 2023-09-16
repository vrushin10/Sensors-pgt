# from flask import Flask, request, json, Response
import json
# from bson import ObjectId
# from pymongo import MongoClient
import uuid
import firebase_admin
import firebase_admin.firestore as firestore
from firebase_admin import credentials 
from fastapi import FastAPI
from fastapi.responses import Response
# import uvicorn 
from pydantic import BaseModel
import model


cred = credentials.Certificate("./bullet-detection-vest-firebase-adminsdk-a8mkk-8874ac4eb9.json")
firebase_admin.initialize_app(cred)

app = FastAPI()


   

# Configuration (You can move this to a config file or use environment variables)
# MONGO_URI = "mongodb+srv://Back_end:Back_end@cluster0.uismmhb.mongodb.net/?retryWrites=true&w=majority"
# DATABASE_NAME = "Sensor_project"
# COLLECTION_NAME = "water_quality"


# class MongoAPI:
#     def __init__(self):
#         self.client = MongoClient(MONGO_URI)
#         self.db = self.client[DATABASE_NAME]
#         self.collection = self.db[COLLECTION_NAME]

#     def read(self):
#         documents = self.collection.find()
#         output = [{**data, "_id": str(data["_id"])} for data in documents]
#         return output

#     def read_filter(self, filter):
#         documents = self.collection.find(filter=filter)
#         output = [{**data, "_id": str(data["_id"])} for data in documents]
#         return output

#     def write(self, data):
#         new_document = data["Document"]
#         response = self.collection.insert_one(new_document)
#         output = {
#             "Status": "Successfully Inserted",
#             "Document_ID": str(response.inserted_id),
#         }
#         return output

#     def update(self, filter_data, update_data):
#         response = self.collection.update_one(
#             filter_data, {"$set": update_data})
#         output = {
#             "Status": "Successfully Updated"
#             if response.modified_count > 0
#             else "Nothing was updated."
#         }
#         return output

#     def delete(self, filter_data):
#         response = self.collection.delete_one(filter_data)
#         output = {
#             "Status": "Successfully Deleted"
#             if response.deleted_count > 0
#             else "Document not found."
#         }
#         return output



class Firebase:
    
    def __init__(self) -> None:
        db = firestore.client()
        self.connection = db.collection("vests")
        
    def create_document(self,document):
        document_id = uuid.uuid4()
        doc_ref = self.connection.document(str(document_id))
        doc_ref.set(document)
        
    def read_all_document(self):
        # doc_ref = self.connection.document()
        docs = self.connection.stream()
        result = [{**doc.to_dict(),"id":doc.id} for doc in docs]
        return result
           
    def read_document(self, document_id):
        doc_ref = self.connection.document(document_id)
        document = doc_ref.get()
        if document.exists:
            result = document.to_dict()
            print('Document data:', result)
            return result
        else:
            print('No such document!')

    def update_document(self, document_id,updates):
        doc_ref = self.connection.document(document_id)
        doc_ref.update(updates)
        
    def delete_document(self, document_id):
        doc_ref = self.connection.document(document_id)
        doc_ref.delete()
        

@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/firebase")
def db_read():
    obj1 = Firebase()
    response = obj1.read_all_document()
    return Response(content=json.dumps(response))

@app.get("/firebase/id")
def mongo_read_id(body:model.dbGet_id):
    obj1 = Firebase()
    response = obj1.read_document(body._id)
    if len(response) > 1:
        raise RuntimeError()
    return response[0]
    
@app.post("/firebase")
def mongo_write(body:model.dbPost):
    if body.values == {} or body.values == None:
          return Response(content=json.dumps({"Error": "Invalid input data"}), status_code=400, media_type="application/json")
    obj1 = Firebase()
    obj1.create_document(body.values.model_dump())
    return Response(content=json.dumps({"success":"a document was created","documnet":body.values.model_dump()}), status_code=200, media_type="application/json")

# @app.put("/firebase")
# def mongo_update_filter(body:model.dbUpdate):
#     if body.filter == {} or body.filter == None or body.filter == "":
#         return Response(response=json.dumps({"Error": "Invalid filter"}), status=400, mimetype="application/json")
#     obj1 = Firebase()
#     response = obj1.update(filter_data=body.filter,update_data=body.updateValues)
#     return Response(response=json.dumps(response[0]), status=200, mimetype="application/json")

@app.put("/firebase/id")
def mongo_update_id(body:model.dbUpdate_id):
    if body._id == None or body._id == "":
        return Response(response=json.dumps({"Error": "Invalid filter"}), status=400, mimetype="application/json")
    obj1 = Firebase()
    response = obj1.update_document(body.iD,body.updateValues)
    return Response(response=json.dumps(response[0]), status=200, mimetype="application/json")

@app.delete("/firebase/id")
def mongo_delete_filter(body:model.dbDelete):
    if body.filter == {} or body.filter == None or body.filter == "":
        return Response(response=json.dumps({"Error": "Invalid filter"}), status=400, mimetype="application/json")
    obj1 = Firebase()
    response = obj1.delete_document(body.iD)
    return Response(response=json.dumps(response[0]), status=200, mimetype="application/json")
    
# @app.delete("/mongodb/id")
# def mongo_update_filter(body:model.dbDelete_id):
#     if body._id == None or body._id == "":
#         return Response(response=json.dumps({"Error": "Invalid filter"}), status=400, mimetype="application/json")
#     obj1 = Firebase()
#     response = obj1.delete(filter_data=filter)
#     return Response(response=json.dumps(response[0]), status=200, mimetype="application/json")
    

