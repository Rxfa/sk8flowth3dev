import time,os
from er1 import *
from er2 import *
from er3 import *
from er4 import *

from queue import Queue
from threading import Thread

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
        er1speed1.start()
        er1HS.start()
        er1afc1_.start()
        er1afc2_.start()
    elif idin == 'ER1' and ricin == 0:
        ER1.SSPCM_Init()
        if ER1.RIC['powered'] == 1 and ER1.AAA['powered'] == 1:
            print('ER1 fully Powered')
        else: 
            print('error with ER1 power Channel')
        time.sleep(3)
        start_ER_RACK(q_er1HS,er1hs)
        start_ER_RACK(q_er1HS,er1hsmon)
        start_ER_RACK(q_er1aaa,er1aaaspeed)
        start_ER_RACK(q_er1aaa,er1aaaspeedmon)
        start_ER_RACK(q_er1afc1,er1afc1speed)
        start_ER_RACK(q_er1afc1,er1afc1speedmon)
        start_ER_RACK(q_er1afc2,er1afc2speed)
        start_ER_RACK(q_er1afc2,er1afc2speedmon)
        er1_.start()
        er1speed1.start()
        er1HS.start()
        er1afc1_.start()
        er1afc2_.start()
    if idin == 'ER2' and ricin == 1:
        start_ER_RACK(q_er2HS,er1hs)
        start_ER_RACK(q_er2HS,er1hsmon)
        start_ER_RACK(q_er2aaa,er1aaaspeed)
        start_ER_RACK(q_er2aaa,er1aaaspeedmon)
        start_ER_RACK(q_er2afc1,er1afc1speed)
        start_ER_RACK(q_er2afc1,er1afc1speedmon)
        start_ER_RACK(q_er2afc2,er1afc2speed)
        start_ER_RACK(q_er2afc2,er1afc2speedmon)
        er2_.start()
        er2speed2.start()
        er1HS.start()
        er1afc1_.start()
        er1afc2_.start()
    elif idin == 'ER2' and ricin == 0:
        ER2.SSPCM_Init()
        if ER2.RIC['powered'] == 1 and ER2.AAA['powered'] == 1:
            print('ER2 fully Powered')
        else: 
            print('error with ER2 power Channel')
        time.sleep(3)
        start_ER_RACK(q_er2HS,er1hs)
        start_ER_RACK(q_er2HS,er1hsmon)
        start_ER_RACK(q_er2aaa,er1aaaspeed)
        start_ER_RACK(q_er2aaa,er1aaaspeedmon)
        start_ER_RACK(q_er2afc1,er1afc1speed)
        start_ER_RACK(q_er2afc1,er1afc1speedmon)
        start_ER_RACK(q_er2afc2,er1afc2speed)
        start_ER_RACK(q_er2afc2,er1afc2speedmon)
        er2_.start()
        er2speed2.start()
        er2HS.start()
        er2afc1_.start()
        er2afc2_.start()


ERRIC(ER1.rack_id,ER1.RIC['powered'])
ERRIC(ER2.rack_id,ER2.RIC['powered'])

