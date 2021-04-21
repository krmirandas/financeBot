from datetime import datetime, timedelta
import io
import json
import os
import pymongo
import requests
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["financeBot"]
mycol = mydb["currencies"]

exchange_api = 'https://api.exchangerate.host/'

base = '?base='
amount = '&amount='

content_exchange_api = None
date = 'latest'  # yyyy-mm-dd
currencies = None


def init_db(ex_api):
    global content_exchange_api
    global date
    global currencies
    content_exchange_api = requests.get(ex_api).content
    data = json.loads(content_exchange_api)
    currencies = data['rates']


def execute(*args):
    var = args[0]
    ex_coin = args[1].upper()
    coin = args[2].upper()
    msg = ''
    ex_api = exchange_api + date + base + coin
    init_db(ex_api)

    if ex_coin not in currencies:
        msg = 'Ingresaste un acrónimo incorrecto.'
        return 'set_slot {0} "{1}"'.format(var, msg)
    val_coin = currencies[ex_coin]
    msg += 'El valor actual de tu moneda {} contra {} es de {}'.format(
        coin, ex_coin, val_coin)
    return 'set_slot {0} "{1}"'.format(var, msg)


def change(*args):
    var = args[0]
    ex_coin = args[1].upper()
    coin = args[2].upper()
    val = args[3]
    msg = ''
    ex_api = exchange_api + date + base + coin + amount + val
    init_db(ex_api)

    if ex_coin not in currencies:
        msg = 'Ingresaste un acrónimo incorrecto.'
        return 'set_slot {0} "{1}"'.format(var, msg)
    val_ret = currencies[ex_coin]
    msg = 'Pagando {} {}, obtendrías: {} {}'.format(
        val, coin, val_ret, ex_coin)
    return 'set_slot {0} "{1}"'.format(var, msg)


def get_dollar(*args):
    var = args[0]
    coin = args[1].upper()

    ex_api = exchange_api + date + base + coin
    init_db(ex_api)

    if coin not in currencies:
        msg = 'Ingresaste un acrónimo incorrecto.'
        return 'set_slot {0} "{1}"'.format(var, msg)
    coin_ = mycol.find_one({"code": coin})
    msg = 'Tu moneda es {},'.format(coin_['name'])
    msg += 'su valor actual frente al dolar es {} {}'.format(
        currencies['USD'], 'USD')
    return 'set_slot {0} "{1}"'.format(var, msg)


def recomend(*args):
    var = args[0]
    ex_coin = args[1].upper()
    coin = args[2].upper()
    msg = ''
    d1 = datetime.today() - timedelta(days=0)
    date = d1.strftime("%Y-%m-%d")
    ex_api = exchange_api + date + base + coin
    init_db(ex_api)
    val1 = currencies[ex_coin]

    d2 = datetime.today() - timedelta(days=1)
    date = d2.strftime("%Y-%m-%d")
    ex_api = exchange_api + date + base + coin
    init_db(ex_api)
    val2 = currencies[ex_coin]

    r = val2 - val1
    if r > 0:
        msg = 'Recomiendamos comprar {}'.format(ex_coin)
        return 'set_slot {0} "{1}"'.format(var, msg)
    else:
        msg = 'No recomiendamos comprar {}, tal vez mañana'.format(ex_coin)
        return 'set_slot {0} "{1}"'.format(var, msg)
