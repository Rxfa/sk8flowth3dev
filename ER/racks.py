from telnetlib import SSPI_LOGON
import time,os,socket
from er1 import *
from er2 import *
from er3 import *
from er4 import *

from queue import Queue
from threading import Thread

lineup = []

def start_ER_RACK(q,rackmode):
    test11 = Thread(target=rackmode,args=(q,))
    test11.start()

#rack_HS()
def ERRIC(idin,ricin):
    if idin == 'ER1' and ricin == 1:
        print('ER1 RIC active')
        ER1.SSPCM_Init()
        start_ER_RACK(q_er1HS,er1hs)
        start_ER_RACK(q_er1HS,er1hsmon)
        start_ER_RACK(q_er1afc2,er1afc2flow)
        start_ER_RACK(q_er1afc2,er1afc2flowmon)
        start_ER_RACK(q_er1aaa,er1AAA)
        start_ER_RACK(q_er1aaa,er1AAAmon)
        er1HS.start()
        er1aaa.start()
        er1_afc2_flow.start()

    elif idin == 'ER1' and not ricin:
        #print(f"RIC flag {ER1.RIC}")
        print('Loading ER1 RIC')
        
        start_ER_RACK(q_er1HS,er1hs)
        start_ER_RACK(q_er1HS,er1hsmon)
        start_ER_RACK(q_er1afc2,er1afc2flow)
        start_ER_RACK(q_er1afc2,er1afc2flowmon)
        start_ER_RACK(q_er1aaa,er1AAA)
        start_ER_RACK(q_er1aaa,er1AAAmon)
        er1HS.start()
        er1aaa.start()
        er1_afc2_flow.start()
        time.sleep(1)
        if ER1.AAA['Powered'] == 1 and ER1.RIC['Powered'] == 1 :
            print('RIC powered')
            ER1.er_AAAspeed_gen(ER1.AAA['fanSpeed'])
            print('fan started')
        else: print(f"check rack config!!!!!!!!!! {ER1.RIC['Powered']}");time.sleep(2)

    if idin == 'ER2' and ricin:
        print('ER2 RIC active')
        start_ER_RACK(q_er2HS,er1hs)
        start_ER_RACK(q_er2HS,er1hsmon)
        start_ER_RACK(q_er2afc2,er1afc2flow)
        start_ER_RACK(q_er2afc2,er1afc2flowmon)
        start_ER_RACK(q_er2aaa,er1AAA)
        start_ER_RACK(q_er2aaa,er1AAAmon)
        

    elif idin == 'ER2' and not ricin:
        print(f"RIC flag {ER2.RIC}")
        print('Loading ER2 RIC')
        ER2.SSPCM_Init()
        start_ER_RACK(q_er2HS,er1hs)
        start_ER_RACK(q_er2HS,er1hsmon)
        start_ER_RACK(q_er2afc2,er1afc2flow)
        start_ER_RACK(q_er2afc2,er1afc2flowmon)
        start_ER_RACK(q_er2aaa,er1AAA)
        start_ER_RACK(q_er2aaa,er1AAAmon)

    if idin == 'ER3' and ricin:
        print('ER3 RIC active')
        start_ER_RACK(q_er3HS,er1hs)
        start_ER_RACK(q_er3HS,er1hsmon)
        start_ER_RACK(q_er3afc2,er1afc2flow)
        start_ER_RACK(q_er3afc2,er1afc2flowmon)
        start_ER_RACK(q_er3aaa,er1AAA)
        start_ER_RACK(q_er3aaa,er1AAAmon)

    elif idin == 'ER3' and not ricin:
        print(f"RIC flag {ER3.RIC}")
        print('Loading ER3 RIC')
        ER3.SSPCM_Init()
        start_ER_RACK(q_er3HS,er1hs)
        start_ER_RACK(q_er3HS,er1hsmon)
        start_ER_RACK(q_er3afc2,er1afc2flow)
        start_ER_RACK(q_er3afc2,er1afc2flowmon)
        start_ER_RACK(q_er3aaa,er1AAA)
        start_ER_RACK(q_er3aaa,er1AAAmon)

    if idin == 'ER4' and ricin:
        print('ER4 RIC active')
        start_ER_RACK(q_er4HS,er1hs)
        start_ER_RACK(q_er4HS,er1hsmon)
        start_ER_RACK(q_er4afc2,er1afc2flow)
        start_ER_RACK(q_er4afc2,er1afc2flowmon)
        start_ER_RACK(q_er4aaa,er1AAA)
        start_ER_RACK(q_er4aaa,er1AAAmon)

    elif idin == 'ER4' and not ricin:
        print(f"RIC flag {ER4.RIC}")
        print('Loading ER4 RIC')
        ER4.SSPCM_Init()
        start_ER_RACK(q_er4HS,er1hs)
        start_ER_RACK(q_er4HS,er1hsmon)
        start_ER_RACK(q_er4afc2,er1afc2flow)
        start_ER_RACK(q_er4afc2,er1afc2flowmon)
        start_ER_RACK(q_er4aaa,er1AAA)
        start_ER_RACK(q_er4aaa,er1AAAmon)

HOST = '127.0.0.1'
PORT = 3333
# Configure socket connection
z = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
z.connect((HOST, PORT))

# Wake up
z.send('keepalive'.encode())

while True:
    try:
        data = z.recv(1024)
    except: print('something went wrong')

    if data.decode().__contains__('activate'):
        step = data.decode()[9:12]
        print(f"activate cmd received for {step}")
        if step == 'ER1': 
            ERRIC(ER1.rack_id,ER1.RIC['Powered'])
        if step == 'ER2': ERRIC(ER2.rack_id,ER2.RIC['Powered'])
        if step == 'ER2': ERRIC(ER3.rack_id,ER3.RIC)
        if step == 'ER2': ERRIC(ER4.rack_id,ER4.RIC)
        time.sleep(0.5)
        z.send(f"{step} activated".encode())
    elif data.decode() == 'ready':
        print('commands ready')
        z.send('exec'.encode())
    elif data.decode().__contains__('status'):
        step = data.decode()[0:3]
        tt = f"ER1 - - HS: {ER1.HS_count} AAA: {ER1.AAA['speed']} AFC2: {ER1.AFC_2['flow']}"
        z.send(tt.encode())
        

    else:
        nxt = data.decode()
        print('exec')
        z.send('need execution'.encode())
    





