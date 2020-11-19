import random

def execute(*args):
    diccionario = {
        'card': 'www.bbva.como/tarjetas',
        'direction': 'www.bbva.como/dirección',
        'credit': 'www.bbva.como/credit'
    }
    var=args[0]
    opt=args[1]
    print(var)
    print(opt)
    msg = 'Por favor, entra al siguiente link : \n' + diccionario[opt]
    return 'set_slot {0} "{1}"'.format(var,msg)

