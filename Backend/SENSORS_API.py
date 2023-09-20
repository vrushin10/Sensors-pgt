import json
import uuid
import firebase_admin
import firebase_admin.firestore as firestore
from firebase_admin import credentials
from fastapi import FastAPI
from fastapi.responses import Response
import sensors_model as model
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate(
    "./bullet-detection-vest-firebase-adminsdk-a8mkk-8874ac4eb9.json")
firebase_admin.initialize_app(cred)

app = FastAPI()


class Firebase:

    def __init__(self,collection:str) -> None:
        db = firestore.client()
        self.connection = db.collection(collection)

    def create_document(self, document):
        document_id = uuid.uuid4()
        doc_ref = self.connection.document(str(document_id))
        doc_ref.set(document)

    def read_latest_document(self, id):
        doc_ref = self.connection.where(filter=FieldFilter("id","==",id)).order_by("timestamp", direction=firestore.Query.DESCENDING).limit(1)
        return doc_ref.to_dict()
        
    def read_all_document(self):
        # doc_ref = self.connection.document()
        docs = self.connection.stream()
        result = [{**doc.to_dict(), "id": doc.id} for doc in docs]
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

    def update_document(self, document_id, updates):
        doc_ref = self.connection.document(document_id)
        doc_ref.update(updates)

    def delete_document(self, document_id):
        doc_ref = self.connection.document(document_id)
        doc_ref.delete()

    def delete_all_document(self):
        doc_stream = self.connection.stream()
        for doc_ref in doc_stream:
            self.delete_document(doc_ref.id)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/firebase")
def db_read():
    obj1 = Firebase("Sensor_logs")
    response = obj1.read_all_document()
    return Response(content=json.dumps(response), media_type="application/json")


@app.get("/firebase/id")
def mongo_read_id(body: model.dbGet_id):
    obj1 = Firebase("Sensor_logs")
    response = obj1.read_document(body._id)
    if len(response) > 1:
        raise RuntimeError()
    return response[0]

@app.get("/firebase/vest")
def get_vests():
    obj1 = Firebase("nodes")
    response = obj1.read_all_document()
    return Response(content=json.dumps(response), media_type="application/json")

@app.get("/firebase/id")
def mongo_read_id(body: model.dbGet_id):
    obj1 = Firebase("Sensor_logs")
    response = obj1.read_document(body._id)
    if len(response) > 1:
        raise RuntimeError()
    return response[0]

@app.get("/RTI/all")
def RTI_all():
    obj1 = Firebase("Sensor_logs")
    obj2 = Firebase("nodes")
    response1 = obj2.read_all_document()
    res = []
    ids = []
    for vals in response1:
        ids.append(vals.get("id"))
    for id in ids:
        val = obj1.read_latest_document(id)
        res.append(val)
        
    print(ids,res)


@app.post("/firebase")
def mongo_write(body: model.dbPost):
    if body.values == {} or body.values == None:
        return Response(content=json.dumps({"Error": "Invalid input data"}), status_code=400, media_type="application/json")
    obj1 = Firebase("Sensor_logs")
    values = body.values.model_dump()
    obj1.create_document(values)
    return Response(content=json.dumps({"success": "a document was created", "documnet": values}), status_code=200, media_type="application/json")


@app.put("/firebase/id",)
def mongo_update_id(body: model.dbUpdate_id):
    if body.iD == None or body.iD == "":
        return Response(response=json.dumps({"Error": "Invalid filter"}), status=400, mimetype="application/json")
    obj1 = Firebase("Sensor_logs")
    values = body.updateValues.model_dump()
    print("before",values)
    for key in values.copy():
        if values[key] == "" or values[key] == None:
            values.pop(key)
    print("after",values)
    obj1.update_document(body.iD,values)
    return Response(content=f"successfuly updated document with id {body.iD}")


@app.delete("/firebase/id")
def mongo_delete_filter(body: model.dbDelete_id):
    obj1 = Firebase("Sensor_logs")
    obj1.delete_document(body.iD)
    return Response(content=f"successfuly deleted document with id {body.iD}", status=200)


@app.delete("/firebase/all")
def mongo_delete_all():
    obj1 = Firebase("Sensor_logs")
    obj1.delete_all_document()
    return "succesfully deleted all documents"
