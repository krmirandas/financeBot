#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Kevin Miranda
# GPL 3.0

import os
import json
import pymongo
import datetime
import time
import requests
import io
import json

exchange_api = "https://api.exchangeratesapi.io/latest"

content_exchange_api = requests.get(exchange_api).content

data = loaded_json = json.loads(content_exchange_api)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["financeBot"]
mycol = mydb["currencies"]
mydoc = mycol.find_one({"code": "MXN"})


def execute(*args):
    var = args[0]
    opts = args[1]
    mydoc = mycol.find_one({"code": opts})
    msg = "Tu moneda es {}. ".format(mydoc['name'])
    msg += "Su valor actual frente al dolar es {}{}".format(
        mydoc['code'], round(data['rates'][opts], 2))
    return 'set_slot {0} "{1}"'.format(var, msg)
