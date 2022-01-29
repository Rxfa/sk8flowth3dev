import time,os
from er1 import *
from er2 import *

from queue import Queue
from threading import Thread

def start_ER_RACK(q,rackmode):
    test11 = Thread(target=rackmode,args=(q,))
    test11.start()

#rack_HS()

start_ER_RACK(q_er1HS,er1hs)
start_ER_RACK(q_er1HS,er1hsmon)
start_ER_RACK(q_er1aaa,er1speed)
start_ER_RACK(q_er1aaa,er1speedmon)

start_ER_RACK(q_er2HS,er2hs)
start_ER_RACK(q_er2HS,er2hsmon)
start_ER_RACK(q_er2aaa,er2speed)
start_ER_RACK(q_er2aaa,er2speedmon)

