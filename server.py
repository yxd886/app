from flask import Flask
from flask import request
from flask import jsonify
import threading
import database

app = Flask(__name__)
app.config["DEBUG"] = True
collection_name = "userlist"
api_collection_names = ["aaa","fmex"]
@app.route('/api/user/register', methods=[ 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username",default = None)
        password = request.form.get("password",default = None)
        if(not username or not password or username=="" or password==""):
            req = {
                "code": "0001",
                "result": "用户名或密码格式错误",
                "data": {}
            }
            return jsonify(req)
        print(request.form)
        status,msg = database.register(collection_name,{"username":username,"password":password})
        if status==True:
            req = {
                "code": "0000",
                "result": "注册成功",
                "data": {"username":username,"token":str(msg)}
            }
            return jsonify(req)
        else:
            req = {
                "code": "0001",
                "result": msg,
                "data": {}
            }
            return jsonify(req)
@app.route('/api/user/login', methods=[ 'POST'])
def login():
    username = request.form.get("username", default=None)
    password = request.form.get("password", default=None)
    if (not username or not password or username == "" or password == ""):
        req = {
            "code": "0001",
            "result": "用户名或密码格式错误",
            "data": {}
        }
        return jsonify(req)
    print(request.form)
    ret = database.find_one(collection_name,{"username":username,"password":password})
    if ret==None:
        req = {
            "code": "0001",
            "result": "用户名或密码错误",
            "data": {}
        }
        return jsonify(req)
    else:
        req = {
            "code": "0000",
            "result": "登陆成功",
            "data": {"username":ret["username"],"token":str(ret["_id"])}
        }
        return jsonify(req)






@app.route('/api/exchange/apiconfig', methods=[ 'POST'])
def apiconfig():
    token = request.headers.get("token",default=None)
    if token==None or len(token)!=24:
        req = {
            "code": "0001",
            "result": "授权过期",

        }
        return jsonify(req)
    ret = database.find_one_by_token(collection_name,token)
    if ret==None:
        req = {
            "code": "0001",
            "result": "授权过期",

        }
        return jsonify(req)
    username = ret["username"]
    exchange_index = int(request.form.get("type",default=0))
    api_key = request.form.get("key",default=0)
    api_secret = request.form.get("secret",default=0)

    if exchange_index==0 or exchange_index>=len(api_collection_names):
        req = {
            "code": "0001",
            "result": "配置失败，交易所选择错误",

        }
        return jsonify(req)
    collection = api_collection_names[exchange_index]
    database.insert_or_update(collection,{"username:":username},{"username":username,"key":api_key,"secret":api_secret})
    req = {
        "code": "0000",
        "result": "配置成功",

    }
    return jsonify(req)


app.run(port=80)
