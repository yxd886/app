import requests
from bson.objectid import ObjectId

def test_login():
    data = {"username":"test11",
            "password":"aaaaaa"}

    rep = requests.post("http://localhost/api/user/login",data=data)
    print(rep.json())


def test_api_config():
    data = {"username": "test11",
            "password": "aaaaaa"}

    rep = requests.post("http://localhost/api/user/login", data=data)
    token = rep.json()["data"]["token"]
    data = {"type": 1,
            "key": "aaaaaa",
            "secret":"bbbbbb"}
    rep = requests.post("http://localhost/api/exchange/apiconfig", data=data)
    print(rep.json())
test_api_config()