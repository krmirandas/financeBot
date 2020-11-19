#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Kevin Miranda
# GPL 3.0

import datetime
import random

def execute(*args):
    now = datetime.datetime.now()

    var=args[0]
    msg = 'Buenos días'
    if (now.hour) > 12 and (now.hour) < 19:
        msg = 'Buenos tardes'
    if (now.hour) > 19:
        msg = 'Buenos noches'
    return 'set_slot {0} "{1}"'.format(var,msg)

