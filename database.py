import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
def register(collection,content):
    mycol = mydb[collection]
    try:
        id = mycol.insert(content)
        return True, id

    except Exception as e:
        print(e)
        if "dup key" in str(e):
            return False, "用户名已存在"


def find_one(collection,content):
    mycol = mydb[collection]
    return mycol.find_one(content)

def find_one_by_token(collection,token):
    mycol = mydb[collection]
    return mycol.find_one({"_id":ObjectId(token)})



def insert_or_update(collection,key,content):
    mycol = mydb[collection]
    return mycol.replace_one(key, content, upsert=True)
