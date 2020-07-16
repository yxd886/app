import pymongo
import database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
collection_names = ["userlist","fmex"]


if __name__ == '__main__':

    for name in collection_names:
        mycol = mydb[name]
        mycol.create_index("username",unique=True)