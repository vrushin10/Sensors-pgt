import requests
import json

def test_health_check():
    response = requests.get("http://localhost:5001/mongodb")
    print(response.raw)
    # assert response.status_code == 200
    # assert response.json()["Status"] == "UP"

def test_read():
    response = requests.get("http://localhost:5001/mongodb")
    assert response.status_code == 200
    assert response.json() == []

def test_write():
    data = {"Document": {"temperature": 25.5, "pH": 7.2}}
    response = requests.post("http://localhost:5001/mongodb", json=data)
    assert response.status_code == 200
    assert response.json()["Status"] == "Successfully Inserted"
    assert response.json()["Document_ID"] != ""

def test_update():
    data = {"Filter": {"temperature": 25.5}}
    data["DataToBeUpdated"] = {"pH": 7.3}
    response = requests.put("http://localhost:5001/mongodb", json=data)
    assert response.status_code == 200
    assert response.json()["Status"] == "Successfully Updated"

def test_delete():
    data = {"Filter": {"temperature": 25.5}}
    response = requests.delete("http://localhost:5001/mongodb", json=data)
    assert response.status_code == 200
    assert response.json()["Status"] == "Successfully Deleted"

if __name__ == "__main__":
    test_health_check()
    test_read()
    test_write()
    test_update()
    # test_delete()