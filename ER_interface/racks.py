import time,os,socket
from er1 import *
from er2 import *
from er3 import *
from er4 import *

from queue import Queue
from threading import Thread

timeout = 0
def start_ER_RACK(q,rackmode):
    test11 = Thread(target=rackmode,args=(q,))
    test11.start()

#rack_HS()

def ERRIC(idin,ricin):
    if idin == 'ER1' and ricin == 1:
        start_ER_RACK(q_er1HS,er1hs)
        start_ER_RACK(q_er1HS,er1hsmon)
        start_ER_RACK(q_er1aaa,er1aaaspeed)
        start_ER_RACK(q_er1aaa,er1aaaspeedmon)
        start_ER_RACK(q_er1afc1,er1afc1speed)
        start_ER_RACK(q_er1afc1,er1afc1speedmon)
        start_ER_RACK(q_er1afc2,er1afc2speed)
        start_ER_RACK(q_er1afc2,er1afc2speedmon)
        
    elif idin == 'ER1' and ricin == 0:
        #ER1.SSPCM_Init()
        #time.sleep(3)
        start_ER_RACK(q_er1HS,er1hs)
        start_ER_RACK(q_er1HS,er1hsmon)
        start_ER_RACK(q_er1aaa,er1aaaspeed)
        start_ER_RACK(q_er1aaa,er1aaaspeedmon)
        start_ER_RACK(q_er1afc1,er1afc1speed)
        start_ER_RACK(q_er1afc1,er1afc1speedmon)
        start_ER_RACK(q_er1afc2,er1afc2speed)
        start_ER_RACK(q_er1afc2,er1afc2speedmon)
    if idin == 'ER2' and ricin == 1:
        start_ER_RACK(q_er2HS,er1hs)
        start_ER_RACK(q_er2HS,er1hsmon)
        start_ER_RACK(q_er2aaa,er1aaaspeed)
        start_ER_RACK(q_er2aaa,er1aaaspeedmon)
        start_ER_RACK(q_er2afc1,er1afc1speed)
        start_ER_RACK(q_er2afc1,er1afc1speedmon)
        start_ER_RACK(q_er2afc2,er1afc2speed)
        start_ER_RACK(q_er2afc2,er1afc2speedmon)
        
    elif idin == 'ER2' and ricin == 0:
       # ER2.SSPCM_Init()
        #time.sleep(3)
        start_ER_RACK(q_er2HS,er1hs)
        start_ER_RACK(q_er2HS,er1hsmon)
        start_ER_RACK(q_er2aaa,er1aaaspeed)
        start_ER_RACK(q_er2aaa,er1aaaspeedmon)
        start_ER_RACK(q_er2afc1,er1afc1speed)
        start_ER_RACK(q_er2afc1,er1afc1speedmon)
        start_ER_RACK(q_er2afc2,er1afc2speed)
        start_ER_RACK(q_er2afc2,er1afc2speedmon)
    

HOST = '127.0.0.1'
PORT = 3333

def startup():
    ERRIC(ER1.rack_id,ER1.RIC['poweredric'])
    ERRIC(ER2.rack_id,ER2.RIC['poweredric'])

#startup()
#ERRIC(ER1.rack_id,ER1.RIC['powered'])
#ERRIC(ER2.rack_id,ER2.RIC['powered'])


