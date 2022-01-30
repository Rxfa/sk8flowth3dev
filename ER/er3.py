
from queue import Queue
from threading import Thread
import time

#from tkinter.tix import Tree
from er_config import ER


ER3 = ER("ER3","COLA1","COL",1,1)
def startER3():
    while True:
        ER3.add_HS()
        if int(ER3.HS_count) > 5: ER3.HS_count = 0
        time.sleep(1)  

def starter3AAA():
    while True:
        ER3.add_HS()
        if int(ER3.HS_count) > 5: ER3.HS_count = 0
        time.sleep(1)  

def er3afc2flow(out_q):
	while True:
		# Produce some data
		hs_mon = ER3.AFC_2['flow']
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er3afc2flowmon(in_q):

    while True:
        # Get some data
        data3 = in_q.get()
        #if int(data3) == 3:
            #print(f"{ER3.rack_id} value is 3")
        # Process the data
        #else: print(f"{ER3.rack_id} HS : {data3}")
        if data3 < 25: print('Low AFC2')
        else: print(f"{ER3.rack_id} AFC2 Flow speed : {data3} kg/hr")
        

def er3hs(out_q):
	while True:
		# Produce some data
		hs_mon = ER3.HS_count
        
		out_q.put(hs_mon);time.sleep(1)
		
# A thread that consumes data
def er3hsmon(in_q):

    while True:
        # Get some data
        data3 = in_q.get()
        if int(data3) == 3:
            print(f"{ER3.rack_id} value is 3")
        # Process the data
        else: print(f"{ER3.rack_id} HS : {data3}")

def er3AAA(out_q):
    aaa_mon = ER3.AAA['speed']
    out_q.put(aaa_mon);time.sleep(1)

def er3AAAmon(in_q):
    while True:
        aaa3 = in_q.get()
        if aaa3 < 28000 : print('ER3 Fan Spped Low');time.sleep(0.5)
        else: print(f"{ER3.rack_id} AAA Fan Speed : {aaa3}")

#print(ER3.AFC_2['speed'])
time.sleep(1)
q_er3aaa = Queue()
er3aaa = Thread(target=starter3AAA)

q_er3afc2 = Queue()
er3_afc2_flow = Thread(target=er3afc2flow)
#er3_afc2_flow.start()

q_er3HS = Queue()
er3HS = Thread(target=startER3)
#er3HS.start()