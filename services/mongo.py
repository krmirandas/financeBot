import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["financeBot"]
mycol = mydb["currencies"]

f = open('currencies.json',)
data = json.load(f)

mydict = []

for i in data:
    mydict.append(data[i])


x = mycol.insert_many(mydict)


mydoc = mycol.find_one({"code": "MXN"})
print(mydoc)