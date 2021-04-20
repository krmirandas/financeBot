import datetime
import io
import json
import os
import pymongo
import requests
import time

exchange_api = 'https://api.exchangerate.host/'

base = '?base='
amount = '&amount='

content_exchange_api = None
date = 'latest'
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
    msg = 'Pagando {} {}, obtendrías: {} {}'.format(val, coin, val_ret, ex_coin)
    return 'set_slot {0} "{1}"'.format(var, msg)

def get_dollar(*args):
    var = args[0]
    coin = args[1].upper()

    ex_api = exchange_api + date + base + coin
    init_db(ex_api)

    if coin not in currencies:
        msg = 'Ingresaste un acrónimo incorrecto.'
        return 'set_slot {0} "{1}"'.format(var, msg)

    msg = 'Tu moneda es {} '.format(coin)
    msg += 'Su valor actual frente al dolar es {} {}'.format(
        currencies['USD'], 'USD')
    return 'set_slot {0} "{1}"'.format(var, msg)
