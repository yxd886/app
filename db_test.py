import pymongo
import database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]


if __name__ == '__main__':

    #print(database.find_one_by_token("sites","5f0fb94b1ff4d6f7ff5ad67e"))
    print(database.insert_or_update("fmex",{"username":"test1"},{"username":"test1","key":"12","secret":"22"}))
    for x in mydb["fmex"].find():
        print(x)
