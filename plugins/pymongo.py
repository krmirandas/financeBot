import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["db"]

mycol = mydb["ciudades"]

for x in mycol.find():
  print(x)