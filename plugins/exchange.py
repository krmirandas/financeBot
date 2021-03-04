import os
import json
import pymongo
import datetime
import time
import requests
import io
import json

exchange_api = 'https://api.exchangeratesapi.io/latest'
base = '?'

# db request
content_exchange_api = None
data = None
myclient = None
mydb = None
mycol = None

def init_db(ex_api):
    global content_exchange_api
    global data
    global myclient
    global mydb
    global mycol
    content_exchange_api = requests.get(ex_api).content
    data = json.loads(content_exchange_api)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["financeBot"]
    mycol = mydb["currencies"]

def execute(*args):
    var = args[0]
    ex_coin = args[1].upper()
    coin = args[2].upper()
    msg = ''
    ex_api = exchange_api + base + 'base=' + coin
    init_db(ex_api)

    mydoc = mycol.find_one({"code": ex_coin})

    coin_data = mycol.find_one({"code": coin})
    ex_coin_data = mycol.find_one({"code": ex_coin})

    if mydoc is None:
        msg = "Ingresaste un acrónomo incorrecto"
        return 'set_slot {0} "{1}"'.format(var, msg)
    msg += "El valor actual de tu moneda {}({}) contra {}({}) es de {}".format(
        coin, coin_data['name'], ex_coin, ex_coin_data['name'], data['rates'][ex_coin])
    return 'set_slot {0} "{1}"'.format(var, msg)
